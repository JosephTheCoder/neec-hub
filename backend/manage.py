from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from hub_api import app
from app.database import db
import os

manager = Manager(app)

current_path = os.path.dirname(os.path.realpath(__file__))

migrations_dir = os.path.join(current_path, 'app', 'database', 'migrations')
migrate = Migrate(app, db, directory=migrations_dir)

manager.add_command('db', MigrateCommand)

import click

@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db)

if __name__ == '__main__':
    manager.run()
