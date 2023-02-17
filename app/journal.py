from application import db
from models import Journal, Action


def insert_turn_on():
    db.session.add(Journal(action_id=1))
    db.session.commit()


def insert_turn_off():
    db.session.add(Journal(action_id=2))
    db.session.commit()


def insert_boiled():
    db.session.add(Journal(action_id=3))
    db.session.commit()


def get_data():
    #  SELECT j.timestamp, a.title FROM journal AS j JOIN action AS a ON j.action_id=a.id;
    rows = db.session.query(Journal, Action).filter(Journal.action_id==Action.id).all()
    parsed_rows = []
    for row in rows:
        parsed_rows.append(f"{row[0].timestamp} - {row[1].title}")
    return parsed_rows
