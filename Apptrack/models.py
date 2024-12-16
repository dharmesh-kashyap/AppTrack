from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Database model for storing app details
class AppDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    app_name = db.Column(db.String(100), nullable=False)
    version = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=False)
