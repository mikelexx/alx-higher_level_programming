#!/usr/bin/python3
"""
script that creates the State “California” with \
the City “San Francisco” from the database hbtn_0e_100_usa: \
(100-relationship_states_cities.py)
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
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = State(name="California")
    session.add(state)
    session.commit()
    city = City(name="San Fransisco", state=state, state_id=state)
    session.add(city)
    session.commit()
    session.close()
