from ariadne import QueryType, MutationType
from logic.service import (
    service_create,
    service_delete,
    service_read,
    service_read_all,
    service_update,
)

query = QueryType()
mutation = MutationType()


async def resolve_create_data(_, __, data):
    return service_create(data)


async def resolve_get_data(_, __, data):
    return dict(service_read(data))


async def resolve_get_all_data(*_):
    return [dict(row) for row in service_read_all()]


async def resolve_update_data(_, __, data):
    return service_update(data)


async def resolve_delete_data(_, __, data):
    return service_delete(data)


query.set_field("getAllData", resolve_get_all_data)
query.set_field("getData", resolve_get_data)

mutation.set_field("createData", resolve_create_data)
mutation.set_field("updateData", resolve_update_data)
mutation.set_field("deleteData", resolve_delete_data)

resolvers = [query, mutation]
