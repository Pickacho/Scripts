from flask import Flask
from redis import Redis

app =Flask(__name__)
redisDB = Redis(host=(os.getenv('HOST')), port=os.port('PORT'))

@app.route('/')
def welcomeToKodeKloud():

    redisDB.incr('visitorCount')
    visitCount = str(redisdb.get('visitorCount'), 'utf-8')
    return "Welcome to KodeKloud! visitor Count: " + visitCount 

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
