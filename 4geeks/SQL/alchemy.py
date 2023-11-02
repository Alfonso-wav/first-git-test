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
    

# Supongamos que ya tenemos los ingredientes base añadidos con anterioridad

# Ahora insertamos un nuevo ingrediente en la pizza, la carne
ingredient = Ingredient()
ingredient.name = "meat"
ingredient.id = 4
db.session.add(ingredient)

# Ahora hacemos COMMIT y lo guardamos en la base de datos, de tal forma que fijamos el ingrediente en la Pizza
db.session.commit()

# Reemplazamos el cuarto ingrediente, que antes era la carne, por los champiñones
ingredient = Ingredient.query.get(4)
ingredient.name = mushrooms

# Guardamos un "checkpoint"
checkpoint_a = db.session.begin_nested()

# Añadimos pepperoni en la pizza
ingredient = Ingredient()
ingredient.name = "pepperoni"
db.session.add(ingredient)

# Un último "checkpoint" antes de añadir el beicon
checkpoint_b = db.session.begin_nested()

# Insertamos el beicon
ingredient = Ingredient()
ingredient.name = "bacon"
db.session.add(ingredient)