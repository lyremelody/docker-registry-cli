FROM python:2.7-alpine

MAINTAINER lyremelody@163.com

ADD *.py /

WORKDIR /

ENTRYPOINT ["/cli.py"]
