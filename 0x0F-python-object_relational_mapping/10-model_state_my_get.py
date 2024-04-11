#!/usr/bin/python3
"""
script that prints the State object with the name passed \
        as argument from the database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    state_name_to_search = sys.argv[4]
    Session = sessionmaker(bind=engine)
    session = Session()
    matched_states = session.query(State)\
        .filter(State.name == state_name_to_search)
    if len(matched_states.all()) > 0:
        for state in matched_states:
            print(state.id)
    else:
        print("Not found")
