import asyncio
import os
import signal
from time import time

from litestar import Litestar, Request, get

SHUTDOWN_TIMEOUT = int(os.environ["SHUTDOWN_TIMEOUT"])


class MachineOverlord:
    def __init__(self) -> None:
        pass

    async def update_last_request_timestamp(self) -> None:
        self.last_request_timestamp = time()

    async def start(self):
        print("Starting Machine Overlord...")
        self.last_request_timestamp = time()
        while True:
            await asyncio.sleep(SHUTDOWN_TIMEOUT)
            if self.last_request_timestamp - time() - SHUTDOWN_TIMEOUT:
                print("Shutting down due to inactivity...")
                os.kill(os.getpid(), signal.SIGTERM)


machine_overlord = MachineOverlord()


async def after_startup_handler(app: Litestar) -> None:
    asyncio.create_task(machine_overlord.start())
    return


async def before_request_handler(request: Request) -> None:
    print("Updating last request timestamp...")
    await machine_overlord.update_last_request_timestamp()
    return


@get("/")
async def get_home() -> dict[str, str]:
    return {"status": "success"}


app = Litestar(
    route_handlers=[get_home],
    after_startup=[after_startup_handler],
    before_request=before_request_handler,
)
