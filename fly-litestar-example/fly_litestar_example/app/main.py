import os

from litestar import Litestar, Request, get


@get("/")
async def get_home() -> dict[str, str]:
    return {
        "status": "success",
        "data": {
            "fly_alloc_id": os.getenv("FLY_ALLOC_ID"),
            "fly_app_name": os.getenv("FLY_APP_NAME"),
            "fly_region": os.getenv("FLY_REGION"),
        },
    }


app = Litestar(
    route_handlers=[get_home],
)
