#!/usr/bin/python3
''' lists all states from database hbtn_0e_0_usa using SQLAlchemy'''
if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).filter(
            State.name.contains('a')).all():
        session.delete(state)
    session.commit()
    session.close()
