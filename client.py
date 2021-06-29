# # import websocket
# #
# # ws = websocket.WebSocket()
# # ws.connect("ws://127.0.0.1:5000")
# # ws.send("res")
# # print(ws.recv())
# # ws.close()
# import socketio
# class LoginSocket(socketio.ClientNamespace):
#     def on_connect(self):
#         print('connected to server')
#         # I need get socket id here to emit to server
#
#
#         # sio.disconnect()
#
#     def on_python(self, *args, **kwargs):
#         print(args, kwargs, 'xxxxxxxxxxxxxxxxxxxxxx')
#
#
#     def on_disconnect(self):
#         print('disconnected from server')
#
#
# sio = socketio.Client()
# sio.register_namespace(LoginSocket('/'))
# if __name__ == '__main__':
#     sio.connect('http:/127.0.0.1:5000/')
#     sio.wait()

# from flask_socketio import SocketIO
# from flask import Flask

# app = Flask(__name__)
# app.config['SECRET_KEY'] = "pig"
# app.debug = True
# socketio = SocketIO(app, cors_allowed_origins='*')
#
# client=socketio.test_client(app,auth={"adata":"sadas"})
# print(client.get_received(namespace='/test'))
# client.send({"sss":"aaa"})
# ret = client.get_received(namespace='/test')
#
# print(ret)
# client.emit('push_ooo1',{"data":"qqq"},namespace='/test')


import json
import time
from websocket import create_connection

ws = create_connection("ws://127.0.0.1:5000")
print("Sending 'Hello, World'...")
