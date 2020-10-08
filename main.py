from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)
students = [
    {"studentId": 1, "name": "Mike", "department": "Software School", "major": "Software Engineering"},
    {"studentId": 2, "name": "Mike2", "department": "Software School", "major": "Software Engineering"},
    {"studentId": 3, "name": "Mike3", "department": "Software School", "major": "Software Engineering"},
    {"studentId": 4, "name": "Mike4", "department": "Software School", "major": "Software Engineering"},
    {"studentId": 5, "name": "Mike5", "department": "Software School", "major": "Software Engineering"}
]


@app.route('/')
def hello_world():
    return 'Hello, Student System!'


@app.route('/api/v1/student', methods=["POST"])
def insert_student():
    data = request.get_json()
    if not data or data.get("studentId") is None or data.get("name") is None \
            or data.get("department") is None or data.get("major") is None:
        return "Invalid Param"
    if data.get("studentId") in [student["studentId"] for student in students]:
        return "Student Exist"
    students.append(
        {
            "studentId": data.get("studentId"),
            "name": data.get("name"),
            "department": data.get("department"),
            "major": data.get("major")
        }
    )
    return "Success"


@app.route("/api/v1/student", methods=["GET"])
def query_student():
    return jsonify(students)


@app.route("/api/v1/student", methods=["PUT"])
def update_student():
    data = request.get_json()
    if not data or data.get("studentId") is None:
        return "Invalid Param"
    if data.get("studentId") not in [student["studentId"] for student in students]:
        return "Student Not Exist"
    student_idx = 0
    for i in range(len(students)):
        if students[i]["studentId"] == data.get("studentId"):
            student_idx = i
    if data.get("name") is not None:
        students[student_idx]["name"] = data.get("name")
    if data.get("department") is not None:
        students[student_idx]["department"] = data.get("department")
    if data.get("major") is not None:
        students[student_idx]["major"] = data.get("major")
    return "Success"


@app.route("/api/v1/student", methods=["DELETE"])
def delete_student():
    data = request.get_json()
    if not data or data.get("studentId") is None:
        return "Invalid Param"
    if data.get("studentId") not in [student["studentId"] for student in students]:
        return "Student Not Exist"
    student_idx = 0
    for i in range(len(students)):
        if students[i]["studentId"] == data.get("studentId"):
            student_idx = i
    students.remove(students[student_idx])
    return "Success"
