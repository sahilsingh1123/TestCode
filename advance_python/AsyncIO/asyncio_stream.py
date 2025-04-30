# client.py
import asyncio
import aiofiles


async def stream_reader(host: str, port: int, queue: asyncio.Queue):
    reader, writer = await asyncio.open_connection(host, port)           # open TCP stream :contentReference[oaicite:4]{index=4}&#8203;:contentReference[oaicite:5]{index=5}
    try:
        while True:
            line = await reader.readline()                                # read one line at a time :contentReference[oaicite:6]{index=6}
            if not line:                                                  # EOF → exit loop :contentReference[oaicite:7]{index=7}
                break
            await queue.put(line.decode().rstrip())                       # enqueue for processing :contentReference[oaicite:8]{index=8}
    finally:
        writer.close()                                                    # close writer :contentReference[oaicite:9]{index=9}
        await writer.wait_closed()                                        # wait closed :contentReference[oaicite:10]{index=10}


async def processor(queue: asyncio.Queue, out_path: str):
    async with aiofiles.open(out_path, 'w') as f:
        while True:
            item = await queue.get()                                      # dequeue :contentReference[oaicite:11]{index=11}
            # transform
            await f.write(item.upper() + '\n')                            # async file write via aiofiles
            queue.task_done()


async def main():
    queue = asyncio.Queue(maxsize=50)                                     # back-pressure via maxsize :contentReference[oaicite:12]{index=12}
    host, port = '127.0.0.1', 8888
    await asyncio.gather(
        stream_reader(host, port, queue),
        processor(queue, 'output.txt'),
    )

if __name__ == '__main__':
    try:
        asyncio.run(main())                                                   # run on Python 3.10–3.13 :contentReference[oaicite:13]{index=13}
    except KeyboardInterrupt:
        print("Server shut down by user")