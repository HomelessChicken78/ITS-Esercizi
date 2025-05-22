FROM python:3.11.11

COPY py_req.txt /
RUN pip install -r py_req.txt

RUN mkdir /app
COPY app.py /app
WORKDIR /app