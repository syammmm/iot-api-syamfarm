import os
from sqlalchemy import create_engine

print("Cloud SQL socket exists:",
      os.path.exists(f"/cloudsql/{os.getenv('CLOUD_SQL_INSTANCE')}"))

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
CLOUD_SQL_INSTANCE = os.getenv("CLOUD_SQL_INSTANCE")

# connector = Connector()

# def getconn():
#     return connector.connect(
#         INSTANCE_CONNECTION_NAME,
#         "psycopg2",
#         user=DB_USER,
#         password=DB_PASS,
#         db=DB_NAME,
#     )

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@10.16.128.3:5432/{DB_NAME}",
    pool_size=5,
    max_overflow=2,
    pool_pre_ping=True,
    connect_args={"sslmode": "require"}
    # "postgresql+psycopg2://postgres:DB_PASSWORD@10.16.128.3:5432/postgres",
    # pool_size=5,
    # max_overflow=2,
    # pool_pre_ping=True,
    # connect_args={"sslmode": "require"}
)