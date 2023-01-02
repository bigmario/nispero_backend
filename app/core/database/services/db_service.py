from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import Settings

conf = Settings()


SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{conf.db_user}:{conf.db_password}@{conf.db_host}:{conf.db_port}/{conf.db_name}"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=False if conf.log_level == "info" else True
)

# SQLALCHEMY_DATABASE_URL = "sqlite:///./data.db"


# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}, echo=True
# )


Base = declarative_base()


# Dependency
def get_db():
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_db():
    Base.metadata.create_all(bind=engine)
