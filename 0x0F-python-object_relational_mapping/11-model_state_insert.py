#!/usr/bin/python3
"""
script that adds the State object “Louisiana” to the database \
        hbtn_0e_6_usa
"""
if __name__ == "__main__":
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    los = State(name="Louisiana")
    session.add(los)
    session.commit()
    print(session.query(State).filter(State.name == "Louisiana").first().id)
