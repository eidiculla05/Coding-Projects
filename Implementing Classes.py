# HW2
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

import random, os

'''
This class represents a course, and has attributes cid (course id), cname (course name), credits (course credits).
'''
class Course:
    '''
        >>> c1 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c2 = Course('CMPSC360', 'Discrete Mathematics', 3)
        >>> c1 == c2
        False
        >>> c3 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c1 == c3
        True
        >>> c1
        CMPSC132(3): Programming in Python II
        >>> c2
        CMPSC360(3): Discrete Mathematics
        >>> c3
        CMPSC132(3): Programming in Python II
        >>> c1 == None
        False
        >>> print(c1)
        CMPSC132(3): Programming in Python II
    '''

    '''
    This function initializes Course instance.
    '''
    def __init__(self, cid, cname, credits):
        # YOUR CODE STARTS HERE
        self.cid=cid
        self.cname=cname
        self.credits=credits

    '''
    This function returns string representation of the Course.
    '''
    def __str__(self):
        # YOUR CODE STARTS HERE
        return self.cid+"("+str(self.credits)+"): "+self.cname

    __repr__ = __str__

    '''
    This function receives another Course object other and returns whether they have the same id or not.
    '''
    def __eq__(self, other):
        # YOUR CODE STARTS HERE
        if isinstance(other,Course):      # must be Course object
            return other.cid==self.cid
        else:
            return False


'''
This class represents a course catalog and has attribute courseOfferings (dictionary containing all course options).
'''
class Catalog:
    ''' 
        >>> C = Catalog()
        >>> C.courseOfferings
        {}
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> C.courseOfferings
        {'CMPSC 132': CMPSC 132(3): Programming and Computation II, 'MATH 230': MATH 230(4): Calculus and Vector Analysis, 'PHYS 213': PHYS 213(2): General Physics, 'CMPEN 270': CMPEN 270(4): Digital Design, 'CMPSC 311': CMPSC 311(3): Introduction to Systems Programming, 'CMPSC 360': CMPSC 360(3): Discrete Mathematics for Computer Science}
        >>> C.removeCourse('CMPSC 360')
        'Course removed successfully'
        >>> C.courseOfferings
        {'CMPSC 132': CMPSC 132(3): Programming and Computation II, 'MATH 230': MATH 230(4): Calculus and Vector Analysis, 'PHYS 213': PHYS 213(2): General Physics, 'CMPEN 270': CMPEN 270(4): Digital Design, 'CMPSC 311': CMPSC 311(3): Introduction to Systems Programming}
        >>> isinstance(C.courseOfferings['CMPSC 132'], Course)
        True
    '''

    '''
    This function initializes Catalog instance.
    '''
    def __init__(self):
        # YOUR CODE STARTS HERE
        self.courseOfferings={}

    '''
    This function receives cid (course id), cname (course name), credits (course credits).
    If the course is not already in the catalog, it is added and a confirmation message is returned.
    If it's already in the catalog, a message is returned stating this.
    '''
    def addCourse(self, cid, cname, credits):
        # YOUR CODE STARTS HERE
        if cid not in self.courseOfferings:
            self.courseOfferings[cid]=Course(cid,cname,credits)
            return "Course added successfully"
        else:
            return "Course already added"

    '''
    This function receives cid (course id) and removes the specified course from the catalog if it's in the catalog, returning a confirmation message.
    If the course is not in the catalog, a message is returned stating that it couldn't be found.
    '''
    def removeCourse(self, cid):
        # YOUR CODE STARTS HERE
        if cid in self.courseOfferings:
            del self.courseOfferings[cid]
            return "Course removed successfully"
        else:
            return "Course not found"

    '''
    This function receives a file, reads it, and adds the courses on the file to the catalog.
    '''
    def _loadCatalog(self, file):
        target_path = os.path.join(os.path.dirname(__file__), file)
        with open(target_path, "r") as f:
            course_info = f.read()
        # YOUR CODE STARTS HERE
        course_info=course_info.split('\n')
        for i in course_info:
            i=i.split(',')
            self.addCourse(i[0],i[1],i[2])
        

'''
This class represents a Semester and has attribute courses (dictionary of courses for the semester).
'''
class Semester:
    '''
        >>> cmpsc131 = Course('CMPSC 131', 'Programming in Python I', 3)
        >>> cmpsc132 = Course('CMPSC 132', 'Programming in Python II', 3)
        >>> math230 = Course("MATH 230", 'Calculus', 4)
        >>> phys213 = Course("PHYS 213", 'General Physics', 2)
        >>> econ102 = Course("ECON 102", 'Intro to Economics', 3)
        >>> phil119 = Course("PHIL 119", 'Ethical Leadership', 3)
        >>> spr22 = Semester()
        >>> spr22
        No courses
        >>> spr22.addCourse(cmpsc132)
        >>> isinstance(spr22.courses['CMPSC 132'], Course)
        True
        >>> spr22.addCourse(math230)
        >>> spr22
        CMPSC 132; MATH 230
        >>> spr22.isFullTime
        False
        >>> spr22.totalCredits
        7
        >>> spr22.addCourse(phys213)
        >>> spr22.addCourse(econ102)
        >>> spr22.addCourse(econ102)
        'Course already added'
        >>> spr22.addCourse(phil119)
        >>> spr22.isFullTime
        True
        >>> spr22.dropCourse(phil119)
        >>> spr22.addCourse(Course("JAPNS 001", 'Japanese I', 4))
        >>> spr22.totalCredits
        16
        >>> spr22.dropCourse(cmpsc131)
        'No such course'
        >>> spr22.courses
        {'CMPSC 132': CMPSC 132(3): Programming in Python II, 'MATH 230': MATH 230(4): Calculus, 'PHYS 213': PHYS 213(2): General Physics, 'ECON 102': ECON 102(3): Intro to Economics, 'JAPNS 001': JAPNS 001(4): Japanese I}
    '''

    '''
    This function initializes Semester instance.
    '''
    def __init__(self):
        # --- YOUR CODE STARTS HERE
        self.courses={}

    '''
    This function returns string representation of the Semester.
    '''
    def __str__(self):
        # YOUR CODE STARTS HERE
        if len(self.courses)!=0:
            string=''
            for i in self.courses:
                string+=i+"; "
            string=string[0:-2]     # Last one should not have a semicolon
            return string
        else:
            return "No courses"

    __repr__ = __str__

    '''
    This function receives course Course object and adds course to self.courses.
    Returns message if course has already been added.
    '''
    def addCourse(self, course):
        # YOUR CODE STARTS HERE
        if course.cid not in self.courses:
            self.courses[course.cid]=course
        else:
            return "Course already added"

    '''
    This function receives course Course object and removes course from self.courses.
    Returns message if course isn't in self.courses.
    '''
    def dropCourse(self, course):
        # YOUR CODE STARTS HERE
        if course.cid in self.courses:
            del self.courses[course.cid]
        else:
            return "No such course"

    '''
    Property method that adds up the credits from each course in self.courses.
    Returns total credits.
    '''
    @property
    def totalCredits(self):
        # YOUR CODE STARTS HERE
        credit=0
        for i in self.courses:
            credit+=int(self.courses[i].credits)
        return credit

    '''
    Property method that returns True is the total amount of credits is higher than 12.
    Return False if the total amount of credits is 12 or less. 
    '''
    @property
    def isFullTime(self):
        # YOUR CODE STARTS HERE
        if self.totalCredits>=12:
            return True
        else:
            return False

'''
This represents a student loan with loan_id attribute and loan amount attribute.
'''
class Loan:
    '''
        >>> import random
        >>> random.seed(2)  # Setting seed to a fixed value, so you can predict what numbers the random module will generate
        >>> first_loan = Loan(4000)
        >>> first_loan
        Balance: $4000
        >>> first_loan.loan_id
        17412
        >>> second_loan = Loan(6000)
        >>> second_loan.amount
        6000
        >>> second_loan.loan_id
        22004
        >>> third_loan = Loan(1000)
        >>> third_loan.loan_id
        21124
    '''
    
    '''
    This function initializes Loan instance.
    '''
    def __init__(self, amount):
        # YOUR CODE STARTS HERE
        self.loan_id=self.__getloanID
        self.amount=amount

    '''
    This function returns string representation of the loan.
    '''
    def __str__(self):
        # YOUR CODE STARTS HERE
        return "Balance: $"+str(self.amount)

    __repr__ = __str__

    '''
    Property method that returns a pseudorandomly generated loan id between 10000 and 99999.
    '''
    @property
    def __getloanID(self):
        # YOUR CODE STARTS HERE
        return random.randint(10000,99999)

'''
This class represents a person with attributes name (name of person) and ssn (person's social security number).
'''
class Person:
    '''
        >>> p1 = Person('Jason Lee', '204-99-2890')
        >>> p2 = Person('Karen Lee', '247-01-2670')
        >>> p1
        Person(Jason Lee, ***-**-2890)
        >>> p2
        Person(Karen Lee, ***-**-2670)
        >>> p3 = Person('Karen Smith', '247-01-2670')
        >>> p3
        Person(Karen Smith, ***-**-2670)
        >>> p2 == p3
        True
        >>> p1 == p2
        False
    '''

    '''
    This function receives name and ssn and initializes Person instance.
    '''
    def __init__(self, name, ssn):
        # YOUR CODE STARTS HERE
        self.name=name
        self.__ssn=ssn  # Private

    '''
    This function returns string representation of the Person.
    '''
    def __str__(self):
        # YOUR CODE STARTS HERE
        return "Person("+self.name+", ***-**-"+self.__ssn[7:]+")"   # Last four digits of ssn

    __repr__ = __str__

    '''
    This function returns self.__ssn.
    '''
    def get_ssn(self):
        # YOUR CODE STARTS HERE
        return self.__ssn

    '''
    This function receives other Person object, returns whether other.ssn = self.ssn.
    '''
    def __eq__(self, other):
        # YOUR CODE STARTS HERE
        if isinstance(other,Person):
            return other.get_ssn()==self.__ssn
        else:
            return False
        
'''
This class inherits the Person class and represents a Staff member.
Has attributes name, ssn, and supervisor.
'''
class Staff(Person):
    '''
        >>> C = Catalog()
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> s1 = Staff('Jane Doe', '214-49-2890')
        >>> s1.getSupervisor
        >>> s2 = Staff('John Doe', '614-49-6590', s1)
        >>> s2.getSupervisor
        Staff(Jane Doe, 905jd2890)
        >>> s1 == s2
        False
        >>> s2.id
        '905jd6590'
        >>> p = Person('Jason Smith', '221-11-2629')
        >>> st1 = s1.createStudent(p)
        >>> isinstance(st1, Student)
        True
        >>> s2.applyHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        'Unsuccessful operation'
        >>> s2.removeHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        >>> st1.enrollCourse('CMPSC 132', C)
        'Course added successfully'
        >>> st1.semesters
        {1: CMPSC 132}
        >>> s1.applyHold(st1)
        'Completed!'
        >>> st1.enrollCourse('CMPSC 360', C)
        'Unsuccessful operation'
        >>> st1.semesters
        {1: CMPSC 132}
    '''

    '''
    This function initializes Staff instance).
    '''
    def __init__(self, name, ssn, supervisor=None): # supervisor defaults to None
        # YOUR CODE STARTS HERE
        super().__init__(name,ssn)
        self.supervisor=supervisor


    '''
    This function returns string representation of the Staff object.
    '''
    def __str__(self):
        # YOUR CODE STARTS HERE
        return "Staff("+self.name+", "+self.id+")"

    __repr__ = __str__

    '''
    Property method that returns the Staff's id with format 905(initials)(last 4 digits of ssn).
    '''
    @property
    def id(self):
        # YOUR CODE STARTS HERE
        name=self.name.split(' ')
        initials=''
        for i in name:
            initials+=i[0]
        return str(905)+initials.lower()+self.get_ssn()[-4:]

    '''
    This function returns supervisor.
    '''
    @property   
    def getSupervisor(self):
        # YOUR CODE STARTS HERE
        return self.supervisor

    '''
    This function receives a Staff object new_supervisor and sets self.supervisor equal to it.
    Returns confirmation message.
    '''
    def setSupervisor(self, new_supervisor):
        # YOUR CODE STARTS HERE
        if isinstance(new_supervisor,Staff):
            self.supervisor=new_supervisor
            return "Completed!"

    '''
    This function receives a Student student and changes their hold status to True.
    Returns confirmation message.
    '''
    def applyHold(self, student):
        # YOUR CODE STARTS 
        if isinstance(student,Student):
            student.hold=True
            return "Completed!"

    '''
    This function receives a Student student and changes their hold status to False.
    Returns confirmation message.
    '''
    def removeHold(self, student):
        # YOUR CODE STARTS HERE
        if isinstance(student,Student):
            student.hold=False
            return "Completed!"

    '''
    This function receives a Student student  and changes their active status to False.
    Returns confirmation message.
    '''
    def unenrollStudent(self, student):
        # YOUR CODE STARTS HERE
        if isinstance(student,Student):
            student.active=False
            return "Completed!"

    '''
    This function receives a person and returns a new Student object with their name and ssn and with the year set to Freshman.
    '''
    def createStudent(self, person):
        # YOUR CODE STARTS HERE
        return Student(person.name,person.get_ssn(),"Freshman")


'''
This class inherits Person and represents a student and has attributes name, ssn, classCode (year), semesters (dictionary of Semesters), hold (hold status), active (active status), account (StudentAccount object).
'''
class Student(Person):
    '''
        >>> C = Catalog()
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1
        Student(Jason Lee, jl2890, Freshman)
        >>> s2 = Student('Karen Lee', '247-01-2670', 'Freshman')
        >>> s2
        Student(Karen Lee, kl2670, Freshman)
        >>> s1 == s2
        False
        >>> s1.id
        'jl2890'
        >>> s2.id
        'kl2670'
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC 132', C)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC 132}
        >>> s1.enrollCourse('CMPSC 360', C)
        'Course added successfully'
        >>> s1.enrollCourse('CMPSC 465', C)
        'Course not found'
        >>> s1.semesters
        {1: CMPSC 132; CMPSC 360}
        >>> s2.semesters
        {}
        >>> s1.enrollCourse('CMPSC 132', C)
        'Course already enrolled'
        >>> s1.dropCourse('CMPSC 360')
        'Course dropped successfully'
        >>> s1.dropCourse('CMPSC 360')
        'Course not found'
        >>> s1.semesters
        {1: CMPSC 132}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC 132, 2: No courses}
        >>> s1.enrollCourse('CMPSC 360', C)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC 132, 2: CMPSC 360}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC 132, 2: CMPSC 360, 3: No courses}
        >>> s1
        Student(Jason Lee, jl2890, Sophomore)
        >>> s1.classCode
        'Sophomore'
    '''

    '''
    This function receives name, ssn, year and initializes Student instance.
    '''
    def __init__(self, name, ssn, year):
        random.seed(1)
        # YOUR CODE STARTS HERE
        super().__init__(name,ssn)
        self.classCode=year
        self.semesters={}
        self.hold=False
        self.active=True
        self.account=self.__createStudentAccount()

    '''
    This function returns string representation of Student object.
    '''
    def __str__(self):
        # YOUR CODE STARTS HERE
        return 'Student('+self.name+", "+self.id+", "+self.classCode+")"
        

    __repr__ = __str__

    '''
    This function creates new StudentAccount object if the Student is active.
    '''
    def __createStudentAccount(self):
        # YOUR CODE STARTS HERE
        if self.active:
            return StudentAccount(self)

    '''
    Property method that returns Student id in format (initials)(last four digits of ssn).
    '''
    @property
    def id(self):
        # YOUR CODE STARTS HERE
        name=self.name.split(' ')
        initials=''
        for i in name:  # Gets initials
            initials+=i[0]
        return initials.lower()+self.get_ssn()[-4:]

    '''
    This function adds new Semester to self.semesters and changes self.classCode based on semester number.
    Returns an error message if the student is inactive or has a hold.
    '''
    def registerSemester(self):
        # YOUR CODE STARTS HERE
        if self.active and self.hold==False:
            key=max(self.semesters,default=0)+1
            self.semesters[key]=Semester()
            if key==1 or key==2:
                self.classCode="Freshman"
            elif key==3 or key==4:
                self.classCode="Sophomore"
            elif key==5 or key==6:
                self.classCode="Junior"
            else:
                self.classCode="Senior"
        else:
            return "Unsuccessful operation"

    '''
    Function receives cid (course id) and Catalog catalog.
    This function adds the course from the catalog to the Student's course list and charges their account, returns confirmation message.
    If this is unable to be done, a message is returned telling the user what went wrong.
    '''
    def enrollCourse(self, cid, catalog):
        # YOUR CODE STARTS HERE
        if self.active==False or self.hold:
            return "Unsuccessful operation"
        if cid in catalog.courseOfferings:
            if cid in self.semesters[max(self.semesters,default=0)].courses:
                return "Course already enrolled"
            else:
                self.semesters[max(self.semesters,default=0)].courses[cid]=catalog.courseOfferings[cid]
                self.account.chargeAccount(int(catalog.courseOfferings[cid].credits)*StudentAccount.CREDIT_PRICE)
                return "Course added successfully"
        return "Course not found"
        
    '''
    Function receives cid (course id)
    This function removes course from Student course list and refunds half the amount to their StudentAccount, returns confirmation message.
    If this is unable to be done, a message is returned telling the user what went wrong
    '''
    def dropCourse(self, cid):
        # YOUR CODE STARTS HERE
        if self.active==False or self.hold:
            return "Unsuccessful operation"
        if cid in self.semesters[max(self.semesters)].courses:
            self.account.makePayment(int(self.semesters[max(self.semesters)].courses[cid].credits)*StudentAccount.CREDIT_PRICE*.5)
            del self.semesters[max(self.semesters)].courses[cid]
            return "Course dropped successfully"
        else:
            return "Course not found"

    '''
    This function receives int amount and adds to StudentAccount balance and creates new Loan which is added to loans dictionary.
    Returns message if unsuccessful.
    '''
    def getLoan(self, amount):
        # YOUR CODE STARTS HERE
        if self.active and self.semesters[max(self.semesters)].isFullTime:
            loan=Loan(amount)
            self.account.loans[loan.loan_id]=loan
            self.account.makePayment(amount)
        elif not self.active:
            return "Unsuccessful operation"
        else:
            return "Not full-time"



'''
This class represents student's financial status and has attributes CREDIT_PRICE, Student student, balance, and loans (dictionary of loans).
'''
class StudentAccount:
    '''
        >>> C = Catalog()
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC 132', C)
        'Course added successfully'
        >>> s1.account.balance
        3000
        >>> s1.enrollCourse('CMPSC 360', C)
        'Course added successfully'
        >>> s1.account.balance
        6000
        >>> s1.enrollCourse('MATH 230', C)
        'Course added successfully'
        >>> s1.enrollCourse('PHYS 213', C)
        'Course added successfully'
        >>> print(s1.account)
        Name: Jason Lee
        ID: jl2890
        Balance: $12000
        >>> s1.account.chargeAccount(100)
        12100
        >>> s1.account.balance
        12100
        >>> s1.account.makePayment(200)
        11900
        >>> s1.getLoan(4000)
        >>> s1.account.balance
        7900
        >>> s1.getLoan(8000)
        >>> s1.account.balance
        -100
        >>> s1.enrollCourse('CMPEN 270', C)
        'Course added successfully'
        >>> s1.account.balance
        3900
        >>> s1.dropCourse('CMPEN 270')
        'Course dropped successfully'
        >>> s1.account.balance
        1900.0
        >>> s1.account.loans
        {27611: Balance: $4000, 84606: Balance: $8000}
        >>> StudentAccount.CREDIT_PRICE = 1500
        >>> s2 = Student('Thomas Wang', '123-45-6789', 'Freshman')
        >>> s2.registerSemester()
        >>> s2.enrollCourse('CMPSC 132', C)
        'Course added successfully'
        >>> s2.account.balance
        4500
        >>> s1.enrollCourse('CMPEN 270', C)
        'Course added successfully'
        >>> s1.account.balance
        7900.0
    '''

    CREDIT_PRICE=1000   #attribute for all instances of the StudentAccount class

    '''
    This function receives Student student and initializes StudentAccount instance.
    '''
    def __init__(self, student):
        # YOUR CODE STARTS HERE
        self.student=student
        self.balance=0
        self.loans={}

    '''
    This function returns string representation of StudentAccount.
    '''
    def __str__(self):
        # YOUR CODE STARTS HERE
        return "Name: "+self.student.name+"\nID: "+self.student.id+"\nBalance: $"+str(self.balance)

    __repr__ = __str__

    '''
    This function receives int amount and removes the amount from self.balance.
    Returns the updated balance.
    '''
    def makePayment(self, amount):
        # YOUR CODE STARTS HERE
        self.balance-=amount
        return self.balance

    '''
    This function receives int amount and adds the amount to self.balance.
    Returns the updated balance.
    '''
    def chargeAccount(self, amount):
        # YOUR CODE STARTS HERE
        self.balance+=amount
        return self.balance




def run_tests():
    import doctest

    # Run tests in all docstrings
    doctest.testmod(verbose=True)
    
    #Run tests per function - Uncomment the next line to run doctest by function. Replace Course with the name of the function you want to test
    doctest.run_docstring_examples(Student, globals(), name='HW2',verbose=True)   

if __name__ == "__main__":
    run_tests()