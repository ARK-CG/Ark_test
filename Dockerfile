FROM python:3
RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi
ENV PYTHONUNBUFFERED 1
RUN mkdir /web
WORKDIR /web
ADD requirements.txt /web/
RUN pip install -r requirements.txt
ADD . /web/
RUN chown -R uwsgi /web
COPY /config/uwsgi.sh /uwsgi.sh
RUN chmod +x /uwsgi.sh