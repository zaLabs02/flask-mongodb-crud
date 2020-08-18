FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /base_app
WORKDIR /base_app
COPY requirements.txt /base_app/
RUN pip install -r requirements.txt --no-cache-dir
COPY . /base_app/