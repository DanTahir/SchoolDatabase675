# In this file you must implement your main query methods 
# so they can be used by your database models to interact with your bot.

import os
import pymysql.cursors

#TODO: add the values for these database keys in your secrets on replit
db_host = os.environ["DB_HOST"]
db_username = os.environ["DB_USER"]
db_password = os.environ["DB_PASSWORD"]
db_name = os.environ["DB_NAME"]


class Database:

    # This method was already implemented for you
    def connect(self):
        """
        This method creates a connection with your database
        IMPORTANT: all the environment variables must be set correctly
                   before attempting to run this method. Otherwise, it
                   will throw an error message stating that the attempt
                   to connect to your database failed.
        """
        try:
            conn = pymysql.connect(host=db_host,
                                   port=3306,
                                   user=db_username,
                                   password=db_password,
                                   db=db_name,
                                   charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor)
            print("Bot connected to database {}".format(db_name))
            return conn
        except ConnectionError as err:
            print(f"An error has occurred: {err.args[1]}")
            print("\n")

    #TODO: needs to implement the internal logic of all the main query operations
    def get_response(self, query, values=None, fetch=False, many_entities=False):
        """
        query: the SQL query with wildcards (if applicable) to avoid injection attacks
        values: the values passed in the query
        fetch: If set to True, then the method fetches data from the database (i.e with SELECT)
        many_entities: If set to True, the method can insert multiple entities at a time.
        """
        connection = self.connect()
        cursor = connection.cursor()
        response = None
        if values:
            if many_entities:
                cursor.executemany(query, values)
            else:
                cursor.execute(query, values)
        else:
            cursor.execute(query)
        connection.commit()
        if fetch:
            response = cursor.fetchall()
        connection.close()
        
        return response

    # the following methods were already implemented for you.
    @staticmethod
    def select(query, values=None, fetch=True):
        database = Database()
        return database.get_response(query, values=values, fetch=fetch)

    @staticmethod
    def insert(query, values=None, many_entities=False):
        database = Database()
        return database.get_response(query, values=values, many_entities=many_entities)

    @staticmethod
    def update(query, values=None):
        database = Database()
        return database.get_response(query, values=values)

    @staticmethod
    def delete(query, values=None):
        database = Database()
        return database.get_response(query, values=values)


class Query:
    GET_STUDENT_BY_USERNAME = """
        SELECT * FROM Student WHERE username = %s;"""

    LOGIN_STUDENT = """
        SELECT * FROM Student WHERE username = %s AND password = %s;"""

    LOGIN_TEACHER = """
        SELECT * FROM Teacher WHERE username = %s AND password = %s;"""
  
    LOGIN_ADMIN = """
        SELECT * FROM Admin WHERE username = %s AND password = %s;"""
  
   

    VIEW_REQS_BY_MAJOR = """
        SELECT
            s.student_id,
            m.major_id,
            m.name AS majorName,
            c.class_id,
            c.name AS className         
        FROM Student s 
        JOIN `Student-Major` sm ON s.student_id = sm.student_id
        JOIN Major m ON sm.major_id = m.major_id
        JOIN Major_Requirement mr ON m.major_id = mr.major_id
        JOIN Class c ON mr.class_id = c.class_id
        WHERE s.student_id = %s;"""

    VIEW_SUBJECTS = """
        SELECT * FROM Subject;"""

    VIEW_SECTIONS_BY_SUBJECT = """
        SELECT 
            s.name AS subjectCode,
            s.description AS subjectName,
            c.name AS className,
            c.number AS classNumber,
            cs.class_section_id AS classSectionID,
            cs.name AS classSectionName,
            cs.start_time AS classSectionStartTime,
            cs.end_time AS classSectionEndTime,
            cs.days AS classSectionDays,
            cr.building_name AS building,
            cr.room_number AS roomNumber
        FROM Subject s
        JOIN Class c ON s.subject_id = c.subject_id
        JOIN Class_Section cs ON c.class_id = cs.class_id
        JOIN Classroom cr ON cs.classroom_id = cr.classroom_id
        WHERE s.name = %s;"""

    VIEW_SECTIONS_ENROLLED = """
        SELECT 
            st.first_name AS firstName,
            st.last_name AS lastName,
            cs.class_section_id AS classSectionID,
            cs.name AS classSectionName,
            c.name AS className,
            c.number AS classNumber,
            su.name AS subjectCode,
            cs.start_time AS classSectionStartTime,
            cs.end_time AS classSectionEndTime,
            cs.days AS classSectionDays,
            cr.building_name AS building,
            cr.room_number AS roomNumber
        FROM Student st
        JOIN `Class_Section-Student` css ON st.student_id = css.student_id
        JOIN Class_Section cs ON css.class_section_id = cs.class_section_id
        JOIN Class c ON cs.class_id = c.class_id
        JOIN Subject su ON c.subject_id = su.subject_id
        JOIN Classroom cr ON cs.classroom_id = cr.classroom_id
        WHERE st.student_id = %s;"""

    SELECT_CLASS_SECTION_STUDENT = """
        SELECT 1 FROM `Class_Section-Student` WHERE student_id = %s AND class_section_id = %s;"""

  
    ADD_CLASS_SECTION = """
        INSERT INTO `Class_Section-Student` (student_id, class_section_id)
        VALUES (%s, %s);"""

    DROP_CLASS_SECTION = """
        DELETE FROM `Class_Section-Student` 
        WHERE student_id = %s 
        AND class_section_id = %s;"""

    VIEW_SECTION_STUDENT = """
        SELECT 
            cs.name AS classSectionName,
            c.name AS className,
            c.number AS classNumber,
            s.name AS subjectCode,
            m.module_id AS moduleID,
            m.name AS moduleName,
            m.description AS moduleDescription
        FROM `Class_Section-Student` css
        JOIN Class_Section cs ON css.class_section_id = cs.class_section_id
        JOIN Class c ON cs.class_id = c.class_id
        JOIN Subject s ON c.subject_id = s.subject_id
        JOIN Module m ON cs.class_section_id = m.class_section_id
        WHERE css.student_id = %s
        AND css.class_section_id = %s;"""

    VIEW_MODULE_STUDENT = """
    
        SELECT 
            cs.name AS classSectionName,
            c.name AS className,
            c.number AS classNumber,
            s.name AS subjectCode,
            m.module_id AS moduleID,
            m.name AS moduleName,
            m.description AS moduleDescription
        FROM `Class_Section-Student` css
        JOIN Class_Section cs ON css.class_section_id = cs.class_section_id
        JOIN Class c ON cs.class_id = c.class_id
        JOIN Subject s ON c.subject_id = s.subject_id
        JOIN Module m ON cs.class_section_id = m.class_section_id
        WHERE css.student_id = %s
        AND m.module_id = %s;"""

    VIEW_DOC_MODULE_STUDENT = """
        SELECT 
            m.module_id AS moduleID,
            m.name AS moduleName,
            m.description AS moduleDescription,
            d.document_id AS documentID,
            d.name AS documentName,
            d.description AS documentDescription,
            d.link AS documentLink
        FROM Module m
        JOIN Document d ON m.module_id = d.module_id
        WHERE m.module_id = %s;"""

    VIEW_ASSMT_MODULE_STUDENT = """
        SELECT 
            m.module_id AS moduleID,
            m.name AS moduleName,
            m.description AS moduleDescription,
            a.assignment_id AS assignmentID,
            a.name AS assignmentName,
            a.description AS assignmentDescription,
            a.link AS assignmentLink
        FROM Module m
        JOIN Assignment a ON m.module_id = a.module_id
        WHERE m.module_id = %s;"""

    VIEW_QUIZ_MODULE_STUDENT = """
        SELECT
            m.module_id AS moduleID,
            m.name AS moduleName,
            m.description AS moduleDescription,
            q.quiz_id AS quizID,
            q.title AS quizName,
            q.description AS quizDescription
        FROM Module m
        JOIN Quiz q ON m.module_id = q.module_id
        WHERE m.module_id = %s;"""

    VIEW_DOC_STUDENT = """
    
        SELECT 
            cs.name AS classSectionName,
            c.name AS className,
            c.number AS classNumber,
            s.name AS subjectCode,
            m.module_id AS moduleID,
            m.name AS moduleName,
            m.description AS moduleDescription,
            d.document_id AS documentID,
            d.name AS documentName,
            d.description AS documentDescription,
            d.link AS documentLink
        FROM `Class_Section-Student` css
        JOIN Class_Section cs ON css.class_section_id = cs.class_section_id
        JOIN Class c ON cs.class_id = c.class_id
        JOIN Subject s ON c.subject_id = s.subject_id
        JOIN Module m ON cs.class_section_id = m.class_section_id
        JOIN Document d ON m.module_id = d.module_id
        WHERE css.student_id = %s
        AND d.document_id = %s;"""

    VIEW_ASSMT_STUDENT = """
    
        SELECT 
            cs.name AS classSectionName,
            c.name AS className,
            c.number AS classNumber,
            s.name AS subjectCode,
            m.module_id AS moduleID,
            m.name AS moduleName,
            m.description AS moduleDescription,
            a.assignment_id AS assignmentID,
            a.name AS assignmentName,
            a.description AS assignmentDescription,
            a.link AS assignmentLink
        FROM `Class_Section-Student` css
        JOIN Class_Section cs ON css.class_section_id = cs.class_section_id
        JOIN Class c ON cs.class_id = c.class_id
        JOIN Subject s ON c.subject_id = s.subject_id
        JOIN Module m ON cs.class_section_id = m.class_section_id
        JOIN Assignment a ON m.module_id = a.module_id
        WHERE css.student_id = %s
        AND a.assignment_id = %s;"""

    VERIFY_STUDENT_ASSMT = """
        SELECT 1 
        FROM `Class_Section-Student`css 
        JOIN Class_Section cs ON css.class_section_id = cs.class_section_id
        JOIN Module m ON cs.class_section_id = m.class_section_id
        JOIN Assignment a ON m.module_id = a.module_id
        WHERE css.student_id = %s
        AND a.assignment_id = %s;"""

    SUBMIT_ASSMT = """
        INSERT INTO `Student-Completed-Assignment` (student_id, assignment_id, submittal_link)
        VALUES (%s, %s, %s);"""

    VIEW_SECTIONS_TAUGHT = """
        SELECT 
            t.first_name AS firstName,
            t.last_name AS lastName,
            cs.class_section_id AS classSectionID,
            cs.name AS classSectionName,
            c.name AS className,
            c.number AS classNumber,
            su.name AS subjectCode,
            cs.start_time AS classSectionStartTime,
            cs.end_time AS classSectionEndTime,
            cs.days AS classSectionDays,
            cr.building_name AS building,
            cr.room_number AS roomNumber
        FROM Teacher t
        JOIN `Class_Section-Teacher` cst ON t.teacher_id = cst.teacher_id  
        Join Class_Section cs ON cst.class_section_id = cs.class_section_id
        JOIN Class c ON cs.class_id = c.class_id
        JOIN Subject su ON c.subject_id = su.subject_id
        JOIN Classroom cr ON cs.classroom_id = cr.classroom_id
        WHERE t.teacher_id = %s;"""

    VIEW_SECTION_TEACHER = """
        SELECT 
            cs.name AS classSectionName,
            c.name AS className,
            c.number AS classNumber,
            s.name AS subjectCode,
            m.module_id AS moduleID,
            m.name AS moduleName,
            m.description AS moduleDescription
        FROM `Class_Section-Teacher` cst
        JOIN Class_Section cs ON cst.class_section_id = cs.class_section_id
        JOIN Class c ON cs.class_id = c.class_id
        JOIN Subject s ON c.subject_id = s.subject_id
        JOIN Module m ON cs.class_section_id = m.class_section_id
        WHERE cst.teacher_id = %s
        AND cst.class_section_id = %s;"""

    CREATE_MODULE_TEACHER = """
        INSERT INTO Module (class_section_id, name, description) VALUES(%s, %s, %s);"""


    VIEW_MODULE_TEACHER = """
    
          SELECT 
              cs.name AS classSectionName,
              c.name AS className,
              c.number AS classNumber,
              s.name AS subjectCode,
              m.module_id AS moduleID,
              m.name AS moduleName,
              m.description AS moduleDescription
          FROM `Class_Section-Teacher` cst
          JOIN Class_Section cs ON cst.class_section_id = cs.class_section_id
          JOIN Class c ON cs.class_id = c.class_id
          JOIN Subject s ON c.subject_id = s.subject_id
          JOIN Module m ON cs.class_section_id = m.class_section_id
          WHERE cst.teacher_id = %s
          AND m.module_id = %s;"""


    VERIFY_TEACHER_SECTION = """
        SELECT 1 FROM `Class_Section-Teacher` WHERE teacher_id = %s AND class_section_id = %s;"""

    VERIFY_TEACHER_MODULE = """
        SELECT 1 
        FROM `Class_Section-Teacher`cst 
        JOIN Class_Section cs ON cst.class_section_id = cs.class_section_id
        JOIN Module m ON cs.class_section_id = m.class_section_id
        WHERE cst.teacher_id = %s
        AND m.module_id = %s;"""

    CREATE_DOC_TEACHER = """
        INSERT INTO Document (module_id, name, description, link) VALUES(%s, %s, %s, %s);"""

    CREATE_ASSMT_TEACHER = """
        INSERT INTO Assignment (module_id, name, description, link, top_score) VALUES(%s, %s, %s, %s, %s)"""

    VERIFY_TEACHER_ASSMT = """
        SELECT 1 
        FROM `Class_Section-Teacher`cst 
        JOIN Class_Section cs ON cst.class_section_id = cs.class_section_id
        JOIN Module m ON cs.class_section_id = m.class_section_id
        JOIN Assignment a ON m.module_id = a.module_id
        WHERE cst.teacher_id = %s
        AND a.assignment_id = %s;"""

  
    VIEW_SUBMITTED_ASSMTS = """
        SELECT 
          cs.name AS classSectionName,
          c.name AS className,
          c.number AS classNumber,
          s.name AS subjectCode,
          m.name AS moduleName,
          a.assignment_id AS assignmentID,
          a.name AS assignmentName,
          a.top_score AS topScore,
          sca.submittal_link AS submittalLink,
          sca.score AS submittalScore,
          sca.sca_id AS submittalID,
          sca.student_id AS studentID
        FROM `Student-Completed-Assignment` sca
        JOIN Assignment a ON sca.assignment_id = a.assignment_id
        JOIN Module m ON a.module_id = m.module_id
        JOIN Class_Section cs ON m.class_section_id = cs.class_section_id
        JOIN Class c ON cs.class_id = c.class_id
        JOIN Subject s ON c.subject_id = s.subject_id
        WHERE sca.assignment_id = %s"""

    VERIFY_TEACHER_SUBMITTAL = """
        SELECT 1 
        FROM `Class_Section-Teacher`cst 
        JOIN Class_Section cs ON cst.class_section_id = cs.class_section_id
        JOIN Module m ON cs.class_section_id = m.class_section_id
        JOIN Assignment a ON m.module_id = a.module_id
        JOIN `Student-Completed-Assignment` sca ON sca.assignment_id = a.assignment_id
        WHERE cst.teacher_id = %s
        AND sca.sca_id = %s;"""
  
    GRADE_SUBMITTED_ASSIGNMENT = """
        UPDATE `Student-Completed-Assignment` SET score = %s WHERE sca_id = %s;"""

    VIEW_TEACHERS = """
        SELECT 
          t.teacher_id AS teacherID,
          t.first_name AS firstName,
          t.last_name AS lastName,
          d.dept_id AS departmentID,
          d.name AS departmentName
        FROM Teacher t
        JOIN Department d ON t.dept_id = d.dept_id;"""

    VIEW_SECTIONS = """
        SELECT 
          s.subject_id AS subjectID,
          s.name AS subjectCode,
          c.name AS className,
          c.number AS classNumber,
          cs.name AS classSectionName,
          cs.class_section_id AS classSectionID
        FROM Class_Section cs
        JOIN Class c ON cs.class_id = c.class_id
        JOIN Subject s ON c.subject_id = s.subject_id;"""

    VIEW_TEACHERS_SECTIONS = """
        SELECT 
          s.subject_id AS subjectID,
          s.name AS subjectCode,
          c.name AS className,
          c.number AS classNumber,
          cs.name AS classSectionName,
          cs.class_section_id AS classSectionID,
          t.teacher_id AS teacherID,
          t.first_name AS firstName,
          t.last_name AS lastName,
          d.dept_id AS departmentID,
          d.name AS departmentName
        FROM Teacher t
        JOIN `Class_Section-Teacher` cst ON t.teacher_id = cst.teacher_id
        JOIN Class_Section cs ON cst.class_section_id = cs.class_section_id
        JOIN Class c ON cs.class_id = c.class_id
        JOIN Subject s ON c.subject_id = s.subject_id
        JOIN Department d ON t.dept_id = d.dept_id"""



    ADD_TEACHER_SECTION = """
        INSERT INTO `Class_Section-Teacher` (teacher_id, class_section_id)
        VALUES (%s, %s);"""