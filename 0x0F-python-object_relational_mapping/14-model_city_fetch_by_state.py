#!/usr/bin/python3
"""
THis script prints all City objects from the database \
        hbtn_0e_14_usa
        Results must be display as they are in the \
        example below (<state name>: (<city id>) <city name>)
"""
if __name__ == "__main__":
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State, City)\
        .join(City, City.state_id == State.id)\
        .order_by(City.id).all()
    for result in results:
        state = result[0]
        city = result[1]
        print("{:s}: ({}) {}".format(state.name, city.id, city.name))
