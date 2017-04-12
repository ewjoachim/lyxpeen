FROM python:3.6

EXPOSE 8080
ENV LC_ALL C.UTF-8
USER root

ADD . /root/lyxpeen

WORKDIR /root/lyxpeen

RUN pip install . -r requirements/server.txt

CMD ["./serve"]
