class studentclass:
    def __init__(self):
        self.full_name = ''
        self.dob = ''
        self.age = ''
        self.gender = ''
        self.mobile_number = ''
        self.email_address = ''
        self.password = ''
        self.preferred_language = ''
        self.school_college_name = ''
        self.class_grade = ''
        self.board_curriculum = ''
        self.academic_year = ''
        self.subjects = []
        self.subject_levels = {}
        self.topics_help_needed = {}
        self.guardian_name = ''
        self.guardian_relationship = ''
        self.guardian_mobile_number = ''
        self.guardian_email_address = ''
        self.preferred_communication_method = ''
    def setusernameandpassword(self, email, password):
        self.email_address = email
        self.password = password


    def setbasicDetails(self, full_name, dob, age, gender, mobile_number, preferred_language, school_college_name, class_grade, board_curriculum, academic_year):
        '''
        This method sets the basic education details of the student.
        '''
        self.full_name = full_name
        self.dob = dob
        self.age = age
        self.gender = gender
        self.mobile_number = mobile_number
        if len(mobile_number) != 10:
            print("Invalid mobile number. Please enter a 10-digit mobile number.")
            return
        self.preferred_language = preferred_language
        self.school_college_name = school_college_name
        self.class_grade = class_grade
        self.board_curriculum = board_curriculum
        self.academic_year = academic_year    
    def savetodb(self):
        import sqlite3
        connection = sqlite3.connect("tution.db")
        cursor = connection.cursor()
        cursor.execute("""
             
             insert into student(
                    name,
                    dob,
                    age,
                    gender,
                    mobile,
                    email,
                    password,
                    school_college_name,
                    class_grade,
                    board_curriculam,
                    academic_year
                    ) values (?,?,?,?,?,?,?,?,?,?,?,?)                
            """,
            (self.full_name,
            self.dob,
            self.age,
            self.gender,
            self.mobile_number,
            self.email_address,
            self.password,
            self.preferred_language,
            self.school_college_name,
            self.class_grade,
            self.board_curriculum,
            self.academic_year
            ))
        connection.commit()
        connection.close()
