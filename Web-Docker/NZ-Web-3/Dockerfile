# Pull base image 
FROM ubuntu:trusty

# update source  
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe"> /etc/apt/sources.list \
  && apt-get update \
  && apt-get install -y apache2 php5 php5-mysql \
  && apt-get clean && rm -rf /var/lib/apt/lists/* 


RUN rm /var/www/html/index.html
COPY app /var/www/html/
COPY start.sh /usr/bin
RUN chmod +x /usr/bin/start.sh
EXPOSE 80
CMD ["/usr/bin/start.sh"]
 
