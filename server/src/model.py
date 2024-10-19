from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

db = "/sqlite.db"

engine = create_engine("sqlite://" + db, echo=True)

metadata = MetaData()


data_model = Table(
    "data_model_table",
    metadata,
    Column("id", String, primary_key=True),
    Column("name", String),
    Column("value", String),
)

metadata.create_all(engine)
