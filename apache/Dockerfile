FROM httpd:2-alpine

#Copy apache vhost file to proxy php requests to php-fpm container

COPY demo.apache.conf /usr/local/apache2/conf/demo.apache.conf
RUN echo "Include /usr/local/apache2/conf/demo.apache.conf" \
	>> /usr/local/apache2/conf/httpd.conf

RUN sed -i 's/LoadModule reqtimeout_module modules\/mod_reqtimeout.so/ #LoadModule reqtimeout_module modules\/mod_reqtimeout.so/' /usr/local/apache2/conf/httpd.conf

RUN  sed -i 's/LoadModule mpm_event_module modules\/mod_mpm_event.so/ #LoadModule mpm_event_module modules\/mod_mpm_event.so/' /usr/local/apache2/conf/httpd.conf

RUN   sed -i 's/#LoadModule mpm_prefork_module modules\/mod_mpm_prefork.so/LoadModule mpm_prefork_module modules\/mod_mpm_prefork.so/' /usr/local/apache2/conf/httpd.conf
#Copy Website Files into the web destination path: /var/www/html/

COPY ./epic-games/epic-games.jpg ${WEB_DESTINATION_PATH}/epic-games.jpg
COPY ./epic-games/index.php ${WEB_DESTINATION_PATH}/index.php
COPY ./epic-games/styles.css ${WEB_DESTINATION_PATH}/styles.css




