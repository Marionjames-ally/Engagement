from app import create_app,db
from flask_script import Manager,Server,Shell
from app.models import User,Admin,Parent,Comment
from flask_migrate import Migrate,MigrateCommand

app = create_app('productio')

migrate = Migrate(app,db)
manager = Manager(app)

manager.add_command('server',Server)
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User, Admin=Admin,Parent=Parent,Comment=Comment )

if __name__ == '__main__':
    manager.run()