import uvicorn
from ariadne import load_schema_from_path, make_executable_schema
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from ariadne.asgi import GraphQL
from logic.router import router
from logic.resolver import resolvers
from utils.rel_path import rel_path

server = FastAPI()
server.openapi_url = "/openapi.json"
server.include_router(router, prefix="/api")

load = load_schema_from_path("schema.gql")
make = make_executable_schema(load, resolvers)

server.add_route("/gql", GraphQL(make))

server.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ssl = {
    "cert": rel_path(__file__, "../../certs/fullchain.pem"),
    "key": rel_path(__file__, "../../certs/private_key.pem")
}


def start():
    uvicorn.run(
        "__init__:server",
        host="127.0.0.2",
        port=443,
        ssl_certfile=ssl["cert"],
        ssl_keyfile=ssl["key"],
    )


if __name__ == "__main__":
    start()
