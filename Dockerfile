FROM nginx

ADD Teleferic/static /srv/www/haku_static

ADD nginx.conf /etc/nginx/