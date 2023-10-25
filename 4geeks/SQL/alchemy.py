from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"
db = SQLAlchemy(app)
print (db)

class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = False)

    def serialize(self):
        return {
            "id" : self.id,
            "name" : self.name
        }