FROM ubuntu:18.04

EXPOSE 5000

RUN apt -y update \
    && apt install -y \
    apt-utils \
    apt-transport-https \
    build-essential \
    python3.8 -y \
    python3-dev \
    python-pip \
    python3-pip \
    sqlite3 \
    software-properties-common -y 

WORKDIR /app
ADD . /app
RUN pip3 install --upgrade pip \
    && pip3 install -r requirements.txt

CMD ["python3", "app.py"]


