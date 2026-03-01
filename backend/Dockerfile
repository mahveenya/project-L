FROM python:3.12-slim

WORKDIR /backend

RUN apt-get update && apt-get install -y --no-install-recommends \
  gcc \
  libpq-dev \
  netcat-openbsd \
  && rm -rf /var/lib/apt/lists/*


COPY . .
RUN pip install --upgrade pip \
  && pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["./scripts/entrypoint.sh"]