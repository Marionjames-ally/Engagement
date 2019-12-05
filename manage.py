<<<<<<< HEAD
from app import create_app
from flask_script import Manager,Server

#creating app instance
app = create_app('development')

manager=Manager(app)
manager.add_command('server',Server(use_debugger=True))
=======
from app import create_app,db
from flask_script import Manager,Server,Shell
from app.models import User
from flask_migrate import Migrate,MigrateCommand

app = create_app('development')

migrate = Migrate(app,db)
manager = Manager(app)

manager.add_command('server',Server)
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User )
>>>>>>> gakori

if __name__ == '__main__':
    manager.run()