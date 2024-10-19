from fastapi import APIRouter
from src.controller import (
    controller_create,
    controller_read_all,
    controller_read,
    controller_update,
    controller_delete,
)

router = APIRouter()

router.add_api_route("/data", controller_create, methods=["POST"])
router.add_api_route("/data/single", controller_read, methods=["GET"])
router.add_api_route("/data", controller_read_all, methods=["GET"])
router.add_api_route("/data", controller_update, methods=["PUT"])
router.add_api_route("/data", controller_delete, methods=["DELETE"])
