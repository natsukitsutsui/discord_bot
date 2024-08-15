FROM python:3.9.11

RUN mkdir -p /root/workspace
COPY requirements.txt /root/workspace/
WORKDIR /root/workspace

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt
