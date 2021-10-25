FROM python:3.9

LABEL maintainer="JP3Pe"

#Create user for storage-service
RUN adduser sanic
USER sanic

WORKDIR /home/sanic/project
# Copy source files
COPY . .
RUN pip install -r requirements.txt

EXPOSE 3004
