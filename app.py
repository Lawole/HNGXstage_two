from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, create_engine

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db = SQLAlchemy(app)

# db.init_app(app)


class User(db.Model):
    # __tablename__ = "Persons"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)


with app.app_context():
    db.create_all()


@app.route("/api", methods=['POST'])
def create_user():
    data = request.get_json('name')
    name = data.get("name")
    new_user = User(name=name)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully!'})


@app.route('/api', methods=['GET'])
def get_users():
    """this returns the id passed in as params """
    # user = session.query(User).filter_by(id=user_id).first()
    # if user:
    #     user_data = {
    #         "id": user.id,
    #         "name": user.name
    #     }
    #     return jsonify(user_data)
    # else:
    #     return jsonify("User does not exist")

    """this returns all the data in the database"""

    users = User.query.all()
    user_data = []
    for user in users:
        user_data.append({
            "id": user.id,
            "name": user.name
        })

    return jsonify(user_data)


@app.route('/api/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    # user = session.query(User).filter_by(id=user_id).first()
    if user:
        user.name = request.json.get("name")

        db.session.commit()
    else:
        return jsonify("User not found")
    # user = User.query.filter_by(id=user_id)
    # user.name = user
    # db.session.commit()

    db.session.commit()
    return jsonify({'message': 'User updated successfully!'})


@app.route('/api/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully!'})


if __name__ == '__main__':
    app.run(debug=True)

