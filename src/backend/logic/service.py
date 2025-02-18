from uuid import uuid4
from sqlalchemy.orm import sessionmaker
from logic.model import engine, data_model

session = sessionmaker(bind=engine)()


def service_create(payload):
    try:
        payload["id"] = str(uuid4())
        session.execute(data_model.insert().values(payload))
        session.commit()
        return payload
    except Exception as e:
        print(e)
        session.rollback()
        raise


def service_read(where):
    try:
        for key, value in where.items():
            result = (
                session.query(data_model)
                .where(getattr(data_model.c, key) == value)
                .first()
            )
            return {
                column.name: getattr(result, column.name)
                for column in data_model.columns
            }
    except Exception as e:
        print(e)
        session.rollback()
        raise


def service_read_all():
    try:
        result = session.query(data_model).all()
        session.commit()
        return [row._asdict() for row in result]
    except Exception as e:
        print(e)
        session.rollback()
        raise


def service_update(payload):
    try:
        for key, value in payload.items():
            result = (
                session.query(data_model)
                .where(getattr(data_model.c, key) == value)
                .update(payload)
            )
        session.commit()
        return result
    except Exception as e:
        print(e)
        session.rollback()
        raise


def service_delete(where):
    try:
        for key, value in where.items():
            result = (
                session.query(data_model)
                .where(getattr(data_model.c, key) == value)
                .delete()
            )
        session.commit()
        return result
    except Exception as e:
        print(e)
        session.rollback()
        raise
