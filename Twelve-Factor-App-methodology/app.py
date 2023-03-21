from flask import Flask
from redis import Redis
import os

app = Flask(__name__)
redisDb = Redis(host=(os.getenv('HOST')), port=os.getenv(str'PORT'))


@app.route('/')
def welcometokodekloud():
    redisDb.incr('visitorCount')
    visitCount = str(redisDb.get('visitorCount'), 'utf-8')
    return "Welcome to KodeKloud! visitor Count: " + visitCount


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)