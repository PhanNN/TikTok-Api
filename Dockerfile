FROM mcr.microsoft.com/playwright:focal

RUN apt-get update && apt-get install -y python3-pip
COPY . /app
RUN pip3 install /app
RUN python -m playwright install