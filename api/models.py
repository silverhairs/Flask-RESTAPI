from api import db, marshmallow

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(40))
    last_name = db.Column(db.String(40), unique=True) # Made it Unique just as an example
    department = db.Column(db.String(50))
    has_kids = db.Column(db.Boolean)

    def __init__(self, first_name, last_name, department, has_kids):
        self.first_name, self.last_name = first_name, last_name
        self.department, self.has_kids = department, has_kids

    def __repr__(self):
        return f'{self.first_name} {self.last_name}'


class EmployeeSchema(marshmallow.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'department', 'has_kids')

employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)