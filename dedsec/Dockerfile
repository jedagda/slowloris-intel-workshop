FROM kalilinux/kali
# Metadata params
ARG BUILD_DATE
ARG VERSION
ARG VCS_URL
ARG VCS_REF

LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url=$VCS_URL \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.version=$VERSION \
      org.label-schema.name='Kali Linux' \
      org.label-schema.description='Official Kali Linux docker image' \
      org.label-schema.usage='https://www.kali.org/news/official-kali-linux-docker-images/' \
      org.label-schema.url='https://www.kali.org/' \
      org.label-schema.vendor='Offensive Security' \
      org.label-schema.schema-version='1.0' \
      org.label-schema.docker.cmd='docker run --rm kalilinux/kali-linux-docker' \
      org.label-schema.docker.cmd.devel='docker run --rm -ti kalilinux/kali-linux-docker' \
      org.label-schema.docker.debug='docker logs $CONTAINER' \
      io.github.offensive-security.docker.dockerfile="Dockerfile" \
      io.github.offensive-security.license="GPLv3" \
      MAINTAINER="Joshua Dagda jedagda@miners.utep.edu"
#RUN echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" > /etc/apt/sources.list && \
#echo "deb-src http://http.kali.org/kali kali-rolling main contrib non-free" >> /etc/apt/sources.list
ENV DEBIAN_FRONTEND noninteractive

# Copy the motd intro file to samsepi0l container
COPY ./text-files/motd /etc/motd


# Set up SSH server and add user with password
RUN apt-get update  && apt-get install -y kali-linux-core 
# RUN apt-get install -y kali-linux-top10
RUN apt-get install -y python3 
RUN apt-get upgrade -y python-requests
RUN apt-get install -y notmuch notmuch-vim net-tools nmap ipython ipython3 iputils-ping 

RUN vim-addon-manager install notmuch
RUN mkdir /var/run/sshd
RUN groupadd dedsec
RUN useradd -ms /bin/bash -g dedsec samsepi0l
RUN echo 'samsepi0l:dedsecrox!' | chpasswd


# Add and install lolcat for a colorful RGB experience
COPY lolcat-master /samsepi0l/
WORKDIR /samsepi0l/lolcat-master/bin/ 
RUN gem install lolcat


#Create unimatrix directory and copy unimatrix script for cool matrix introduction
RUN mkdir /usr/local/bin/unimatrix
COPY unimatrix.py /usr/local/bin/unimatrix
RUN chmod a+rx /usr/local/bin/unimatrix

#We support 256color, right? If not, you can always change this environment variable.
ENV TERM=xterm-256color

#Running ssh with keys is a good thing, right?
RUN sed -i 's/RSAAuthentication yes/RSAAuthentication no/' /etc/ssh/ssh_config

#Start the ssh service
CMD service ssh start && nginx -g 'daemon off;'
CMD ["/usr/sbin/sshd", "-D"]


#RUN echo '[ ! -z "$TERM" -a -r /etc/motd ] && cat /etc/issue && cat /etc/motd'  >> /etc/bash.bashrc

# These files are only pertaining to the slowloris workshop

WORKDIR /home/samsepi0l
RUN mkdir slowloris
COPY ./slowloris/ /home/samsepi0l/slowloris/
COPY ./text-files/README /home/samsepi0l/slowloris/
RUN chown samsepi0l:dedsec -R /home/samsepi0l/slowloris/
RUN mkdir mail/
COPY ./text-files/hellofriend.eml /home/samsepi0l/mail/
RUN chown samsepi0l:dedsec -R /home/samsepi0l/mail/



#ENV NOTVISIBLE "in users profile"
#RUN echo "export VISIBLE=now" >> /etc/profile

#RUN apt-get update \
#    && apt-get dist-upgrade \
#    && apt-get clean
#ENTRYPOINT bash
#EXPOSE 22

