from flask import Flask, request, jsonify
from models import db, AppDetails

app = Flask(__name__)

# SQLite database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Initialize the database when the app starts
with app.app_context():
    db.create_all()

# Endpoint 1: POST /add-app - Add app details
@app.route('/add-app', methods=['POST'])
def add_app():
    data = request.json
    new_app = AppDetails(
        app_name=data['app_name'],
        version=data['version'],
        description=data['description']
    )
    db.session.add(new_app)
    db.session.commit()
    return jsonify({"message": "App added successfully!", "id": new_app.id}), 201

# Endpoint 2: GET /get-app/<id> - Retrieve app details
@app.route('/get-app/<int:id>', methods=['GET'])
def get_app(id):
    app_details = AppDetails.query.get(id)
    if app_details:
        return jsonify({
            "id": app_details.id,
            "app_name": app_details.app_name,
            "version": app_details.version,
            "description": app_details.description
        })
    return jsonify({"message": "App not found"}), 404

# Endpoint 3: DELETE /delete-app/<id> - Delete app by ID
@app.route('/delete-app/<int:id>', methods=['DELETE'])
def delete_app(id):
    app_details = AppDetails.query.get(id)
    if app_details:
        db.session.delete(app_details)
        db.session.commit()
        return jsonify({"message": "App deleted successfully!"})
    return jsonify({"message": "App not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
