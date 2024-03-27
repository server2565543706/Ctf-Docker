import random
import time
import socket
import threading
from flag import flag  # 确保有一个名为 flag.py 的文件，其中定义了 flag 变量
import hashlib
from secrets import token_hex

def generate_challenge():
    return token_hex(3)[:5]  # 生成五位随机十六进制字符

def is_valid_hash(challenge, player_input):
    sha = hashlib.sha256()
    sha.update(player_input.encode())
    return sha.hexdigest()[:5] == challenge

def generate_seed():
    return int(time.time() / 100)

def play_round(player_choice):
    choices_map = {0: "石头", 2: "剪刀", 5: "布"}
    choices = list(choices_map.keys())
    server_choice = random.choice(choices)

    win_conditions = {(0, 2), (2, 5), (5, 0)}  # 石头赢剪刀，剪刀赢布，布赢石头
    if (player_choice, server_choice) in win_conditions:
        return choices_map[server_choice], True
    else:
        return choices_map[server_choice], False

def handle_client(client_socket, addr):
    try:
        seed = generate_seed()
        random.seed(seed)
        win_count = 0

        challenge = generate_challenge()
        client_socket.send(f"sha256(?)[0:5]=={challenge}\n".encode())

        player_hash = client_socket.recv(1024).decode().strip()
        if not is_valid_hash(challenge, player_hash):
            client_socket.send("校验失败。\n".encode())
            return

        for i in range(100):
            client_socket.send("请选择石头(0)、剪刀(2)或布(5): ".encode())
            player_choice = int(client_socket.recv(1024).decode().strip())

            if player_choice not in [0, 2, 5]:
                client_socket.send("选择无效，请选择石头(0)、剪刀(2)或布(5)。\n".encode())
                break

            server_choice, result = play_round(player_choice)
            if result:
                win_count += 1
                client_socket.send(f"你赢了这一轮！师兄出的是：{server_choice}\n".encode())
            else:
                client_socket.send(f"你输了。师兄出的是：{server_choice}\n".encode())
                break

        if win_count == 100:
            client_socket.send(f"恭喜，你赢得了所有的轮次！这是你的 flag: {flag}\n".encode())
        else:
            client_socket.send("挑战失败，请再试一次。\n".encode())

    except Exception as e:
        print(f"与 {addr} 的连接发生错误: {e}")
    finally:
        client_socket.close()

def main():
    host = '0.0.0.0'
    port = 6335

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen()

    print(f"Listening on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_thread.start()

if __name__ == "__main__":
    main()
