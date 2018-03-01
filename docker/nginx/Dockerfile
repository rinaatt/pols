FROM nginx:1.12-alpine

RUN mkdir /var/www

RUN rm /etc/nginx/conf.d/default.conf
ADD pols.nginx /etc/nginx/conf.d/pols.conf
