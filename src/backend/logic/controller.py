from fastapi import Request
from fastapi.responses import JSONResponse
from logic.service import (
    service_create,
    service_delete,
    service_read,
    service_read_all,
    service_update,
)


async def controller_create(request: Request):
    try:
        return JSONResponse(
            status_code=200,
            content={
                "success": True,
                "message": service_create(await request.json()),
            },
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": str(e),
            },
        )


async def controller_read(request: Request):
    try:
        return JSONResponse(
            status_code=200,
            content={
                "success": True,
                "message": service_read(await request.json()),
            },
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": str(e),
            },
        )


async def controller_read_all():
    try:
        return JSONResponse(
            status_code=200,
            content={
                "success": True,
                "message": [dict(row) for row in service_read_all()],
            },
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": str(e),
            },
        )


async def controller_update(request: Request):
    try:
        return JSONResponse(
            status_code=200,
            content={
                "success": True,
                "message": service_update(await request.json()),
            },
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": str(e),
            },
        )


async def controller_delete(request: Request):
    try:
        return JSONResponse(
            status_code=200,
            content={
                "success": True,
                "message": service_delete(await request.json()),
            },
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": str(e),
            },
        )
