# Container image that runs your code
FROM python:alpine3.17

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY entrypoint.sh /entrypoint.sh
COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt
# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]
