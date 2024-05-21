# https://hub.docker.com/_/python
FROM python

WORKDIR app
COPY final_project /app
RUN python3 -m pip install -r requirements.txt
WORKDIR final_project/mock/application

FROM percona
