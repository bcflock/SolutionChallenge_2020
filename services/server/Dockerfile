FROM nginx

RUN apt-get update 

RUN chown -R nginx:nginx /usr/share 

COPY ./html /usr/share/nginx/html

COPY nginx.conf /etc/nginx/

COPY mysite.conf /etc/nginx/sites-available/

COPY python_uwsgi.conf /etc/nginx/nginxconfig.io/
COPY security.conf /etc/nginx/nginxconfig.io/
COPY general.conf /etc/nginx/nginxconfig.io/


ENV NGINX_HOST=localhost
ENV NGINX_PORT=80