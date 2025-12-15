from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os


from sqlalchemy import Column, String, Text, DateTime, ForeignKey, Integer
from datetime import datetime


# load_dotenv('../env_var.txt')
load_dotenv('env_var.txt')

db_pswd = os.getenv('db_pswd')
db_name = os.getenv('db_name')

# print(db_name, db_pswd)

# Database URL format: "postgresql://<username>:<pswd>@localhost:5432/<db_name>" 
db_conn_str = f"postgresql://postgres:{db_pswd}@localhost:5432/{db_name}"
# db_conn_str = (
#     f"postgresql"
#     f"://postgres:{db_pswd}"
#     f"@localhost:5432" 
#     f"/{db_name}" 
# )
# print(db_conn_str)
# Using engine you connect with database. 
engine = create_engine(db_conn_str)
# To create a session with database. A session is created once you connect with database.
SessionCreator = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass

# ORM   
class Entry(Base):
    __tablename__ = "Entry"

    id = Column(Text, primary_key=True)
    fname = Column(Text)
    lname = Column(Text)
    dp_url = Column(String)
    created_on = Column(DateTime, default=datetime.utcnow)