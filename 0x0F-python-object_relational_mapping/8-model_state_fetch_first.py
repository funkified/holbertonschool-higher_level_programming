#!/usr/bin/python3
"""
Connecting script with my database
"""
from model_state import State, Base
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
        argv[1], argv[2], 'localhost', argv[3]))
    # Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    # Session.configure(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
    session.close()
