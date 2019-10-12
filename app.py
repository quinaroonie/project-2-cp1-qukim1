import os, flask
import flask_socketio 
import flask_sqlalchemy


app = flask.Flask(__name__)


import models
socketio = flask_socketio.SocketIO(app) 


@app.route('/')
def hello():
    return flask.render_template('index.html')

    
@socketio.on('connect')
def on_connect():
    print('Someone connected!')
    flask_socketio.emit('update', {
        'data': 'Got your connection!'
    })



@socketio.on('message')
def get_message(data):
    print("message data: " + data.new_message) 

socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
)



  
