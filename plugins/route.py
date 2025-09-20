from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.Response(
        text="""
        <body style="background-color:black; color:yellow; display:flex; justify-content:center; align-items:flex-start; height:100vh; margin:0; font-family:sans-serif; padding-top:20vh; font-size:4rem;">
            || NeonAnurag ||
        </body>
        """,
        content_type="text/html"
    )

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app


# MyselfNeon
# Don't Remove Credit 🥺
# Telegram Channel @NeonFiles
