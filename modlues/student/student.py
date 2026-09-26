class studentclass:
    def __init__(self):
        self.full_name = full_name
        self.dob = dob
        self.age = age
        self.gender = gender
        self.mobile_number = mobile_number
        self.email_address = email_address
        self.preferred_language = preferred_language
        self.school_college_name = school_college_name
        self.class_grade = class_grade
        self.board_curriculum = board_curriculum
        self.academic_year = academic_year
        self.subjects = subjects if subjects is not None else []
        self.subject_levels = subject_levels if subject_levels is not None else {}
        self.topics_help_needed = topics_help_needed if topics_help_needed is not None else {}
        self.guardian_name = guardian_name
        self.guardian_relationship = guardian_relationship
        self.guardian_mobile_number = guardian_mobile_number
        self.guardian_email_address = guardian_email_address
        self.preferred_communication_method = preferred_communication_method
    
