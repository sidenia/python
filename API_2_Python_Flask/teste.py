from flask import Flask
app = Flask(__name__) #nome do app vai ser teste


@app.route('/') #url ou endpoint  cada método da view vai para 1 end point
def hello_world():
    return "hello world."


app.run()
