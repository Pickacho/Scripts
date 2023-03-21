FROM python:3.11-alpine
WORKDIR /kodekloud-TWELVE-FACTOR-APP
COPY requirements.txt /kodekloud-TWELVE-FACTOR-APP
RUN pip install -r requirements.txt --no-cache-dir
COPY . /kodekloud-TWELVE-FACTOR-APP
CMD [ "app.py" ]
