from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# DATABASE RAILWAY

senha = "JTorFKcjfjzUxlAYcrnI"
username = "postgres"
database_name = "railway"

DATABASE_URL = f"postgresql://{username}:{senha}@containers-us-west-161.railway.app:7324/{database_name}"


""" # DATABASE LOCAL

senha = "root"
username = "postgres"
database_name = "python_db"

DATABASE_URL = f"postgresql://{username}:{senha}@localhost:5432/{database_name}"  """

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()