"""
In this file you must implement all your database models.
If you need to use the methods from your database.py call them
statically. For instance:
       # opens a new connection to your database
       connection = Database.connect()
       # closes the previous connection to avoid memory leaks
       connection.close()
"""
from database import *

class TestModel:
    """
    This is an object model example. Note that
    this model doesn't implement a DB connection.
    """

    def __init__(self, ctx):
        self.ctx = ctx
        self.author = ctx.message.author.name

    def response(self):
        return f'Hi, {self.author}. I am alive'


class StudentFromUsernameModel:

    def __init__(self, ctx, arg):
        myDBInstance = Database()
        if myDBInstance.connect():
            myQuery = Database.select(Query.GET_STUDENT_BY_USERNAME, (arg))
            student = myQuery[0]
            self.firstName = student['first_name']
            self.studentID = student['student_id']
    
    def response(self):
        return self


class StudentLoginModel:

    def __init__(self, ctx, username, password):
        myDBInstance = Database()
        if myDBInstance.connect():
            myQuery = Database.select(Query.LOGIN_STUDENT, (username, password))

            if myQuery:
                student = myQuery[0]
                self.firstName = student['first_name']
                self.studentID = student['student_id']
                self.username = student['username']  
            else:
                self.firstName = None
                self.studentID = None
                self.username = None    
    
    def response(self):
        return self

class TeacherLoginModel:

    def __init__(self, ctx, username, password):
        myDBInstance = Database()
        if myDBInstance.connect():
            myQuery = Database.select(Query.LOGIN_TEACHER, (username, password))
    
            if myQuery:
                teacher = myQuery[0]
                self.firstName = teacher['first_name']
                self.teacherID = teacher['teacher_id']
                self.username = teacher['username']  
            else:
                self.firstName = None
                self.teacherID = None
                self.username = None    
    
    def response(self):
        return self

class AdminLoginModel:

    def __init__(self, ctx, username, password):
        myDBInstance = Database()
        if myDBInstance.connect():
            myQuery = Database.select(Query.LOGIN_ADMIN, (username, password))
    
            if myQuery:
                admin = myQuery[0]
                self.adminID = admin['admin_id']
                self.username = admin['username']  
            else:
                self.adminID = None
                self.username = None    
    
    def response(self):
        return self
    

class ViewReqsByMajorModel:
    def __init__(self, ctx, studentID):
        responseString = ""    
        myDBInstance = Database()
        if myDBInstance.connect():
            myQuery = Database.select(Query.VIEW_REQS_BY_MAJOR, (studentID))
            responseString = f"Your major is {myQuery[0]['majorName']}. You are required to take the following classes:\n"
            for row in myQuery:
                responseString += f"{row['className']}\n"
          
        self.responseString = responseString
          
    def response(self):
        return self

class ViewSubjectsModel:
    def __init__(self, ctx):
        responseString = ""    
        myDBInstance = Database()
        if myDBInstance.connect():
            myQuery = Database.select(Query.VIEW_SUBJECTS)
            responseString = "Subjects: \n"
            for row in myQuery:
                responseString += f"ID: {row['subject_id']} - Code: {row['name']} - Name: {row['description']}\n"
    
        self.responseString = responseString
  
    def response(self):
      return self


class ViewClassSectionsBySubjectModel:
    def __init__(self, ctx, subjectCode):
        responseString = ""    
        myDBInstance = Database()
        if myDBInstance.connect():
            myQuery = Database.select(Query.VIEW_SECTIONS_BY_SUBJECT, (subjectCode))
            responseString = f"Class Sections available for  {myQuery[0]['subjectCode']} - {myQuery[0]['subjectName']}:\n\n"
            for row in myQuery:
                responseString += f"Section ID: {row['classSectionID']} - Course: {row['subjectCode']} {row['classNumber']} - {row['className']} - Section: {row['classSectionName']} - {row['classSectionDays']} - {row['classSectionStartTime']} - {row['classSectionEndTime']} - {row['building']} {row['roomNumber']}\n\n"
    
        self.responseString = responseString
    
    def response(self):
        return self




class ViewClassSectionsEnrolledModel:
    def __init__(self, ctx, studentID):
        responseString = "Error retrieving class sections"    
        myDBInstance = Database()
        if myDBInstance.connect():
            myQuery = Database.select(Query.VIEW_SECTIONS_ENROLLED, (studentID))
            if myQuery and myQuery[0]:
                responseString = f"Class Sections enrolled in by {myQuery[0]['firstName']} {myQuery[0]['lastName']}:\n\n"
                for row in myQuery:
                    responseString += f"Section ID: {row['classSectionID']} - Course: {row['subjectCode']} {row['classNumber']} - {row['className']} - Section: {row['classSectionName']} - {row['classSectionDays']} - {row['classSectionStartTime']} - {row['classSectionEndTime']} - {row['building']} {row['roomNumber']}\n\n"
            else:
                responseString = f"Sorry Student {studentID}, the operation failed."
        self.responseString = responseString
    
    def response(self):
        return self


class AddClassSectionModel:
    def __init__(self, ctx, studentID, classSectionID):
      responseString = "Error adding class section"    
      myDBInstance = Database()
      if myDBInstance.connect():
          myQuery = Database.select(Query.SELECT_CLASS_SECTION_STUDENT, (studentID, classSectionID))
          if not myQuery or not myQuery[0]:            
              Database.insert(Query.ADD_CLASS_SECTION, (studentID, classSectionID))
              responseString = f"Class section {classSectionID} added successfully."
          else:
              responseString = f"You are already in Section {classSectionID}."
      self.responseString = responseString

    def response(self):  
        return self  

class DropClassSectionModel:
    def __init__(self, ctx, studentID, classSectionID):
        responseString = "Error dropping class section"    
        myDBInstance = Database()
        if myDBInstance.connect():
            Database.delete(Query.DROP_CLASS_SECTION, (studentID, classSectionID))
            responseString = f"Class section {classSectionID} dropped successfully."
        self.responseString = responseString
    
    def response(self):  
        return self  

class ViewSectionStudentModel:
    def __init__(self, ctx, studentID, classSectionID):
        responseString = "Error viewing class section"    
        myDBInstance = Database()
        if myDBInstance.connect():
            myQuery = Database.select(Query.VIEW_SECTION_STUDENT, (studentID, classSectionID))
            if myQuery and myQuery[0]:
                responseString = f"{myQuery[0]['subjectCode']} {myQuery[0]['classNumber']} {myQuery[0]['className']} - Section {myQuery[0]['classSectionName']}\n\nModules: \n\n"
                for row in myQuery:
                    responseString += f"Module ID: {row['moduleID']} - Name: {row['moduleName']} - Description: {row['moduleDescription']}\n"
              
            else:
                responseString = "Class section not found."
        self.responseString = responseString

    def response(self):  
        return self 

class ViewModuleStudentModel:
    def __init__(self, ctx, studentID, moduleID):
        responseString = "Error viewing module"    
        myDBInstance = Database()
        if myDBInstance.connect():
            myQuery = Database.select(Query.VIEW_MODULE_STUDENT , (studentID, moduleID))
            if myQuery and myQuery[0]:
                responseString = f"{myQuery[0]['subjectCode']} {myQuery[0]['classNumber']} {myQuery[0]['className']} - Section {myQuery[0]['classSectionName']}\n\nModule {myQuery[0]['moduleID']} -  {myQuery[0]['moduleName']}\n\n"
                myQuery2 = Database.select(Query.VIEW_DOC_MODULE_STUDENT, (myQuery[0]['moduleID']))
                if myQuery2 and myQuery2[0]: 
                    responseString += f"Documents: \n\n"
                    for row in myQuery2:
                        responseString += f"Document ID: {row['documentID']} - Name: {row['documentName']} - Description: {row['documentDescription']} - Link: {row['documentLink']}\n"

                myQuery3 = Database.select(Query.VIEW_ASSMT_MODULE_STUDENT, (myQuery[0]['moduleID']))
                if myQuery3 and myQuery3[0]:
                    responseString += f"\nAssignments: \n\n"
                    for row in myQuery3:
                        responseString += f"Assmt ID: {row['assignmentID']} - Name: {row['assignmentName']} - Description: {row[ 'assignmentDescription']} - Link: {row['assignmentLink']}\n"

                myQuery4 = Database.select(Query.VIEW_QUIZ_MODULE_STUDENT, (myQuery[0]['moduleID']))
                if myQuery4 and myQuery4[0]:
                    responseString +="\nQuizzes: \n\n"
                    for row in myQuery4:
                        responseString += f"Quiz ID: {row['quizID']} - Name: {row['quizName']} - Description: {row['quizDescription']}\n"
            else:
                responseString = "Module not found."
        self.responseString = responseString
  
    def response(self):  
        return self 


class ViewDocStudentModel:

    def __init__(self, ctx, studentID, docID):
        responseString = "Error viewing document"    
        myDBInstance = Database()
        if myDBInstance.connect():
            myQuery = Database.select(Query.VIEW_DOC_STUDENT , (studentID, docID))
            if myQuery and myQuery[0]:
                responseString = f"{myQuery[0]['subjectCode']} {myQuery[0]['classNumber']} {myQuery[0]['className']} - Section {myQuery[0]['classSectionName']}\n\nModule {myQuery[0]['moduleID']} - {myQuery[0]['moduleName']}\n\nDocument ID: {myQuery[0]['documentID']} - Name: {myQuery[0]['documentName']} - Description: {myQuery[0]['documentDescription']} - Link: {myQuery[0]['documentLink']}\n"
            else:
                responseString = "Document not found."
        self.responseString = responseString
      
    def response(self):  
        return self 



class ViewAssmtStudentModel:

    def __init__(self, ctx, studentID, assmtID):
        responseString = "Error viewing assignment"    
        myDBInstance = Database()
        if myDBInstance.connect():
            myQuery = Database.select(Query.VIEW_ASSMT_STUDENT , (studentID, assmtID))
            if myQuery and myQuery[0]:
                responseString = f"{myQuery[0]['subjectCode']} {myQuery[0]['classNumber']} {myQuery[0]['className']} - Section {myQuery[0]['classSectionName']}\n\nModule {myQuery[0]['moduleID']} - {myQuery[0]['moduleName']}\n\nAssignment ID: {myQuery[0]['assignmentID']} - Name: {myQuery[0]['assignmentName']} - Description: {myQuery[0]['assignmentDescription']} - Link: {myQuery[0]['assignmentLink']}\n"
            else:
                responseString = "Assignment not found."
        self.responseString = responseString
    
    def response(self):  
        return self 
      
class VerifyStudentAssmtModel:
  def __init__(self, ctx, studentID, assmtID):
      responseBool = False    
      myDBInstance = Database()
      if myDBInstance.connect():
          myQuery = Database.select(Query.VERIFY_STUDENT_ASSMT, (studentID, assmtID))
          if myQuery and myQuery[0]:
              responseBool = True
      self.responseBool = responseBool
  def response(self):  
      return self 

class SubmitAssmtModel:

    def __init__(self, ctx, studentID, assmtID, assmtLink):
        responseString = "Error submitting assignment"    
        myDBInstance = Database()
        if myDBInstance.connect():
            Database.insert(Query.SUBMIT_ASSMT , (studentID, assmtID, assmtLink))
            responseString = f"Assignment {assmtID} submitted successfully."
        self.responseString = responseString

    def response(self):  
        return self 

class ViewSectionsTaughtModel:
    def __init__(self, ctx, teacherID):
        responseString = "Error retrieving class sections taught"    
        myDBInstance = Database()
        if myDBInstance.connect():
            myQuery = Database.select(Query.VIEW_SECTIONS_TAUGHT, (teacherID))
            if myQuery and myQuery[0]:
                responseString = f"Class Sections taught by Professor {myQuery[0]['firstName']} {myQuery[0]['lastName']}:\n\n"
                for row in myQuery:
                    responseString += f"Section ID: {row['classSectionID']} - Course: {row['subjectCode']} {row['classNumber']} - {row['className']} - Section: {row['classSectionName']} - {row['classSectionDays']} - {row['classSectionStartTime']} - {row['classSectionEndTime']} - {row['building']} {row['roomNumber']}\n\n"
            else:
                responseString = f"Sorry Professor {teacherID}, the operation failed."
        self.responseString = responseString
    
    def response(self):
        return self


class ViewSectionTeacherModel:
    def __init__(self, ctx, teacherID, sectionID):
        responseString = "Error retrieving class section"    
        myDBInstance = Database()
        if myDBInstance.connect():
            myQuery = Database.select(Query.VIEW_SECTION_TEACHER, (teacherID, sectionID))
            if myQuery and myQuery[0]:
                responseString = f"{myQuery[0]['subjectCode']} {myQuery[0]['classNumber']} {myQuery[0]['className']} - Section {myQuery[0]['classSectionName']}\n\nModules: \n\n"
                for row in myQuery:
                    responseString += f"Module ID: {row['moduleID']} - Name: {row['moduleName']} - Description: {row['moduleDescription']}\n"
        self.responseString = responseString

    def response(self):
        return self

class CreateModuleModel:
    def __init__(self, ctx, class_section_id, module_name, module_description):
        responseString = "Error creating module"    
        myDBInstance = Database()
        if myDBInstance.connect():
            Database.insert(Query.CREATE_MODULE_TEACHER, (class_section_id, module_name, module_description))
            responseString = f"Module {module_name} created successfully."
        self.responseString = responseString

    def response(self):
        return self


class ViewModuleTeacherModel:
    def __init__(self, ctx, teacherID, moduleID):
        responseString = "Error viewing module"    
        myDBInstance = Database()
        if myDBInstance.connect():
            myQuery = Database.select(Query.VIEW_MODULE_TEACHER , (teacherID, moduleID))
            if myQuery and myQuery[0]:
                responseString = f"{myQuery[0]['subjectCode']} {myQuery[0]['classNumber']} {myQuery[0]['className']} - Section {myQuery[0]['classSectionName']}\n\nModule {myQuery[0]['moduleID']} -  {myQuery[0]['moduleName']}\n\n"
                myQuery2 = Database.select(Query.VIEW_DOC_MODULE_STUDENT, (myQuery[0]['moduleID']))
                responseString += f"Documents: \n\n"
                if myQuery2 and myQuery2[0]: 
                    
                    for row in myQuery2:
                        responseString += f"Document ID: {row['documentID']} - Name: {row['documentName']} - Description: {row['documentDescription']} - Link: {row['documentLink']}\n"
  
                myQuery3 = Database.select(Query.VIEW_ASSMT_MODULE_STUDENT, (myQuery[0]['moduleID']))
                responseString += f"\nAssignments: \n\n"
                if myQuery3 and myQuery3[0]:
                    
                    for row in myQuery3:
                        responseString += f"Assmt ID: {row['assignmentID']} - Name: {row['assignmentName']} - Description: {row[ 'assignmentDescription']} - Link: {row['assignmentLink']}\n"
  
                myQuery4 = Database.select(Query.VIEW_QUIZ_MODULE_STUDENT, (myQuery[0]['moduleID']))
                responseString +="\nQuizzes: \n\n"
                if myQuery4 and myQuery4[0]:   
                    for row in myQuery4:
                        responseString += f"Quiz ID: {row['quizID']} - Name: {row['quizName']} - Description: {row['quizDescription']}\n"
            else:
                responseString = "Module not found."
        self.responseString = responseString
  
    def response(self):  
        return self 

class VerifyTeacherSectionModel:
    def __init__(self, ctx, teacherID, section_id):
        responseBool = False    
        myDBInstance = Database()
        if myDBInstance.connect():
            myQuery = Database.select(Query.VERIFY_TEACHER_SECTION, (teacherID, section_id))
            if myQuery and myQuery[0]:
                responseBool = True
        self.responseBool = responseBool
    def response(self):  
        return self 

class VerifyTeacherModuleModel:
    def __init__(self, ctx, teacherID, moduleID):
        responseBool = False    
        myDBInstance = Database()
        if myDBInstance.connect():
            myQuery = Database.select(Query.VERIFY_TEACHER_MODULE, (teacherID, moduleID))
            if myQuery and myQuery[0]:
                responseBool = True
        self.responseBool = responseBool
    def response(self):  
        return self 

class CreateDocTeacherModel:
    def __init__(self, ctx, moduleID, docName, docDesc, docLink):
        responseString = "Error creating document"    
        myDBInstance = Database()
        if myDBInstance.connect():
            Database.insert(Query.CREATE_DOC_TEACHER, (moduleID, docName, docDesc, docLink))
            responseString = f"Document {docName} created successfully."
        self.responseString = responseString

    def response(self):
        return self


class CreateAssmtTeacherModel:
    def __init__(self, ctx, moduleID, assmtName, assmtDesc, assmtLink, topScore):
        responseString = "Error creating document"    
        myDBInstance = Database()
        if myDBInstance.connect():
            Database.insert(Query.CREATE_ASSMT_TEACHER, (moduleID, assmtName, assmtDesc, assmtLink, topScore))
            responseString = f"Assignment {assmtName} created successfully."
        self.responseString = responseString

    def response(self):
        return self


class VerifyTeacherAssmtModel:
    def __init__(self, ctx, teacherID, assmtID):
        responseBool = False    
        myDBInstance = Database()
        if myDBInstance.connect():
            myQuery = Database.select(Query.VERIFY_TEACHER_ASSMT, (teacherID, assmtID))
            if myQuery and myQuery[0]:
                responseBool = True
        self.responseBool = responseBool
    def response(self):  
        return self 

class ViewSubmittedAssmtsModel:
    def __init__(self, ctx, assmtID):
        responseString = "Error viewing assignments"    
        myDBInstance = Database()
        if myDBInstance.connect():
            myQuery = Database.select(Query.VIEW_SUBMITTED_ASSMTS , (assmtID))
            if myQuery and myQuery[0]:
                responseString = f"Submittals for Assmt {myQuery[0]['assignmentID']} - Name: {myQuery[0]['assignmentName']}, for {myQuery[0]['subjectCode']} {myQuery[0]['classNumber']} Section {myQuery[0]['classSectionName']}\n\n"
                for row in myQuery:
                    responseString += f"Submittal ID: {row['submittalID']} - Student ID: {row['studentID']} - Link: {row['submittalLink']} Score: {row['submittalScore']} out of {row['topScore']}\n\n"
        self.responseString = responseString
  
    def response(self):
        return self


class VerifyTeacherSubmittalModel:
    def __init__(self, ctx, teacherID, submittalID):
        responseBool = False    
        myDBInstance = Database()
        if myDBInstance.connect():
            myQuery = Database.select(Query.VERIFY_TEACHER_SUBMITTAL, (teacherID, submittalID))
            if myQuery and myQuery[0]:
                responseBool = True
        self.responseBool = responseBool
    def response(self):  
        return self 

class GradeSubmittalModel:
    def __init__(self, ctx, submittalID, score):
      responseString = "Error grading submital"    
      myDBInstance = Database()
      if myDBInstance.connect():
          Database.update(Query.GRADE_SUBMITTED_ASSIGNMENT, (score, submittalID))
          responseString = f"Submittal {submittalID} graded successfully."
      self.responseString = responseString

    def response(self):
        return self

class ViewTeacherModel:
  def __init__(self, ctx):
      responseString = "Error retrieving teachers"    
      myDBInstance = Database()
      if myDBInstance.connect():
          myQuery = Database.select(Query.VIEW_TEACHERS)
          if myQuery and myQuery[0]:
              responseString = f"Teachers: \n\n"
              for row in myQuery:
                  responseString += f"Teacher ID: {row['teacherID']} - Name: {row['firstName']} {row['lastName']} - Dept: {row['departmentName']}\n"
      self.responseString = responseString

  def response(self):
      return self

class ViewSectionsModel:
    def __init__(self, ctx):
        responseString = "Error retrieving class sections"    
        myDBInstance = Database()
        if myDBInstance.connect():
            myQuery = Database.select(Query.VIEW_SECTIONS)
            if myQuery and myQuery[0]:
                responseString = f"Class Sections: \n\n"
                for row in myQuery:
                    responseString += f"Section ID: {row['classSectionID']} - Course: {row['subjectCode']} {row['classNumber']} - Section Name: {row['classSectionName']}\n"
        self.responseString = responseString

    def response(self):
        return self


class ViewTeachersSectionsModel:
    def __init__(self, ctx):
        responseString = "Error retrieving class sections"    
        myDBInstance = Database()
        if myDBInstance.connect():
            myQuery = Database.select(Query.VIEW_TEACHERS_SECTIONS)
            if myQuery and myQuery[0]:
                responseString = f"Teacher Section Assignments: \n\n"
                for row in myQuery:
                    responseString += f"Teacher ID: {row['teacherID']} - Name: {row['firstName']} {row['lastName']} - Section ID: {row['classSectionID']} - Course: {row['subjectCode']} {row['classNumber']} - Section Name: {row['classSectionName']}\n"
        self.responseString = responseString

    def response(self):
        return self

class AddTeacherSectionModel:
  def __init__(self, ctx, teacherID, sectionID):
      responseString = "Error adding teacher to section"    
      myDBInstance = Database()
      if myDBInstance.connect():
          Database.insert(Query.ADD_TEACHER_SECTION, (teacherID, sectionID))
          responseString = f"Teacher {teacherID} added to section {sectionID} successfully."
      self.responseString = responseString

  def response(self):
      return self