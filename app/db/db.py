from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base

# 1️⃣ Engine SOLO para crear la base (sin especificar DB)
server_engine = create_engine(
    "mysql+pymysql://root:root@localhost:3306/"
)

# Crear base si no existe
with server_engine.connect() as conn:
    conn.execute(text("CREATE DATABASE IF NOT EXISTS mi_db"))
    print("Base creada (si no existía)")

# 2️⃣ Engine real apuntando a la base
engine = create_engine(
    "mysql+pymysql://root:root@localhost:3306/mi_db"
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()