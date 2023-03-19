# Container image that runs your code
FROM python:alpine3.17

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY entrypoint.sh /entrypoint.sh
COPY requirements.txt /requirements.txt

RUN mkdir /conf
COPY conf/feed-input.json /conf/feed-input.json
COPY feedlist.py /feedlist.py

RUN pip install -r requirements.txt
RUN python feedlist.py > /web3-feeds.md
RUN cat /web3-feeds.md

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]
