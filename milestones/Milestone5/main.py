"""
The code below is just representative of the implementation of a Bot. 
However, this code was not meant to be compiled as it. It is the responsability 
of all the students to modifify this code such that it can fit the 
requirements for this assignments.
"""

import discord
import os
from discord.ext import commands
#from database import *
from models import *
#TODO:  add your Discord Token as a value to your secrets on replit using the DISCORD_TOKEN key
TOKEN = os.environ["DISCORD_TOKEN"]

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

user_variables = {}




@bot.command(name="test", description="write your database business requirement for this command here")
async def _test(ctx, arg1):
    #testModel = TestModel(ctx, arg1)
    #response = testModel.response()
    studentModel = StudentFromUsernameModel(ctx, arg1)
    student = studentModel.response()
    response = f'Hi, {student.firstName}. Your student ID is {student.studentID}'
    await ctx.send(response)


# TODO: complete the following tasks:
#       (1) Replace the commands' names with your own commands
#       (2) Write the description of your business requirement in the description parameter
#       (3) Implement your commands' methods.

@bot.command(name="studentlogin", description="This command logs you in as a student if you give it a correct username and password")
async def _studentlogin(ctx, *args):
    response = "This command did not work."
    if ctx.author.id not in user_variables:
        user_variables[ctx.author.id] = {
          'isLoggedIn': False,
          'username': None,
          'password': None,
          'studentID': None,
          'teacherID': None,
          'adminID': None
      }

    if user_variables[ctx.author.id]["isLoggedIn"]:
        response = "You are already logged in."
    else:    
        studentToLoginModel = StudentLoginModel(ctx, args[0], args[1])
        student = studentToLoginModel.response()
    
        if student.studentID:
            user_variables[ctx.author.id]["studentID"] = student.studentID
            user_variables[ctx.author.id]["isLoggedIn"] = True
            user_variables[ctx.author.id]["username"] = student.username
            response = f'Hi, {student.firstName}. Your student ID is {student.studentID}. You are now logged in.'
        else:
            response = f'Sorry{args[0]}, your username and/or password is incorrect.'

    await ctx.send(response)

@bot.command(name="teacherlogin", description="This command logs you in as a teacher if you give it a correct username and password")
async def _teacherlogin(ctx, *args):
    response = "This command did not work."
    if ctx.author.id not in user_variables:
        user_variables[ctx.author.id] = {
          'isLoggedIn': False,
          'username': None,
          'password': None,
          'studentID': None,
          'teacherID': None,
          'adminID': None
        }

    if user_variables[ctx.author.id]["isLoggedIn"]:
        response = "You are already logged in."
    else:    
        teacherToLoginModel = TeacherLoginModel(ctx, args[0], args[1])
        teacher = teacherToLoginModel.response()

        if teacher.teacherID:
            user_variables[ctx.author.id]["teacherID"] = teacher.teacherID
            user_variables[ctx.author.id]["isLoggedIn"] = True
            user_variables[ctx.author.id]["username"] = teacher.username
            response = f'Hi, {teacher.firstName}. Your teacher ID is {teacher.teacherID}. You are now logged in.'
        else:
            response = f'Sorry{args[0]}, your username and/or password is incorrect.'

    await ctx.send(response)


@bot.command(name="adminlogin", description="This command logs you in as an admin if you give it a correct username and password")
async def _teacherlogin(ctx, *args):
    response = "This command did not work."
    if ctx.author.id not in user_variables:
        user_variables[ctx.author.id] = {
          'isLoggedIn': False,
          'username': None,
          'password': None,
          'studentID': None,
          'teacherID': None,
          'adminID': None
        }

    if user_variables[ctx.author.id]["isLoggedIn"]:
        response = "You are already logged in."
    else:    
        adminToLoginModel = AdminLoginModel(ctx, args[0], args[1])
        admin = adminToLoginModel.response()

        if admin.adminID:
            user_variables[ctx.author.id]["adminID"] = admin.adminID
            user_variables[ctx.author.id]["isLoggedIn"] = True
            user_variables[ctx.author.id]["username"] = admin.username
            response = f'Hi, {admin.username}. Your admin ID is {admin.adminID}. You are now logged in.'
        else:
            response = f'Sorry{args[0]}, your username and/or password is incorrect.'

    await ctx.send(response)




@bot.command(name="logout", description="This command logs you out if you are logged in.")
async def _logout(ctx, *args):
    response = "This command did not work."
    if ctx.author.id not in user_variables:
        response = "You are not logged in."
    elif not user_variables[ctx.author.id]["isLoggedIn"]:
        response = "You are not logged in."
    else: 
        user_variables[ctx.author.id]["isLoggedIn"] = False
        user_variables[ctx.author.id]["username"] = None
        user_variables[ctx.author.id]["password"] = None
        user_variables[ctx.author.id]["studentID"] = None
        user_variables[ctx.author.id]["teacherID"] = None
        user_variables[ctx.author.id]["adminID"] = None
        response = "You are now logged out."
        
    await ctx.send(response)


@bot.command(name="viewreqs", description="A student can use this to view required classes for his major")
async def _viewreqs(ctx, *args):


    response = "This command did not work."

    if ctx.author.id not in user_variables:
        response = "You are not logged in as a student."
    elif not user_variables[ctx.author.id]["studentID"]:
        response = "You are not logged in as a student."
    else:
        viewReqsByMajorToModel = ViewReqsByMajorModel(ctx, user_variables[ctx.author.id]["studentID"])
        viewReqsByMajor = viewReqsByMajorToModel.response()
        response = viewReqsByMajor.responseString
        
      
    await ctx.send(response)


@bot.command(name="viewsubjects", description="This command allows you to view a list of subjects")
async def _viewsubjects(ctx, *args):
  response = "This command did not work."

  if ctx.author.id not in user_variables:
      response = "You are not logged in as a student."
  elif not user_variables[ctx.author.id]["studentID"]:
      response = "You are not logged in as a student."
  else:
      viewSubjectsModeled = ViewSubjectsModel(ctx)
      viewSubjects = viewSubjectsModeled.response()
      response = viewSubjects.responseString


  await ctx.send(response)


@bot.command(name="viewsectionsbysubject", description="This command allows you to view a list of class sections for a given subject")
async def _viewsectionsbysubject(ctx, *args):

  response = "This command did not work."

  if ctx.author.id not in user_variables:
      response = "You are not logged in as a student."
  elif not user_variables[ctx.author.id]["studentID"]:
      response = "You are not logged in as a student."
  else:
      viewClassSectionsBySubjectModeled = ViewClassSectionsBySubjectModel(ctx, args[0])
      viewClassSectionsBySubject = viewClassSectionsBySubjectModeled.response()
      response = viewClassSectionsBySubject.responseString


  await ctx.send(response)


@bot.command(name="viewsectionsenrolled", description="This command allows a student to view class sections he is enrolled in")
async def _viewsectionsenrolled(ctx, *args):
    response = "This command did not work."
  
    if ctx.author.id not in user_variables:
        response = "You are not logged in as a student."
    elif not user_variables[ctx.author.id]["studentID"]:
        response = "You are not logged in as a student."
    else:
        viewClassSectionsEnrolledModeled = ViewClassSectionsEnrolledModel(ctx, user_variables[ctx.author.id]["studentID"])
        viewClassSectionsEnrolled = viewClassSectionsEnrolledModeled.response()
        response = viewClassSectionsEnrolled.responseString


    await ctx.send(response)


@bot.command(name="addsection", description="This allows a student to enroll in a class section")
async def _addsection(ctx, *args):
    response = "This command did not work."
    
    if ctx.author.id not in user_variables:
        response = "You are not logged in as a student."
    elif not user_variables[ctx.author.id]["studentID"]:
        response = "You are not logged in as a student."
    else:
        AddClassSectionModeled = AddClassSectionModel(ctx, user_variables[ctx.author.id]["studentID"], args[0])
        AddClassSection = AddClassSectionModeled.response()
        response = AddClassSection.responseString
    
    
    await ctx.send(response)

@bot.command(name="dropsection", description="database business requirement #8 here")
async def _dropsection(ctx, *args):
    response = "This command did not work."
  
    if ctx.author.id not in user_variables:
        response = "You are not logged in as a student."
    elif not user_variables[ctx.author.id]["studentID"]:
        response = "You are not logged in as a student."
    else:
        DropClassSectionModeled = DropClassSectionModel(ctx, user_variables[ctx.author.id]["studentID"], args[0])
        DropClassSection = DropClassSectionModeled.response()
        response = DropClassSection.responseString
  
  
    await ctx.send(response)


@bot.command(name="viewsectionstudent", description="This allows a student to view a particular section he's enrolled in")
async def _viewsectionstudent(ctx, *args):
    response = "This command did not work."
  
    if ctx.author.id not in user_variables:
        response = "You are not logged in as a student."
    elif not user_variables[ctx.author.id]["studentID"]:
        response = "You are not logged in as a student."
    else:
        ViewSectionStudentModeled = ViewSectionStudentModel(ctx, user_variables[ctx.author.id]["studentID"], args[0])
        ViewSectionStudent = ViewSectionStudentModeled.response()
        response = ViewSectionStudent.responseString
  
  
    await ctx.send(response)


@bot.command(name="viewmodulestudent", description="allows a student to view a module for a class section he is enrolled in")
async def _viewmodulestudent(ctx, *args):
    response = "This command did not work."
  
    if ctx.author.id not in user_variables:
        response = "You are not logged in as a student."
    elif not user_variables[ctx.author.id]["studentID"]:
        response = "You are not logged in as a student."
    else:
        ViewModuleStudentModeled = ViewModuleStudentModel(ctx, user_variables[ctx.author.id]["studentID"], args[0])
        ViewModuleStudent = ViewModuleStudentModeled.response()
        response = ViewModuleStudent.responseString
  
  
    await ctx.send(response)
  

@bot.command(name="viewdocstudent", description="This allows a student to view a single document for a class section he is enrolled in")
async def _viewdocstudent(ctx, *args):
    response = "This command did not work."
  
    if ctx.author.id not in user_variables:
        response = "You are not logged in as a student."
    elif not user_variables[ctx.author.id]["studentID"]:
        response = "You are not logged in as a student."
    else:
        ViewDocStudentModeled = ViewDocStudentModel(ctx, user_variables[ctx.author.id]["studentID"], args[0])
        ViewDocStudent = ViewDocStudentModeled.response()
        response = ViewDocStudent.responseString
  
  
    await ctx.send(response)


@bot.command(name="viewassmtstudent", description="database business requirement #12 here")
async def _viewassmtstudent(ctx, *args):
    response = "This command did not work."
  
    if ctx.author.id not in user_variables:
        response = "You are not logged in as a student."
    elif not user_variables[ctx.author.id]["studentID"]:
        response = "You are not logged in as a student."
    else:
        ViewAssmtStudentModeled = ViewAssmtStudentModel(ctx, user_variables[ctx.author.id]["studentID"], args[0])
        ViewAssmtStudent = ViewAssmtStudentModeled.response()
        response = ViewAssmtStudent.responseString
  
  
    await ctx.send(response)


@bot.command(name="submitassmt", description="Submit an assignment for a grade.")
async def _submitassmt(ctx, *args):
    response = "This command did not work."

    if ctx.author.id not in user_variables:
        response = "You are not logged in as a student."
    elif not user_variables[ctx.author.id]["studentID"]:
        response = "You are not logged in as a student."
    else:
        VerifyStudentAssmtModeled = VerifyStudentAssmtModel(ctx, user_variables[ctx.author.id]["studentID"], args[0])
        VerifyStudentAssmt = VerifyStudentAssmtModeled.response()
        if VerifyStudentAssmt.responseBool:
            SubmitAssmtModeled = SubmitAssmtModel(ctx, user_variables[ctx.author.id]["studentID"], args[0], args[1])
            SubmitAssmt = SubmitAssmtModeled.response()
            response = SubmitAssmt.responseString
        else:
            response = "You are not enrolled in this class section."
    await ctx.send(response)



@bot.command(name="viewsectionstaught", description="This command allows a teacher to view the sections they teach")
async def _command14(ctx, *args):
    response = "This command did not work."
    
    if ctx.author.id not in user_variables:
        response = "You are not logged in as a teacher."
    elif not user_variables[ctx.author.id]["teacherID"]:
        response = "You are not logged in as a teacher."
    else:
        ViewSectionsTaughtModeled = ViewSectionsTaughtModel(ctx, user_variables[ctx.author.id]["teacherID"])
        ViewSectionsTaught = ViewSectionsTaughtModeled.response()
        response = ViewSectionsTaught.responseString
    await ctx.send(response)
    


@bot.command(name="viewsectionteacher", description="Allows a teacher to  view an individual class and its modules")
async def _viewsectionteacher(ctx, *args):
    response = "This command did not work."
    
    if ctx.author.id not in user_variables:
        response = "You are not logged in as a teacher."
    elif not user_variables[ctx.author.id]["teacherID"]:
        response = "You are not logged in as a teacher."
    else:
        ViewSectionTeacherModeled = ViewSectionTeacherModel(ctx, user_variables[ctx.author.id]["teacherID"], args[0])
        ViewSectionTeacher = ViewSectionTeacherModeled.response()
        response = ViewSectionTeacher.responseString
    await ctx.send(response)

@bot.command(name="createmodule", description="Allows a teacher to create a new module in a class section he teaches")
async def _createmodule(ctx, *args):
    response = "This command did not work."

    if ctx.author.id not in user_variables:
        response = "You are not logged in as a teacher."
    elif not user_variables[ctx.author.id]["teacherID"]:
        response = "You are not logged in as a teacher."
    else:
        argString = " ".join(args)
      
        idNameDesc = argString.split('/')
        if len(idNameDesc) < 3:
            response = f"Please provide your response in the format [class section id]/[name]/[description]. Your entry: {args}"
        else:
            VerifyTeacherSectionModeled = VerifyTeacherSectionModel(ctx, user_variables[ctx.author.id]["teacherID"], idNameDesc[0])
            VerifyTeacherSection = VerifyTeacherSectionModeled.response()
            if VerifyTeacherSection.responseBool:
                CreateModuleModeled = CreateModuleModel(ctx, idNameDesc[0], idNameDesc[1], idNameDesc[2])
            
                CreateModule = CreateModuleModeled.response()
                response = CreateModule.responseString
            else:
                response = "You are not authorized to create a module in this class section."
    await ctx.send(response)

@bot.command(name="viewmoduleteacher", description="Allows a teacher to  view an individual module and its documents, assignments and quizzes")
async def _viewmoduleteacher(ctx, *args):
    response = "This command did not work."

    if ctx.author.id not in user_variables:
        response = "You are not logged in as a teacher."
    elif not user_variables[ctx.author.id]["teacherID"]:
        response = "You are not logged in as a teacher."
    else:
        ViewModuleTeacherModeled = ViewModuleTeacherModel(ctx, user_variables[ctx.author.id]["teacherID"], args[0])
        ViewModuleTeacher = ViewModuleTeacherModeled.response()
        response = ViewModuleTeacher.responseString
    await ctx.send(response)

@bot.command(name="createdoc", description="Allows a teacher to create a new document in a module in a class section he teaches")
async def _createdoc(ctx, *args):
    response = "This command did not work."

    if ctx.author.id not in user_variables:
        response = "You are not logged in as a teacher."
    elif not user_variables[ctx.author.id]["teacherID"]:
        response = "You are not logged in as a teacher."
    else:
        argString = " ".join(args)

        idNameDescLink = argString.split('/')
        if len(idNameDescLink) < 4:
            response = f"Please provide your response in the format [module id]/[name]/[description]/[link]. Your entry: {args}"
        else:
            VerifyTeacherModuleModeled = VerifyTeacherModuleModel(ctx, user_variables[ctx.author.id]["teacherID"], idNameDescLink[0])
            VerifyTeacherModule = VerifyTeacherModuleModeled.response()
            if VerifyTeacherModule.responseBool:
                CreateDocTeacherModeled = CreateDocTeacherModel(ctx, idNameDescLink[0], idNameDescLink[1], idNameDescLink[2], idNameDescLink[3])

                CreateDocTeacher = CreateDocTeacherModeled.response()
                response = CreateDocTeacher.responseString
            else:
                response = "You are not authorized to create a document in this module."
    await ctx.send(response)

@bot.command(name="createassmt", description="Allows a teacher to create a new assignment in a module in a class section he teaches")
async def _createassmt(ctx, *args):
    response = "This command did not work."

    if ctx.author.id not in user_variables:
        response = "You are not logged in as a teacher."
    elif not user_variables[ctx.author.id]["teacherID"]:
        response = "You are not logged in as a teacher."
    else:
        argString = " ".join(args)

        idNameDescLinkTopscore = argString.split('/')
        if len(idNameDescLinkTopscore) < 5:
            response = f"Please provide your response in the format [module id]/[name]/[description]/[link]/[Top score]. Your entry: {args}"
        else:
            VerifyTeacherModuleModeled = VerifyTeacherModuleModel(ctx, user_variables[ctx.author.id]["teacherID"], idNameDescLinkTopscore[0])
            VerifyTeacherModule = VerifyTeacherModuleModeled.response()
            if VerifyTeacherModule.responseBool:
                CreateAssmtTeacherModeled = CreateAssmtTeacherModel(ctx, idNameDescLinkTopscore[0], idNameDescLinkTopscore[1], idNameDescLinkTopscore[2], idNameDescLinkTopscore[3], idNameDescLinkTopscore[4])
                CreateAssmtTeacher = CreateAssmtTeacherModeled.response()
                response = CreateAssmtTeacher.responseString
            else:
                response = "You are not authorized to create an assignment in this module."
    await ctx.send(response)

@bot.command(name="viewsubmittals", description="Allows a teacher to view submitted assignments in a class section he teaches")
async def _viewsubmittals(ctx, *args):
    response = "This command did not work."

    if ctx.author.id not in user_variables:
        response = "You are not logged in as a teacher."
    elif not user_variables[ctx.author.id]["teacherID"]:
        response = "You are not logged in as a teacher."
    else:
        VerifyTeacherAssmtModeled = VerifyTeacherAssmtModel(ctx, user_variables[ctx.author.id]["teacherID"], args[0])
        VerifyTeacherAssmt = VerifyTeacherAssmtModeled.response()
        if VerifyTeacherAssmt.responseBool:
            ViewSubmittedAssmtsModeled = ViewSubmittedAssmtsModel(ctx, args[0])
            ViewSubmittedAssmts = ViewSubmittedAssmtsModeled.response()
            response = ViewSubmittedAssmts.responseString
        else:
            response = "You are not authorized to view submittals of this assignment."
    await ctx.send(response)

@bot.command(name="gradesubmittal", description="Allows a teacher to grade a submitted assignment in a class section he teaches")
async def _gradesubmittal(ctx, *args):
    response = "This command did not work."

    if ctx.author.id not in user_variables:
        response = "You are not logged in as a teacher."
    elif not user_variables[ctx.author.id]["teacherID"]:
        response = "You are not logged in as a teacher."
    else:
        VerifyTeacherSubmittalModeled = VerifyTeacherSubmittalModel(ctx, user_variables[ctx.author.id]["teacherID"], args[0])
        VerifyTeacherSubmittal = VerifyTeacherSubmittalModeled.response()
        if VerifyTeacherSubmittal.responseBool:
            GradeSubmittalModeled = GradeSubmittalModel(ctx, args[0], args[1])
            GradeSubmittal = GradeSubmittalModeled.response()
            response = GradeSubmittal.responseString
        else:
            response = "You are not authorized to grade submittals of this assignment."
    await ctx.send(response)

@bot.command(name="viewteachers", description="Allows an admin to view a list of teachers")
async def _viewteachers(ctx, *args):
    response = "This command did not work."
    
    if ctx.author.id not in user_variables:
        response = "You are not logged in as an admin."
    elif not user_variables[ctx.author.id]["adminID"]:
        response = "You are not logged in as an admin."
    else:
        ViewTeacherModeled = ViewTeacherModel(ctx)
        ViewTeacher = ViewTeacherModeled.response()
        response = ViewTeacher.responseString
    await ctx.send(response)

@bot.command(name="viewsections", description="Allows an admin to view a list of class sections")
async def _viewsections(ctx, *args):
    response = "This command did not work."

    if ctx.author.id not in user_variables:
        response = "You are not logged in as an admin."
    elif not user_variables[ctx.author.id]["adminID"]:
        response = "You are not logged in as an admin."
    else:
        ViewSectionsModeled = ViewSectionsModel(ctx)
        ViewSections = ViewSectionsModeled.response()
        response = ViewSections.responseString
    await ctx.send(response)

@bot.command(name="viewteacherassmts", description="Allows an admin to view a list of teachers assigned to sections")
async def _viewteacherassmts(ctx, *args):
    response = "This command did not work."

    if ctx.author.id not in user_variables:
        response = "You are not logged in as an admin."
    elif not user_variables[ctx.author.id]["adminID"]:
        response = "You are not logged in as an admin."
    else:
        ViewTeachersSectionsModeled = ViewTeachersSectionsModel(ctx)
        ViewTeachersSections = ViewTeachersSectionsModeled.response()
        response = ViewTeachersSections.responseString
    await ctx.send(response)


@bot.command(name="addteachersection", description="Allows an admin to assign a teacher to a class section")
async def _addteachersection(ctx, *args):
    response = "This command did not work."

    if ctx.author.id not in user_variables:
        response = "You are not logged in as an admin."
    elif not user_variables[ctx.author.id]["adminID"]:
        response = "You are not logged in as an admin."
    else:
        VerifyTeacherSectionModeled = VerifyTeacherSectionModel(ctx, args[0], args[1])
        VerifyTeacherSection = VerifyTeacherSectionModeled.response()
        if VerifyTeacherSection.responseBool:
            response = "That teacher is already assigned to that section."
          
        else:
            AddTeacherSectionModeled = AddTeacherSectionModel(ctx, args[0], args[1])
            AddTeacherSection = AddTeacherSectionModeled.response()
            response = AddTeacherSection.responseString    
          
    await ctx.send(response)


bot.run(TOKEN)