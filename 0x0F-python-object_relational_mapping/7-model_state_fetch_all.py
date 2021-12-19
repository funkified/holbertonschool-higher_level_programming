#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sqlalchemy
from sys import argv

engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
    argv[1], argv[2], 'localhost', argv[3]))
Base.metadata.create_all(engine)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

for state in session.query(State).order_by(State.id).all():
    print("{}: {}".format(state.id, state.name))
session.close()
