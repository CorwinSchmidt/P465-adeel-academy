from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)

# https://rahmanfadhil.com/flask-rest-api/

# HAYDEN: read this and these notes and follow a long with the structure of the code, an example is used using post
# each route, the pages that our api is going to call have to ahve 3 things
    # 1. a model 
    # 2. a schema used by Marshmallow, bassically provides a layer of communiation between flask and our db see here(https://flask-marshmallow.readthedocs.io/en/latest/)
    # 3. create a schema object for getting multiple objects 3a, and single objects 3b
    # 4. the actual endpoint that is called when a user goes to a certain route eg /users
    # 5. register the endpoint

# TODO object items
'''
    Completed: 
        ********* TEACHER *********HAYDEN
            String: userID (firebase)
            String: name
            String: email
            String[]: courseID
            boolean: connected (on/offline)
                    
        ******** ADMIN ********HAYDEN
            String: userID (firebase)
            String: name
            String: email
                    

        ****** MODULE *****HAYDEN
            String: moduleID
            String: name
            String: description
            Document[]: documents
            Course_Assignment[]: assignments
                    
        ****** DOCUMENT ******HAYDEN
            String: documentID
            Enum type: (file, text, URL, media)
                    
        ********* CHAT *********HAYDEN
            Message[]: messages
            String[]: userIDs (chat partners)
                    
        ******* MESSAGE *******HAYDEN
            String: userID (sender)
            String: content
            int: timestamp
                    
        ***** ANNOUNCEMENT *****HAYDEN
            String: name
            String: description
            String: courseID
                    
        ** COURSE_ASSIGNMENT **HAYDEN
            String: name
            String: description
            int: dueTime
            String: courseID
                    
        ** STUDENT_ASSIGNMENT **HAYDEN
            String: name
            String: description
            int: dueTime
            boolean: turnedIn
            float: grade
    Complete:
        ********* STUDENT ********* Dean
            String: userID (firebase)
            String: name
            String: email
            String[]: courseID
            boolean: connected (on/offline)

        ******** COURSE ******** Dean
            String: courseID 
            String: name
            String: description
            String[]: userIDs (teachers)
            String[]: userIDs (students)
            Module[]: modules
            
         ******** StudentCourses ********HAYDEN
            Int: unique takes id
            Int: StudentId (ref student id)
            Int: CourseId (ref teacher id)
'''

# STUDENT
# 1. example model for a user            
class Student(db.Model):
    __tablename__ = 'student'
    studentId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))  
    # courses = db.relationship("StudentCourses") # creates a list that references StudentCourses, another db.Model, but it needs to be created first
    connected = db.Column(db.Boolean)

    def __repr__(self):
        return "studentId: {}, Name: {}, Email: {}, Courses: {}, Connected: {}".format(self.id, self.name, self.email, self.courses, self.connected)

# 2. a schema used by Marshmallow
class StudentSchema(ma.Schema):
    class Meta:
        fields = ("studentId", "name", "email", "courses", "connected")

# 3a multiple users schema
students_schema = StudentSchema(many=True)

# 3b single user schema
student_schema = StudentSchema()


# 4. the actual endpoint that is called when a user goes to a certain route eg /users
# for returning a list of items
class StudentListResource(Resource):
    def get(self):
        posts = Student.query.all()
        return students_schema.dump(posts)

    def post(self):

        connection = False

        if request.json['connected']=='True' or request.json['connected'] == 'true':
            connection = True

        new_student = Student(
            studentId=request.json['studentId'],
            name=request.json['name'],
            email=request.json['email'],
            connected=connection, 
        )
        db.session.add(new_student)
        db.session.commit()
        return student_schema.dump(new_student)

# 4. the actual endpoint that is called when a user goes to a certain route eg /users
# for a single data item given an ID
class StudentResource(Resource):
    def get(self, student_id):
        student = Student.query.get_or_404(student_id)
        return student_schema.dump(student)

    def patch(self, student_id):
        student = Student.query.get_or_404(student_id)
        if 'studentId' in request.json:
            student.studentId = request.json['studentId']
        if 'name' in request.json:
            student.name = request.json['name']
        if 'email' in request.json:
            student.email = request.json['email']
        if 'connected' in request.json and (request.json['connected']=='True' or request.json['connected'] == 'true'):
            student.connected = True
        db.session.commit()
        return student_schema.dump(student)

    def delete(self, student_id):
        student = Student.query.get_or_404(student_id)
        db.session.delete(student)
        db.session.commit()
        return '', 204


# 5. register the endpoints so flask knows where to go when called
api.add_resource(StudentListResource, '/students') # example call to get all students "curl http://localhost:5000/students"
api.add_resource(StudentResource, '/students/<int:student_id>')
# example to insert a student
'''
curl http://localhost:5000/students \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"studentId":"1", "name":"dean", "email":"test@dean.com", "connected":"True"}'
'''

# Course
# The Post is just an example fromt the website using a blog post
# 1. example model for a user            
class Course(db.Model):
    __tablename__ = 'course'
    courseId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(500)) 
    # students = db.relationship("Student") # creates a list that references Student, another db.Model
    # teachers = db.relationship("Teachers") # creates a list that references Student, another db.Model (not created yet)
    # modules = db.relationship("Modules") # creates a list that references Student, another db.Model (not created yet)

    def __repr__(self):
        return "courseId: {}, Name: {}, description: {}, students: {}, teachers: {}, modules: {}".format(self.courseId, self.name, self.description, self.students, self.teachers, self.modules)

# 2. a schema used by Marshmallow
class CourseSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "description", "students", "teachers", "modules")

# 3a multiple users schema
courses_schema = CourseSchema(many=True)

# 3b single user schema
course_schema = CourseSchema()

# 4. the actual endpoint that is called when a user goes to a certain route eg /users
    # for returning a list of items
class CourseListResource(Resource):
    def get(self):
        courses = Course.query.all()
        return courses_schema.dump(courses)

    def post(self):
        new_course = Course(
            courseId=request.json['courseId'],
            name=request.json['name'],
            description=request.json['description'],
        )
        db.session.add(new_course)
        db.session.commit()
        return course_schema.dump(new_course)

# 4. the actual endpoint that is called when a user goes to a certain route eg /users
    # for a single data item given an ID
class CourseResource(Resource):
    def get(self, course_id):
        course = Course.query.get_or_404(course_id)
        return course_schema.dump(course)

    def patch(self, course_id):
        course = Course.query.get_or_404(course_id)
        if 'courseId' in request.json:
            course.courseId = request.json['courseId']
        if 'name' in request.json:
            course.name = request.json['name']
        if 'description' in request.json:
            course.description = request.json['description']
        db.session.commit()
        return course_schema.dump(course)

    def delete(self, course_id):
        course = Course.query.get_or_404(course_id)
        db.session.delete(course)
        db.session.commit()
        return '', 204


# 5. register the endpoints so flask knows where to go when called
api.add_resource(CourseListResource, '/courses') # example call to get all courses "curl http://localhost:5000/courses"
api.add_resource(CourseResource, '/courses/<int:course_id>') # eg curl http://localhost:5000/courses/1
# example to insert a course
'''
curl http://localhost:5000/courses \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"courseId":"1", "name":"cs OOP", "description":"GOD I LOVE OOP"}'
'''

# Int: unique takes id
# Int: StudentId (ref student id)
# Int: CourseId (ref teacher id)



# StudentCourses
# The Post is just an example fromt the website using a blog post
# 1. example model for a user            
class StudentCourses(db.Model):
    __tablename__ = 'studentcourse'
    studentCourseId = db.Column(db.Integer, primary_key=True)
    courseId = db.Column(db.Integer, db.ForeignKey('course.courseId'))
    studentId= db.relationship(db.Integer, db.ForeignKey('student.studentId'))

    def __repr__(self):
        return "studentCourseId: {}, courseId: {}, studentId: {}".format(self.studentCourseId, self.courseId, self.studentId)

# 2. a schema used by Marshmallow
class StudentCoursesSchema(ma.Schema):
    class Meta:
        fields = ("studentCourseId", "courseId", "studentId")

# 3a multiple users schema
studentCourses_schema = StudentCoursesSchema(many=True)
# 3b single user schema
studentCourse_schema = StudentCoursesSchema()

# 4. the actual endpoint that is called when a user goes to a certain route eg /users
    # for returning a list of items
class StudentCourseListResource(Resource):
    def get(self):
        student_courses = StudentCourses.query.all()
        return studentCourses_schema.dump(student_courses)

    def post(self):
        new_student_course = StudentCourses(
            courseId=request.json['courseId'],
            studentId=request.json['studentId'],
        )
        db.session.add(new_student_course)
        db.session.commit()
        return studentCourse_schema.dump(new_student_course)

# 4. the actual endpoint that is called when a user goes to a certain route eg /users
    # for a single data item given an ID
class StudentCourseResource(Resource):
    def get(self, studentCourseId):
        student_course = StudentCourses.query.get_or_404(studentCourseId)
        return studentCourse_schema.dump(student_course)

    def patch(self, studentCourseId):
        course = Course.query.get_or_404(studentCourseId)
        if 'studentCourseId' in request.json:
            course.studentCourseId = request.json['studentCourseId']
        if 'studentId' in request.json:
            course.studentId = request.json['studentId']
        if 'courseId' in request.json:
            course.courseId = request.json['courseId']
        db.session.commit()
        return studentCourse_schema.dump(course)

    def delete(self, studentCourseId):
        student_course = Course.query.get_or_404(studentCourseId)
        db.session.delete(student_course)
        db.session.commit()
        return '', 204


# 5. register the endpoints so flask knows where to go when called
api.add_resource(StudentCourseListResource, '/studentcourses') # example call to get all courses "curl http://localhost:5000/studentcourses"
api.add_resource(StudentCourseResource, '/studentcourses/<int:studentCourseId>') # eg curl http://localhost:5000/studentcourses/1
# example to insert a course
'''
curl http://localhost:5000/studentcourses \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"studentCourseId":"1", "studentId":"1", "courseId":"2"}'
'''

# TEACHER
class Teacher(db.Model):

    __tablename__ = 'teacher'

    teacherID = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    # courses = db.relationship("StudentCourses")
    connected = db.column(db.Boolean)


    def __repr__(self):

        return "Teacher ID : {}, Name: {}, Email: {}, Courses: {}, Connected: {}".format(self.teacherID, self.name, self.email, self.courses, self.connected)


# Marshmellow Schema
class TeacherSchema(ma.Schema):

    class Meta:

        fields = ("teacherID", "name", "email", "courses", "connected")

# Schema for Multiple Teachers
teachers_schema = TeacherSchema(many = True)


# Schema for Individual Teachers
teacher_schema = TeacherSchema()


"""
Creating the API's Endpoint, Resource to Return the List of Items
"""
class TeacherListResource(Resource):

    def get(self):

        posts = Teacher.query.all()
        return teacher_schema.dump(posts)

    def post(self):

        connection = False

        if request.json['connected'] == "True" or request.json['connected'] == 'true':

            connection = True
        
        newTeacher = Teacher(
            teacherID = request.json['teacherID'],
            name = request.json['name'],
            email = request.json['email'],
            connected = connection
        )

        db.session.add(newTeacher)
        db.session.commit()
        return teacher_schema.dump(newTeacher)


class TeacherResource(Resource):

    def get(self, teacherID):

        teacher = Teacher.query.get_or_404(teacherID)
        return teacher_schema.dump(teacher)

    def patch(self, teacherID):

        teacher = Teacher.query.get_or_404(teacherID)

        if 'teacherID' in request.json:
            teacher.teacherID = request.json['teacherID']

        if 'name' in request.json:
            teacher.name = request.json['name']

        if 'email' in request.json:
            teacher.email = request.json['email']

        if 'connected' in request.json and (request.json['connected'] == 'True' or request.json['connected'] == 'true'):
            teacher.connected = True

        db.session.commit()
        return teacher_schema.dump(teacher)

    
    def delete(self, teacherID):

        teacher = teacherID.query.get_or_404(teacherID)
        db.session.delete(teacher)
        db.session.commit()
        return '', 204
    
# Registering the Endpoints 
api.add_resource(TeacherListResource, '/teachers')
api.add_resource(TeacherResource, '/teachers/<int:teacherID>')


# ADMIN

class Admin(db.Model):

    __tablename__ = 'admin'

    adminID = db.Column(db.Integer, primary_keys = True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))

    def __repr__(self):

        return "AdminID: {}, Name: {}, Email: {}".format(self.adminID, self.name, self.email)


# Marshmellow Schema
class AdminSchema(ma.Schema):

    class Meta:
        fields = ("adminID", "name", "email")


# Schema for Multiple Admin
admins_schema = AdminSchema(many = True)

# Schema for Single Admin
admin_schema = AdminSchema()


# The Endpoints for the List of Admins
class AdminListResource(Resource):

    def get(self):

        posts = Admin.query.all()
        return admins_schema.dump(posts)

    
    def post(self):

        newAdmin = Admin(
            adminID = request.json['adminID'],
            name = request.json['name'],
            email = request.json['email']
        )

        db.session.add(newAdmin)
        db.session.commit()
        return admin_schema.dump(newAdmin)


# Endpoint for Each Admin, given their Admin ID
class AdminResource(Resource):

    def get(self, adminID):

        admin = Admin.query.get_or_404(adminID)
        return admin_schema.dump(admin)

    def patch(self, adminID):

        admin = Admin.query.get_or_404(adminID)

        if "adminID" in request.json['adminID']:
            admin.adminID = request.json['adminID']

        if 'name' in request.json['name']:
            admin.name = request.json['name']

        if 'email' in request.json['email']:

            admin.email = request.json['email']

        db.session.commit()
        return admin_schema.dump(admin)


    def delete(self, adminID):

        admin = Admin.query.get_or_404(adminID)
        db.session.delete(admin)
        db.session.commit()
        return '', 204


# Register the Endpoints 
api.add_resource(AdminListResource, '/admin')
api.add_resource(AdminResource, '/admin/<int:adminID>')


# MODULE 

class Module(db.Model):

    __tablename__ = 'module'
    
    moduleID = db.Column(db.Integer, primary_key = 50)
    name = db.Column(db.String(50))
    description = db.Column(db.String(50))
    # documents = db.relationship("Document")
    # assignments = db.relationship("CourseAssignment")

    def __repr__(self):

        return "Module ID: {}, Name: {}, Description: {}".format(self.moduleID, self.name, self.description)


# Marshmallow Schema
class ModuleSchema(ma.Schema):

    class Meta:

        fields = ("moduleID", "name", "description")


# Schema for Multiple Modules
modules_schema = ModuleSchema(many = True)


# Schema for Single Module
module_schema = ModuleSchema()


# Endpoint for a List of Modules
class ModuleListResource(Resource):

    def get(self):

        posts = Module.query.all()
        return modules_schema.dump(posts)

    def post(self):

        newModule = Module(
            moduleID = request.json['moduleID'],
            name = request.json['name'],
            description = request.json['description']
        )

        db.session.add(newModule)
        db.session.commit()
        return module_schema.dump(newModule)


# Endpoint for the Single Module, given the Module ID
class ModuleResource(Resource):

    def get(self, moduleID):

        module = Module.query.get_or_404(moduleID)
        return module_schema.dump(module)


    def patch(self, moduleID):

        module = Module.query.get_or_404(moduleID)

        if 'moduleID' in request.json['moduleID']:

            module.moduleID = request.json['moduleID']

        if 'name' in request.json['name']:

            module.name = request.json['name']

        if 'description' in request.json['description']:

            module.description = request.json['description']

        db.session.commit()
        return module_schema.dump(module)


    def delete(self, moduleID):

        module = Module.query.get_or_404(moduleID)
        db.session.delete(module)
        db.session.commit()
        return '', 204



# Register the Endpoints
api.add_resource(ModuleListResource, '/module')
api.add_resource(ModuleResource, '/module/<int:moduleID>')


# DOCUMENT

class Document(db.Model):

    __tablename__ = 'document'

    documentID = db.Column(db.Integer, primary_key = True)
    # Enum Type --> Not Sure How to Proceed on this Yet


    def __repr__(self):

        return "Document ID: {}".format(self.documentID)


# Marshmallow Schema
class DocumentSchema(ma.Schema):

    class Meta:

        fields = ("documentID")


# Schema for Multiple Documents
documents_schema = DocumentSchema(many = True)


# Schema for Single Documents
document_schema = DocumentSchema()


# Endpoint for a List of Documents
class DocumentListResource(Resource):

    def get(self):

        posts = Document.query.all()
        return documents_schema.dump(posts)

    
    def post(self):

        newDocument = Document(
            documentID = request.json['documentID']
        )

        db.session.add(newDocument)
        db.session.commit()
        return document_schema.dump(newDocument)



# Endpoint for a Single Document

class DocumentResource(Resource):

    def get(self, documentID):

        document = Document.query.get_or_404(documentID)
        return document_schema.dump(document)

    
    def patch(self, documentID):

        document = Document.query.get_or_404(documentID)

        if 'documentID' in request.json['documentID']:

            document.documentID = request.json['documentID']

        db.session.commit()
        return document_schema.dump(document)


    def delete(self, documentID):

        document = Document.query.get_or_404(documentID)
        db.session.delete(document)
        db.session.commit()
        return '', 204


# Register the Endpoints
api.add_resource(DocumentListResource, '/documents')
api.add_resource(DocumentResource, '/documents/<int:documentID>')


# CHAT
class Chat(db.Model):

    __tablename__ = 'chat'

    # messages = db.relationship("Message")
    # userIDs = db.relationship("Student")


    
    # MESSAGE

class Message(db.Model):

    __tablename__ = 'message'

    messageID = db.Column(db.Integer, primary_key = True)
    # userID = db.relationship("Student")
    message = db.Column(db.String(50))
    timestamp = db.Column(db.Integer)


    def __repr__(self):

        return "Message ID: {}, Message: {}, Timestamp: {}".format(self.messageID, self.message, self.timestamp)


# Marshmallow Schema
class MessageSchema(ma.Schema):

    class Meta:

        fields = ("messageID", "message", "timestamp")

# Schema for Multiple Messages
messages_schema = MessageSchema(many = True)

# Schema for Single Messages
message_schema = MessageSchema()


# Endpoint for Returning a List of Messages
class MessagesListResource(Resource):

    def get(self):

        posts = Message.query.all()
        return messages_schema.dump(posts)


    def post(self):

        newMessage = Message(
            messageID = request.json['messageID'],
            message = request.json['message'],
            timestamp = request.json['timestamp']
        )
        db.session.add(newMessage)
        db.session.commit()
        return message_schema.dump(newMessage)


# Endpoint for a Single Message
class MessageResource(Resource):

    def get(self, messageID):

        message = Message.query.get_or_404(messageID)
        return message_schema.dump(message)
        

    def patch(self, messageID):

        message = Message.query.get_or_404(messageID)

        if "messageID" in request.json['messageID']:

            message.messageID = request.json['messageID']

        if 'message' in request.json['message']:

            message.message = request.json['message']

        if 'timestamp' in request.json['timestamp']:

            message.timestamp = request.json['timestamp']

        db.session.commit()
        return message_schema.dump(message)


    def delete(self, messageID):

        message = Message.query.get_or_404(messageID)
        db.session.delete(message)
        db.session.commit()
        return message_schema.dump(message)
        


# Register Endpoints
api.add_resource(MessagesListResource, '/messages')
api.add_resources(MessageResource, '.messages/<int:messageID>')



# ANNOUNCEMENT

class Announcement(db.Model):

    __tablename__ = 'announcement'

    courseID = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(50))


    def __repr__(self):

        return "Course ID: {}, Name: {}, Description: {}".format(self.courseID, self.name, self.description)


# Marshmallow Schema
class AnnouncementSchema(ma.Schema):

    class Meta:

        fields = ("courseID", "name", "description")


# Schema for Multiple Announcements
announcements_schema = AnnouncementSchema(many = True)

# Schema for Single Announcement
announcement_schema = AnnouncementSchema()

# Endpoint for a List of Announcements
class AnnouncementListResource(Resource):

    def get(self):

        announcement = Announcement.query.all()
        return announcement_schema.dump(announcement)


    def post(self):

        newAnnouncement = Announcement(
            courseID = request.json['courseID'],
            name = request.json['name'],
            description = request.json['description']
        )
        db.session.add(newAnnouncement)
        db.session.commit()
        return announcement_schema.dump(newAnnouncement)


# Endpoint for a Single Announcement
class AnnouncementResource(Resource):

    def get(self, announcementID):

        announcement = Announcement.query.get_or_404(announcementID)
        return announcement_schema.dump(announcement)


    def patch(self, announcementID):

        announcement = Announcement.query.get_or_404(announcementID)

        if 'courseID' in request.json['courseID']:

            announcement.courseID = request.json['courseID']

        if 'name' in request.json['name']:

            announcement.name = request.json['name']

        if 'description' in request.json['description']:

            announcement.description = request.json['description']

        db.session.commit()
        return announcement_schema.dump(announcement)


    def delete(self, announcementID):

        announcement = Announcement.query.get_or_404(announcementID)
        db.session.delete(announcement)
        db.session.commit()
        return '', 204


# Register Endpoints
api.add_resource(AnnouncementListResource, '/announcements')
api.add_resource(AnnouncementResource, '/announcements/<int:announcementID>')



# Course Assignment

class CourseAssignment(db.Model):

    __tablename__ = 'courseAssignment'

    courseID = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(50))
    dueDate = db.Column(db.Integer)


    def __repr__(self):

        return "Course ID: {}, Name: {}, Description: {}, Due Date: {}".format(self.courseID, self.name, self.description, self.dueDate)


# Marshmallow Schema
class CourseAssignmentSchema(ma.Schema):

    class Meta:

        fields = ("courseID", "name", "description", "dueDate")


# Schema for Multiple Course Assignments
courseAssignmentsSchema = CourseAssignmentSchema(many = True)

# Schema for Single Course Assignment
course_Assignment_Schema = CourseAssignmentSchema()

# Endpoint for a List of Course Assignments
class CourseAssignmentsListResource(Resource):

    def get(self):

        posts = CourseAssignment.query.all()
        return course_Assignment_Schema.dump(posts)


    def post(self):

        newCourseAssignment = CourseAssignment(
            courseID = request.json['courseID'],
            name = request.json['name'],
            description = request.json['description'],
            dueDate = request.json['dueDate']
        )

        db.session.add(newCourseAssignment)
        db.session.commit()
        return course_Assignment_Schema.dump(newCourseAssignment)


# Endpoint for a Single Course Assignment
class CourseAssignmentResource(Resource):

    def get(self, courseID):

        courseAssignment = CourseAssignment.get_or_404(courseID)
        return course_Assignment_Schema.dump(courseAssignment)


    def patch(self, courseID):

        courseAssignment = CourseAssignment.get_or_404(courseID)

        if 'courseID' in request.json['courseID']:

            courseAssignment.courseID = request.json['courseID']

        if 'name' in request.json['name']:

            courseAssignment.name = request.json['name']

        if 'description' in request.json['description']:

            courseAssignment.description = request.json['description']

        if 'dueDate' in request.json['dueDate']:

            courseAssignment.dueDate = request.json['dueDate']

        db.session.commit()
        return course_Assignment_Schema.dump(courseAssignment)


# Register Endpoints
api.add_resource(CourseAssignmentsListResource, '/courseAssignments')
api.add_resource(CourseAssignmentResource, '/courseAssignments/<int:courseID>')
    

# STUDENT ASSIGNMENT

class StudentAssignment(db.Model):

    __tablename__ = 'studentAssignment'

    assignmentID = db.Column(db.Integer, primary_key = 50)
    name = db.Column(db.String(50))
    description = db.Column(db.String(50))
    dueDate = db.Column(db.Integer)
    grade = db.Column(db.Float)
    turnedIn = db.Column(db.Boolean)

    def __repr__(self):

        return "Assignment ID: {}, Name: {}, Description: {}, Due Date: {}, Grade: {}, Turned in: {}".format(self.assignmentID, self.name, self.description, self.dueDate, self.grade, self.turnedIn)

    

# Marshmallow Schema
class StudentAssignmentSchema(ma.Schema):

    class Meta:

        fields = ("assignmentID", "name", "description", "dueDate", "grade", "turnedIn")

# Schema for Multiple Student Assignments
students_schema = StudentAssignmentSchema(many = True)

# Schema for Single Student Assignments
student_schema = StudentAssignmentSchema()


# Endpoint for the List of Student Assignments
class StudentAssignmentListResource(Resource):

    def get(self):

        student_assignment = StudentAssignment.query.all()
        return student_schema.dump(student_assignment)


    def post(self):

        newStudentAssignment = StudentAssignment(

            assignmentID = request.json['assignmentID'],
            name = request.json['name'],
            description = request.json['description'],
            dueDate = request.json['dueDate'],
            grade = request.json['grade'],
            turnedIn = request.json['turnedIn']
        )

        db.session.add(newStudentAssignment)
        db.session.commit()
        return student_schema.dump(newStudentAssignment)


# Endpoint for a Single Student Assignment
class StudentAssignmentResource(Resource):

    def get(self, assignmentID):

        student_ass = StudentAssignment.query.get_or_404(assignmentID)
        return student_schema.dump(student_ass)

    def patch(self, assignmentID):

        student_ass = StudentAssignment.query.get_or_404(assignmentID)

        if 'assignmentID' in request.json['assignmentID']:

            student_ass.assignmentID = request.json['assignmentID']

        if 'name' in request.json['name']:

            student_ass.name = request.json['name']

        if 'description' in request.json['description']:

            student_ass.description = request.json['description']

        if 'dueDate' in request.json['dueDate']:

            student_ass.dueDate = request.json['dueDate']

        if 'grade' in request.json['grade']:

            student_ass.grade = request.json['grade']

        if 'turnedIn' in request.json['turnedIn']:

            student_ass.turnedIn = request.json['turnedIn']

        db.session.commit()
        return student_schema.dump(student_ass)


    def delete(self, assignmentID):

        student_ass = StudentAssignment.query_or_404(assignmentID)
        db.session.delete(student_ass)
        db.session.commit()
        return '', 204


# Register Endpoints
api.add_resource(StudentAssignmentListResource, '/studentAssignments')
api.add_resource(StudentAssignmentResource, '/studentAssignments/<int:assignmentID>')
    

# main function that gets flask runnning
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
