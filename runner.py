import sqlalchemy as sa
import sqlalchemy.orm as so
from app import create_app, db
from app.models import Article

app = create_app()

app.run()
