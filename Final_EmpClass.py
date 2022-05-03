import json

class Employee:
    def __init__(self, Emp_ID="", fName='', lName='', Department='', jTitle=''):
        self.Emp_ID = Emp_ID
        self.fName = fName
        self.lName = lName
        self.Department = Department
        self.jTitle = jTitle

    @property
    def E_ID(self):
        return self.Emp_ID

    @property
    def E_fName(self):
        return self.fName

    @property
    def E_lName(self):
        return self.lName

    @property
    def E_Department(self):
        return self.Department

    @property
    def E_jTitle(self):
        return self.jTitle

    @E_ID.setter
    def E_ID(self, Emp_ID):
        self.Emp_ID = Emp_ID

    @E_fName.setter
    def E_fName(self, fName):
        self.fName = fName

    @E_lName.setter
    def E_lName(self, lName):
        self.lName = lName

    @E_Department.setter
    def E_Department(self, Department):
        self.Department = Department

    @E_jTitle.setter
    def E_jTitle(self, jTitle):
        self.jTitle = jTitle







    #Below are methods that I wanted to implement but could not get to work
    #as I wanted to.

    # def save_to_json(self, filename):
    #     Emp_Dict = {
    #         self.Emp_ID:[
    #             {'Employee ID': self.Emp_ID,
    #              'First Name': self.E_fName,
    #              'Last Name': self.E_lName,
    #              'Deparment': self.E_Department,
    #              'Job Title': self.E_jTitle}]
    #     }
    #
    #     with open(filename, 'w') as f:
    #         f.write(json.dumps(Emp_Dict, indent=2))


    # def load_from_json(self, filename):
    #     with open(filename, 'r') as f:
    #         data = json.loads(f.read())
    #
    #     self.Emp_ID = data['Employee ID']
    #     self.E_fName = data['First Name']
    #     self.E_lName = data['Last Name']
    #     self.E_Department = data['Department']
    #     self.E_jTitle = data['Job Title']
    #
    #
    # def view_data(self, filename):
    #     with open(filename, 'r') as f:
    #         data = json.load(f)
    #         for entry in data:
    #             return 'Employee ID: {}'.format(self.Emp_ID)
    #             return 'Name: {} {}'.format(self.E_fName, self.E_lName)
    #             return 'Department: {}, Title: {}'.format(self.E_Department, self.E_jTitle)
    #             return "\n\n"
