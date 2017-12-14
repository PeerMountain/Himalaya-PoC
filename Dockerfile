FROM nginx

COPY Teleferic/static /srv/www/haku_static

COPY nginx.conf /etc/nginx/