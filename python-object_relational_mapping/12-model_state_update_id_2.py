#!/usr/bin/python3
"""
This module changes the name of a State object where id = 2
to "New Mexico" in the database hbtn_0e_6_usa using SQLAlchemy ORM.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
    Connects to the MySQL database, creates a session,
    retrieves the State with id = 2, updates its name, and commits.
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.id == 2).first()

    if state:
        state.name = "New Mexico"
        session.commit()

    session.close()
