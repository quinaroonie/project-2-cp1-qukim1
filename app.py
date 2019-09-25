import os, flask
import flask_socketio 
import flask_sqlalchemy


app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app) 

import models



@app.route('/')
def hello():
    return flask.render_template('index.html')


@socketio.on('connect') 
def on_connect():
    messages = models.Message.query.all()
    
@socketio.on('connect')
def on_connect():
    print('Someone connected!')
    flask_socketio.emit('data' : 'You are Connected'
    })

@socketio.on('disconnect')
def on_disconnect():
    print('Someone disconnected!')
    
    
    html = ['<li>' + m.text + '</li>' for m in messages]
    return '<ul>' + ''.join(html) + '</ul>'
    



socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
)





  
