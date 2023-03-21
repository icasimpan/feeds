FROM python:alpine3.17

COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

USER github
RUN mkdir /home/github/conf
COPY conf/feed-input.json /home/github/conf/feed-input.json
COPY feedlist.py /home/github/feedlist.py

RUN python feedlist.py > /home/github/web3-feeds.md
RUN cat /home/github/web3-feeds.md

ENTRYPOINT [python]
