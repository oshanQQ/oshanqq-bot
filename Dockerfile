FROM python:3.10.0

RUN apt-get update \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN pip install janome \
  requests \
  requests-oauthlib \
  python-dotenv

RUN pip install --upgrade pip
