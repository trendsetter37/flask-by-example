from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
import config

from app import app, db
app.config.from_object(config.DevelopmentConfig) # setting manually fix this down the road

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
