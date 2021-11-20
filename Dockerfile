FROM python:3.10.0

RUN apt-get update && apt-get install -y \
  hogehoge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

  python-dotenv
