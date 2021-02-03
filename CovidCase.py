import csv
from numpy import genfromtxt



import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table,Column,Integer,String,Date
import glob
import os
from sqlalchemy import MetaData
from sqlalchemy.orm import mapper

Base = declarative_base()

class CovidOC(Base):
   __tablename__ = 'covid'

   uid = Column(Integer, primary_key=True)
   County= Column(String)
   State = Column(String)
   Date = Column(String)
   Confirmed = Column(String)
   Deaths = Column(String)
   Population = Column(String)

   def __repr__(self):
       return f"{self.Confirmed} - {self.County} - {self.Date} - {self.Deaths} - {self.Population} - {self.State}"


engine = create_engine('sqlite:///covid.db', echo = True)
Session = sessionmaker(bind = engine)
session = Session()
CovidOC.metadata.drop_all(engine)
CovidOC.metadata.create_all(engine)

with open('simplified_orange_county.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        c1 = CovidOC(County = lines[0], State = lines[1], Date = lines[2], Confirmed = lines[3], Deaths= lines[4], Population = lines[5])
        session.add(c1)


session.commit()

result = session.query(CovidOC).all()

for row in result:

   print(row)
