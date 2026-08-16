from flask_sqlalchemy import SQLAlchemy,query
from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import Column,String,Integer


from sqlalchemy import engine 



engine=engine.create_engine("sqlite:///form.db")# it connects to the database
Base=declarative_base()# it is a class which have important functionality
Session=sessionmaker(bind=engine)# it helps to communicate with database

class Student(Base):
      __tablename__="formtable"
      name=Column(String(100),primary_key=True)
      departement=Column(String(100),nullable=False)
      Date=Column(String(100),nullable=False)
      status=Column(String(50),nullable=False)
      roll=Column(Integer,nullable=False)

Base.metadata.create_all(engine)#first it checks all the thing tha are linked with base or classes that inherits the base,then if the table exist then it holds other wise it create a new table 
      