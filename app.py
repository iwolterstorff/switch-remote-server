import asyncio

import sanic
import ujson


app = sanic.Sanic("switch-remote-server")
app.config.from_pyfile('./.env')

app.static('/', './static/index.html')
app.static('/static', './static')

@app.websocket('/websocket')
async def socket(request, ws):
    while True:
        report = await ws.recv()
        print(ujson.loads(report))

app.run(host=app.config.HOST, port=app.config.PORT)