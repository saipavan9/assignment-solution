import socketio
import logging
import logging_loki

handler = logging_loki.LokiHandler(
    url="http://loki:3100/loki/api/v1/push", 
    tags={"application": "my-app"},
    auth=("username", "password"),
    version="1",
)

logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
logging.basicConfig(filename='server.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s',level=logging.DEBUG)
logger.error(
    "Something happened", 
    extra={"tags": {"service": "my-service"}},
)





sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')
app = socketio.ASGIApp(sio)

m1 = 0
m2 = 0
m3 = 0

@sio.event
async def connect(sid, environ):
    print(sid, 'connected')
    logger.warning(sid)
    logger.info("connected")
    await sio.emit("init",{"m1":m1,"m2": m2,",m3": m3})


@sio.event
async def disconnect(sid):
    logger.warning("disconnected")
    print(sid, 'disconnected')


@sio.event
async def update(sid,data):
    global m1, m2 , m3
    if(data == "m1"):
        m1 = m1 ^ 1
    elif(data == m2):
        m2 = m2 ^ 1
    else:
        m3 = m3 ^ 1

    logger.info("update event")
    await sio.emit("change", data)