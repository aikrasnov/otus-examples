import asyncio
import random
import time

counter = 0


async def handle_echo(reader, writer):
    global counter
    counter += 1
    local_counter = counter
    randint = random.randint(1, 10)
    time.sleep(randint)
    await asyncio.sleep(randint)
    # data = await reader.read(1024)
    # message = data.decode()
    # addr = writer.get_extra_info("peername")
    # print(f"Получено {message} от {addr}, спал {randint}")
    print(f"Когда я уснул было {local_counter}, когда проснулся {counter}")
    writer.close()


loop = asyncio.get_event_loop()
coro = asyncio.start_server(handle_echo, "127.0.0.1", 10001, loop=loop)
server = loop.run_until_complete(coro)
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
