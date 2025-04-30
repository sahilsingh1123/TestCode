"""
Server for streaming data to client asynchronously using asyncio
"""

import asyncio


class DataProducer:
    """Produce an endless stream of newline-terminated messages."""

    def __init__(self, interval: float = 0.1):
        self.interval = interval
        self.counter = 0

    async def messages(self):
        """Async generator yielding one message per interval."""
        while True:
            msg = f"data-{self.counter}\n"
            self.counter += 1
            yield msg  # produce message :contentReference[oaicite:4]{index=4}
            await asyncio.sleep(self.interval)


async def client_handler_advance(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    addr = writer.get_extra_info("peername")
    print(f"Client connected: {addr}")
    producer = DataProducer(interval=0.1)

    try:
        async for message in producer.messages():  # get messages :contentReference[oaicite:6]{index=6}
            writer.write(message.encode())  # send data :contentReference[oaicite:7]{index=7}
            await writer.drain()  # apply back-pressure :contentReference[oaicite:8]{index=8}
    except asyncio.CancelledError:
        print(f"Streaming to {addr} cancelled.")
    except Exception as e:
        print(f"Connection to {addr} failed. - {str(e)}")
    finally:
        writer.close()  # close connection :contentReference[oaicite:9]{index=9}
        await writer.wait_closed()


# async def client_handler(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
#     addr = writer.get_extra_info('peername')
#     print(f"Client connected: {addr}")
#
#     try:
#         counter = 0
#         # Stream indefinitely (or until you Ctrl+C)
#         while True:
#             message = f"data-{counter}\n"
#             writer.write(message.encode())           # send a line
#             await writer.drain()                     # back-pressure :contentReference[oaicite:5]{index=5}
#             counter += 1
#             await asyncio.sleep(0.1)                 # simulate interval :contentReference[oaicite:6]{index=6}
#     except asyncio.CancelledError:
#         print(f"Connection to {addr} cancelled.")
#     except Exception as e:
#         print(f"Connection to {addr} failed. - {str(e)}")
#     finally:
#         writer.close()                              # close writer :contentReference[oaicite:7]{index=7}
#         await writer.wait_closed()
#         print(f"Client disconnected: {addr}")


async def main():
    server = await asyncio.start_server(
        client_handler_advance, "127.0.0.1", 8888  # start server :contentReference[oaicite:8]{index=8}
    )
    addrs = ", ".join(str(sock.getsockname()) for sock in server.sockets)
    print(f"Serving on {addrs}")

    async with server:
        await server.serve_forever()  # run until interrupted


if __name__ == "__main__":
    try:
        asyncio.run(main())  # run event loop :contentReference[oaicite:9]{index=9}
    except KeyboardInterrupt:
        print("Server shut down by user")
