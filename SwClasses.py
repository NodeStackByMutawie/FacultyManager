import random
import string

class facultyMember:
    def __init__(self, id, name, department, coursesTaught, fieldsOfSpeciality, professionalInterests):
        self._id = id
        self._name = name
        self._department = department
        self._coursesTaught = coursesTaught
        self._fieldsOfSpeciality = fieldsOfSpeciality
        self._professionalInterests = professionalInterests

    def getId(self):
        return self._id

    def getName(self):
        return self._name

    def getDepartment(self):
        return self._department

    def getCoursesTaught(self):
        return self._coursesTaught

    def getFieldsOfSpeciality(self):
        return self._fieldsOfSpeciality

    def getProfessionalInterests(self):
        return self._professionalInterests

    @staticmethod
    def generateId():
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

    def setId(self):
        self._id = self.generateId()

    def setName(self, name):
        self._name = name

    def setDepartment(self, department):
        self._department = department

    def setCoursesTaught(self, coursesTaught):
        self._coursesTaught = coursesTaught

    def setFieldsOfSpeciality(self, fieldsOfSpeciality):
        self._fieldsOfSpeciality = fieldsOfSpeciality

    def setProfessionalInterests(self, professionalInterests):
        self._professionalInterests = professionalInterests

class searchCirteria:
    def __init__(self, name, department, course, speciality, interests):
        self._name = name
        self._department = department
        self._course = course
        self._speciality = speciality
        self._interests = interests

    def setName(self, name):
        self._name = name

    def setDepartment(self, department):
        self._department = department

    def setCourse(self, course):
        self._course = course

    def setSpeciality(self, speciality):
        self._speciality = speciality

    def setInterests(self, interests):
        self._interests = interests

    def getName(self):
        return self._name

    def getDepartment(self):
        return self._department

    def getCourse(self):
        return self._course

    def getSpeciality(self):
        return self._speciality

    def getInterests(self):
        return self._interests

class facultyDirectory:
    def __init__(self):
        self._facultyMembers = []

    def addFacultyMember(self, facultyMember):
        self._facultyMembers.append(facultyMember)

    def deleteFacultyMember(self, id):
        for member in self._facultyMembers:
            if member.getId() == id:
                self._facultyMembers.remove(member)
                return True
        return False

    def searchFacultyMember(self, criteria):
        results = []
        for member in self._facultyMembers:
            if (criteria.getName() in member.getName() and
                criteria.getDepartment() in member.getDepartment() and
                criteria.getCourse() in member.getCoursesTaught() and
                criteria.getSpeciality() in member.getFieldsOfSpeciality() and
                criteria.getInterests() in member.getProfessionalInterests()):
                results.append(member)
        return results

    def getAllFacultyMembers(self):
        return self._facultyMembers

    def getFacultyMemberById(self, id):
        for member in self._facultyMembers:
            if member.getId() == id:
                return member
        return None

    def updateFacultyMember(self, id, name, department, coursesTaught, fieldsOfSpeciality, professionalInterests):
        for member in self._facultyMembers:
            if member.getId() == id:
                member.setName(name)
                member.setDepartment(department)
                member.setCoursesTaught(coursesTaught)
                member.setFieldsOfSpeciality(fieldsOfSpeciality)
                member.setProfessionalInterests(professionalInterests)
                return True
        return False

class admin:
    def __init__(self, username, password):
        self._username = username
        self._password = password
        self._directory = facultyDirectory()

    def getUsername(self):
        return self._username

    def getPassword(self):
        return self._password

    def setUsername(self, username):
        self._username = username

    def setPassword(self, password):
        self._password = password

    def addFacultyMember(self, facultyMember):
        self._directory.addFacultyMember(facultyMember)

    def deleteFacultyMember(self, id):
        return self._directory.deleteFacultyMember(id)

    def viewFacultyMember(self, id):
        return self._directory.getFacultyMemberById(id)

    def editFacultyMember(self, id, name, department, coursesTaught, fieldsOfSpeciality, professionalInterests):
        return self._directory.updateFacultyMember(id, name, department, coursesTaught, fieldsOfSpeciality, professionalInterests)

class user:
    def __init__(self):
        self._directory = facultyDirectory()

    def listFacultyMembers(self):
        return self._directory.getAllFacultyMembers()

    def searchFacultyMembers(self, criteria):
        return self._directory.searchFacultyMember(criteria)