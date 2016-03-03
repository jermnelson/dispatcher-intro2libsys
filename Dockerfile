# Dockerfile for Intro2Libsys.info Main Website
FROM python:3.5.1
MAINTAINER Jeremy Nelson <jermnelson@gmail.com>

# Set environmental variables
ENV DISPATCH_HOME /opt/dispatcher
ENV WEB_HOME /opt/intro2libsys
ENV NGINX_HOME /etc/nginx


# Update Ubuntu, Install setup tools, nginx, and Git
RUN apt-get update && apt-get install -y && \
  apt-get install -y python3-setuptools &&\
  apt-get install -y git &&\
  apt-get install -y  nginx &&\
  apt-get install -y python3-pip &&\
  mkdir $DISPATCH_HOME

# Copy dispatcher.py
COPY dispatcher.py $DISPATCH_HOME/dispatcher.py
COPY requirements.txt $DISPATCH_HOME/requirements.txt

# Clone intro2libsys and all presentation 
RUN cd /opt/ \
  && git clone https://github.com/jermnelson/intro2libsys.git $WEB_HOME \
  && mkdir 2014 && mkdir 2015 && mkdir 2016 && mkdir courses \
  && git clone https://github.com/jermnelson/atla-2015.git /opt/2015/atla-2015 \
  && git clone https://github.com/jermnelson/calcon-2015.git /opt/2015/calcon-2015.git \
  && git clone https://github.com/jermnelson/ccc-forum-2015.git /opt/2015/ccc-forum-2015 \
  && git clone https://github.com/jermnelson/CoASL-RDA-LinkedData.git /opt/2014/coasl-rda-linked-data \
  && git clone https://github.com/jermnelson/code4lib-2015-talk.git /opt/2015/code4lib-2015-talk \
  && git clone https://github.com/jermnelson/fac-iot.git /opt/2015/fac-iot \
  && git clone https://github.com/jermnelson/focused-redis-topics.git /opt/courses/focused-redis-topics \
  && git clone https://github.com/jermnelson/islandora-camp-colorado.git /opt/2014/islandora-camp-colorado \
  && git clone https://github.com/jermnelson/lita-library-linked-data.git /opt/2014/lita-library-linked-data \
  && git clone https://github.com/jermnelson/introduction-to-redis.git /opt/courses/introduction-to-redis \
  && git clone https://github.com/jermnelson/next-library-systems.git /opt/2014/next-library-systems \
  && git clone https://github.com/jermnelson/niso-2015-webinar.git /opt/2015/niso-2015-webinar \
  && git clone https://github.com/jermnelson/open-repository-2015.git /opt/2015/open-repository-2015 \
  && git clone https://github.com/jermnelson/pycon-2014-poster.git /opt/2014/pycon-2014-poster \
  && git clone https://github.com/jermnelson/pyconjp-2015.git /opt/2015/pycon-jp-2015 \
  && cd $DISPATCH_HOME && pip3 install -r requirements.txt

WORKDIR $DISPATCH_HOME

# EXPOSE Port 
EXPOSE 5000
CMD ["python", "dispatcher.py"]
