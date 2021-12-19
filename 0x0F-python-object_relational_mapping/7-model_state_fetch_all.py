#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sqlalchemy


engine = create_engine('mysql://root:root@localhost/hbtn_0e_6_usa')
Base.metadata.create_all(engine)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

for state in session.query(State).order_by(State.id).all():
    print("{}: {}".format(state.id, state.name))
session.close()
