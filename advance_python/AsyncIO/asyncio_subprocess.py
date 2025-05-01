"""
You can do a great deal with pure asyncio in a single process—but when you need to:

Leverage existing command-line tools

Use OS-level protocols not exposed in Python

Isolate or sandbox external code

Offload CPU-bound work beyond the GIL
"""

import asyncio


async def ping(host: str):
    proc = await asyncio.create_subprocess_exec(
        "ping",
        "-c",
        "4",
        host,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    print(f"Started ping to {host} (PID {proc.pid})")
    try:
        async for raw in proc.stdout:
            text = raw.decode().strip()
            if "time=" in text:
                print(f"{host} → {text.split('time=')[1]}")
    except asyncio.CancelledError:
        proc.kill()
        await proc.wait()
        raise
    finally:
        await proc.wait()
        print(f"{host} done with code {proc.returncode}")


async def main():
    hosts = ["8.8.8.8", "1.1.1.1", "example.com"]
    await asyncio.gather(*(ping(h) for h in hosts))


if __name__ == "__main__":
    asyncio.run(main())
