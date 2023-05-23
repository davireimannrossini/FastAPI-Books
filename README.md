# FastAPI-Books
Implementação simples do FastAPI com PostgreSQL


PostgeSQL

senha = "root"
username = "postgres"
database_name = "python_db"
DATABASE_URL = f"postgresql://{username}:{senha}@localhost:5432/{database_name}" 

__tablename__ = 'book'
id = Column(Integer, primary_key=True)
title = Column(String)
description = Column(String)
