#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_base import Base
import sqlalchemy


engine = create_engine('mysql+mysqldb://root:root@localhost/hbtn_0e_4_usa', pool_pre_ping=True)
Base.metadata.create_all(engine)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

for state in session.query(State).order_by(State.id).all():
    print("{}: {}".format(state.id, state.name))
session.close()
