from api import db, app
from flask import request, jsonify
from api.models import Employee, employee_schema, employees_schema


# Add new employee
@app.route("/new", methods=["POST"])
def new_employee():
    employee = Employee(
        request.json["first_name"],
        request.json["last_name"],
        request.json["department"],
        request.json["has_kids"],
    )

    db.session.add(employee)
    db.session.commit()

    return employee_schema.jsonify(employee)


# fetch all the employees
@app.route("/all")
def fetch_employees():
    employees = Employee.query.all()
    res = employees_schema.dump(employees)

    return jsonify(res)


# fetch single employee by ID
@app.route("/employee<id>")
def get_by_id(id):
    employee = Employee.query.get(id)
    return employee_schema.jsonify(employee)


# modify employee data
@app.route("/modify<id>", methods=["PUT"])
def modify_by_id(id):
    employee = Employee.query.get(id)
    employee.first_name, employee.last_name, employee.department, employee.has_kids = (
        request.json["first_name"],
        request.json["last_name"],
        request.json["department"],
        request.json["has_kids"],
    )
    db.session.commit()
    return employee_schema.jsonify(employee)


# delete employee by ID
@app.route("/delete<id>", methods=["DELETE"])
def delete_by_id(id):
    employee = Employee.query.get(id)
    db.session.delete(employee)

    all_employees = Employee.query.all()
    res = employees_schema.dump(all_employees)
    return employees_schema.jsonify(res)
