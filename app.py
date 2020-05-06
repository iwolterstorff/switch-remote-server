import asyncio
import sys

import sanic
import ujson

import serial_utils

if (serial_port := sys.argv[1]):
    serial_utils.set_serial_port(serial_port)
else:
    print("Specify serial port on command line")

app = sanic.Sanic("switch-remote-server")
app.config.from_pyfile('./.env')

app.static('/', './static/index.html')
app.static('/static', './static')

@app.websocket('/websocket')
async def socket(request, ws):
    while True:
        data = await ws.recv()
        report = ujson.loads(data)
        serial_utils.report_out(report)

app.run(host=app.config.HOST, port=app.config.PORT)
