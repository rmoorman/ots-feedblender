from flask.ext.script import Manager
from flask_frozen import Freezer
from app import app

manager = Manager(app)

@manager.command
def freeze():
    freezer = Freezer(app)
    freezer.freeze()

if __name__ == "__main__":
    manager.run()
