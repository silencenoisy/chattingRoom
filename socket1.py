from flask import Flask, render_template, make_response, redirect, url_for, request
from flask_socketio import SocketIO, emit, send,join_room,leave_room
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = "pig"
app.debug = True
async_mode = None
socketio = SocketIO(app, cors_allowed_origins='*', async_mode=async_mode)
# socketio.init_app(app,cors_allowed_origins="*")


name_space = "/test"


# name_space = "/"

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    data = request.form
    username = data.get('username')
    room_num = data.get('room_num', type=int,default=-1)
    if username is not None and room_num!=-1:
        return redirect(url_for('chatting', user=username, room=room_num))
    return redirect(url_for('index'))


@app.route('/chatting', methods=['GET'])
def chatting():
    data = request.args
    username = data.get('user')
    room_num = data.get('room', type=int)
    if username is not None and room_num is not None:
        return render_template('client.html',user=username, room=room_num)
    return "参数错误!"



@socketio.on('connect',namespace=name_space)
def test_connect():
    print("Ssss")
    emit('my response', {'data': 'Connect'})
    print(request.url)


@socketio.on('disconnect')
def test_disconnect(data):
    print('Client disconnect')
    data = data['data']
    room = data['room']
    user = data['user']
    leave_room(room)

@socketio.on('join',namespace=name_space)
def on_join(data):
    data = data['data']
    room = data['room']
    user = data['user']
    join_room(room)
    send("用户：%s 加入房间"%user, to=[room])
    print("join room",data)

@socketio.on('leave',namespace=name_space)
def on_leave(data):
    data = data['data']
    room = data['room']
    user = data['user']
    leave_room(room)
    send("用户：%s 离开房间"%user, to=[room])
    emit("left_room")
    print("leave room",data)


@socketio.on('sumbit_chat_broadcast', namespace=name_space)
def broadcast_message(data):
    print("receive:",data)
    data = data['data']
    senddata = {
        "user":data['user'],
        "content":data['content'],
        "room":data['room'],
    }
    emit('show_chat_broadcast', {'data': senddata}, broadcast=True)

@socketio.on('sumbit_chat', namespace=name_space)
def chat_message(data):
    print("receive:",data)
    data = data['data']
    room = data['room']
    print(type(room))
    senddata = {
        "user":data['user'],
        "content":data['content'],
        "room":room,
    }
    emit('show_chat', {'data': senddata}, to=[room])


if __name__ == '__main__':
    socketio.run(app)


