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