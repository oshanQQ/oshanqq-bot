FROM python:3.10.0

RUN apt-get update \
  && apt-get -y install locales \
  && localedef -f UTF-8 -i ja_JP ja_JP.UTF-8 \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN pip install janome \
  requests \
  requests-oauthlib \
  python-dotenv

RUN pip install --upgrade pip
