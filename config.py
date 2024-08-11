import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    DEBUG = True
    db_name = os.environ.get('DB_NAME') or 'myapp.db'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEVELOPMENT_DATABASE_URI') or \
        f'sqlite:///{basedir}/Volume/{db_name}'