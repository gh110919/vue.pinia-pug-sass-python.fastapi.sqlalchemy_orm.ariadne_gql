from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.router import router
from utils.rel_path import rel_path
import uvicorn
from ariadne import load_schema_from_path, make_executable_schema
from ariadne.asgi import GraphQL
from src.resolver import resolvers


server = FastAPI()
server.openapi_url = "/openapi.json"
server.include_router(router, prefix="/api")
server.add_route(
    "/gql",
    GraphQL(make_executable_schema(load_schema_from_path("schema.gql"), resolvers)),
)

server.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def start():
    uvicorn.run(
        "main:server",
        host="127.0.0.2",
        port=80,
        # ssl_certfile=rel_path(__file__, "../certs/fullchain.pem"),
        # ssl_keyfile=rel_path(__file__, "../certs/private_key.pem"),
    )


if __name__ == "__main__":
    start()
