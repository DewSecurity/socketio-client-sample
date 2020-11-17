import socketio
from socketio.exceptions import ConnectionError

# standard Python
sio = socketio.Client()

@sio.event
def connect():
    print("I'm connected!")
    sio.emit('pic', {'id': '19Jm5In9JHIUl41k5QifwOiGhHpQGcC5l'})
    #sio.emit('pic', 'chez so suk')
    print("sended")

#@sio.event
#def connect_error():
#    print("The connection failed!")

@sio.event
def disconnect():
    print("I'm disconnected!")

print('starting')
try:
    sio.connect('http://192.168.43.71:3500')
    print('ok')
    print('my sid is', sio.sid)

except ConnectionError as e:
    print('Connection Error: ', e)
