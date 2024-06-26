#!/usr/bin/python3
"""
script that lists all City objects from the database hbtn_0e_101_usa
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
    cities = session.query(City).order_by(City.id)
    for city in cities:
        print("{}: {:s} -> {:s}".format(city.id,
                                        city.name,
                                        city.state.name))
