FROM debian:stable-slim
RUN apt-get update  
RUN apt-get install -y python3
COPY main.py main.py
COPY books/ books/
CMD ["python3", "main.py"]