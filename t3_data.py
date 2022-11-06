from google.cloud.sql.connector import Connector
import sqlalchemy
import pymysql
connector = Connector()
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from google.cloud.sql.connector import Connector, IPTypes
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

def getconn():
    with Connector() as connector:
        conn = connector.connect(
            "team14-t3:us-central1:t3", # Cloud SQL Instance Connection Name
            "pg8000",
            user="victoria",
            password="******",
            db="t3_team14",
            ip_type= IPTypes.PUBLIC  # IPTypes.PRIVATE for private IP
        )
        return conn


app = Flask(__name__)

# configure Flask-SQLAlchemy to use Python Connector
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+pg8000://"
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    "creator": getconn
}

db = SQLAlchemy(app)

from sqlalchemy import MetaData
meta = MetaData()
data = Table(
   't3', meta, 
   Column('id', Integer, primary_key = True), 
   Column('grade', String), 
   Column('income', String), 
)
