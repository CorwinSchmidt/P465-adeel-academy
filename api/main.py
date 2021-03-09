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
    Incomplete:
        ********* TEACHER *********
            String: userID (firebase)
            String: name
            String: email
            String[]: courseID
            boolean: connected (on/offline)
                    
        ******** ADMIN ********
            String: userID (firebase)
            String: name
            String: email
                    

        ****** MODULE *****
            String: moduleID
            String: name
            String: description
            Document[]: documents
            Course_Assignment[]: assignments
                    
        ****** DOCUMENT ******
            String: documentID
            Enum type: (file, text, URL, media)
                    
        ********* CHAT *********
            Message[]: messages
            String[]: userIDs (chat partners)
                    
        ******* MESSAGE *******
            String: userID (sender)
            String: content
            int: timestamp
                    
        ***** ANNOUNCEMENT *****
            String: name
            String: description
            String: courseID
                    
        ** COURSE_ASSIGNMENT **
            String: name
            String: description
            int: dueTime
            String: courseID
                    
        ** STUDENT_ASSIGNMENT **
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
            
         ******** StudentCourses ********
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


# main function that gets flask runnning
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
