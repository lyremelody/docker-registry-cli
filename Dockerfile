FROM python:2.7-alpine

ADD *.py /

WORKDIR /

ENTRYPOINT ["/cli.py"]
