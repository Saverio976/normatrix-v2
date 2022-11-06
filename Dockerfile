FROM python:3.11-slim
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get autopurge && \
    apt-get clean
RUN pip install -U pip setuptools wheel
RUN pip install -U norma2
CMD /usr/local/bin/norma2 /code
