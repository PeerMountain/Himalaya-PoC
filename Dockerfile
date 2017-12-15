FROM nginx

ADD Teleferic/static /srv/www/haku/static
ADD Docs/build /srv/www/docs

ADD nginx.conf /etc/nginx/