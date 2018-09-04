from sqlalchemy import create_engine, MetaData

from .config import DATABASE_URI

engine = create_engine(DATABASE_URI)
metadata = MetaData(bind=engine)

from . import tables  # noqa

conn = engine.connect()
# do stuff here
# http://docs.sqlalchemy.org/en/latest/core/connections.html
conn.close()
