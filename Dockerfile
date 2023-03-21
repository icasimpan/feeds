FROM python:alpine3.17

COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

RUN adduser icasimpan -D
RUN mkdir /home/icasimpan/conf
COPY conf/feed-input.json /home/icasimpan/conf/feed-input.json
COPY feedlist.py /home/icasimpan/feedlist.py

RUN python feedlist.py > /home/icasimpan/web3-feeds.md
RUN cat /home/icasimpan/web3-feeds.md

ENTRYPOINT [python]
