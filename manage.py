import unittest
from app import create_app,db
from flask_script import Manager,Server
from app.models import User

# Creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server)


@manager.command
def test():
    """Run the unit tests."""
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()