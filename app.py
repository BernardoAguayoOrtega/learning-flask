from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
import os


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'planets.db')

db = SQLAlchemy(app)


@app.cli.command('db_create')
def db_create():
    db.create_all()
    print('Database created!')


@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print('Datavase dropped!!!')


@app.cli.command('db_seed')
def db_seed():
    mercury = Planet(planet_name='Mercury',
                     planet_type='Class D',
                     home_star='Sol',
                     mass=3.258e23,
                     radius=1516,
                     distance=35.98e6)

    venus = Planet(planet_name='Venus',
                   planet_type='Class k',
                   home_star='Sol',
                   mass=3.258e23,
                   radius=1516,
                   distance=35.98e6)

    db.session.add(mercury)
    db.session.add(venus)

    tes_user = User(first_name='Bernardo',
                    last_name='Aguayo',
                    email='test@test.com',
                    password='test')

    db.session.add(tes_user)

    db.session.commit()
    print('Database seeded!')


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/super_simple')
def super_simple():
    return jsonify(message='Hello from the planetary API. Some planet, New some planet')


@app.route('/not_found')
def not_found():
    return jsonify(message='That resource was not found'), 404


@app.route('/parameters')
def parameters():
    name = request.args.get('name')
    age = int(request.args.get('age'))

    if age < 18:
        return jsonify(message='Sorry ' + name + ", you are not old enough"), 401
    else:
        return jsonify(message='Welcome ' + name + ', you are old enough')


@app.route('/url_variables/<string:name>/<int:age>')
def url_variables(name: str, age: int):
    if age < 18:
        return jsonify(message='Sorry ' + name + ", you are not old enough"), 401
    else:
        return jsonify(message='Welcome ' + name + ', you are old enough')

# database models


class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)


class Planet(db.Model):
    __tablename__ = 'planets'
    planet_id = Column(Integer, primary_key=True)
    planet_name = Column(String)
    planet_type = Column(String)
    home_star = Column(String, unique=True)
    mass = Column(Float)
    radius = Column(Float)
    distance = Column(Float)


if __name__ == '__main__':
    app.run()
