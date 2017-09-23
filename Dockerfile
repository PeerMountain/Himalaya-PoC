FROM nginx:alpine

COPY nginx.conf /etc/nginx/
COPY Docs/static/ /srv/www/docs_static
COPY Teleferic/static/ /srv/www/haku_static