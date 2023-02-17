from application import db, models


def insert_initial_data():
    actions = (
        "Turned On",
        "Turned Off",
        "Boiled",
    )

    db.drop_all()
    db.create_all()
    db.session.commit()

    db.session.bulk_save_objects([
        models.Action(title=action)
        for action in actions
    ])
    db.session.commit()
