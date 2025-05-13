from flask import Flask, request, jsonify, session, send_from_directory
from flask_cors import CORS
from SwClasses import facultyMember, facultyDirectory
import json, os

app = Flask(__name__)
CORS(app)
app.secret_key = 'super-secret-key'

DATA_FILE = 'faculty_data.json'
directory = facultyDirectory()

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
            for item in data:
                member = facultyMember(
                    item['id'],
                    item['name'],
                    item['department'],
                    item['coursesTaught'],
                    item['fieldsOfSpeciality'],
                    item['professionalInterests']
                )
                directory.addFacultyMember(member)

def save_data():
    all_members = directory.getAllFacultyMembers()
    with open(DATA_FILE, 'w') as f:
        json.dump([{
            "id": m.getId(),
            "name": m.getName(),
            "department": m.getDepartment(),
            "coursesTaught": m.getCoursesTaught(),
            "fieldsOfSpeciality": m.getFieldsOfSpeciality(),
            "professionalInterests": m.getProfessionalInterests()
        } for m in all_members], f, indent=4)

@app.route("/faculty", methods=["GET"])
def get_faculty():
    members = directory.getAllFacultyMembers()
    return jsonify([{
        "id": m.getId(),
        "name": m.getName(),
        "department": m.getDepartment(),
        "coursesTaught": m.getCoursesTaught(),
        "fieldsOfSpeciality": m.getFieldsOfSpeciality(),
        "professionalInterests": m.getProfessionalInterests()
    } for m in members])

@app.route("/faculty", methods=["POST"])
def add_faculty():
    data = request.json
    member = facultyMember(
        data["id"],
        data["name"],
        data["department"],
        data["coursesTaught"],
        data["fieldsOfSpeciality"],
        data["professionalInterests"]
    )
    directory.addFacultyMember(member)
    save_data()
    return jsonify({"message": "Member added successfully"})

@app.route("/faculty/<id>", methods=["DELETE"])
def delete_faculty(id):
    success = directory.removeFacultyMember(id)
    save_data()
    if success:
        return jsonify({"message": "Deleted successfully"})
    return jsonify({"message": "Member not found"}), 404

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    if data["username"] == "admin" and data["password"] == "admin123":
        session["admin"] = True
        return jsonify({"message": "Login successful"})
    return jsonify({"message": "Invalid credentials"}), 401

@app.route("/logout", methods=["POST"])
def logout():
    session.pop("admin", None)
    return jsonify({"message": "Logged out"})

@app.route("/")
def index():
    return send_from_directory("static", "login.html")

if __name__ == "__main__":
    load_data()
    app.run(debug=True)