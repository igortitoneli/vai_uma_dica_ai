FROM python:3.11.3-slim-buster

RUN addgroup --system app && adduser --system --group app

WORKDIR /home/api_vuda

COPY ./requirements.txt api_vuda/requirements.txt

RUN apt-get update && apt-get install -y --no-install-recommends netcat-openbsd git
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --upgrade --force-reinstall -r api_vuda/requirements.txt

COPY ./src .

ENTRYPOINT [ "/bin/bash", "-c", "flask run --host=0.0.0.0 --port=50000 --debug" ]
