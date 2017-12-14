FROM nginx

COPY nginx.conf /etc/nginx/
COPY Docs/ /srv/www/docs_static
COPY Teleferic/static/ /srv/www/haku_static