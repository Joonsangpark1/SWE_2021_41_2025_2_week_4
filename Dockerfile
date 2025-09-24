FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y python3

WORKDIR /app

CMD ["python3","/app/bind_mount/is_happy.py"]