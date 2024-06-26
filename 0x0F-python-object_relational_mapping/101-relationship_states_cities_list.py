#!/usr/bin/python3
"""
lists all State objects, and corresponding City objects,\
contained in the database hbtn_0e_101_usa
"""
if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_state import State
    from relationship_city import Base, City
    import sys
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id)
    for state in states:
        print("{}: {:s}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {:s}".format(city.id, city.name))
