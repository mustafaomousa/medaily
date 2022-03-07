
from app.models import db, User


def seed_users():
    demouser = User(username='demouser', email='demouser@demo.com', password='password')

    db.session.add(demouser)
    db.session.commit()


def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()