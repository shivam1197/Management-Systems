
class Student:
    stulist=[]
    def __init__(self):
        self.rollNo="" #Unique ID for every user
        self.name=None
        self.mobile=None
        self.dob=None
        self.address=None
        self.fee=None
        self.age=None
        self.course=None
        self.batch=None

    def rollnoGeneration(self): #Using 3 things to generate a string of roll number  #taking first 4 letters of the name
        age_using=self.age  #taking the complete age
        mob_using=self.mobile#Last 4 Digits of the mobile
        dob_using=self.dob
        self.rollNo=age_using+mob_using[6::]#Concatinating the string


    def timetableManagement(self): # manages the time table and returns the Studnet with the current timetable depending on the course
        if(self.course=="BCA"):
            return #someimage
        elif(self.course=="MCA"):
            return #someImage
        elif(self.course=="BBA"):
            return #someImage

    def feeManagement(self): #shows the fees depending the course of the student
        if (self.fee == "BCA"):
            BCAfees=self.fee = 10000
            return BCAfees
        elif (self.course == "MCA"):
            MCAfees=self.fee = 20000
            return MCAfees
        elif (self.course == "BBA"):
            BBAfees=self.fee = 30000
            return BBAfees

    def addStudent(self):
        '''this add function will append one student at a time in this student list.'''
        Student.stulist.append(self)



    def searchStudent(self):
        '''this search function will find student details on the basis of unique roll number.'''
        for e in Student.stulist:
         if (e.rollNo==self.rollNo):
            self.name = e.name
            self.mobile = e.mobile
            self.age=e.age
            self.dob = e.dob
            self.address = e.address
            self.course = e.course
            self.batch = e.batch
            return 1


    @staticmethod
    def deleteStudent(rollNo):
        '''this delete function will delete student details on the basis of unique roll number.'''
        for i in range(len(Student.stulist)):
            if Student.stulist[i].rollNo==rollNo:
                Student.stulist.pop(i)
                return 1

    def check(self):
        '''this check function will check if particular student's roll number exists in the list.'''
        for e in Student.stulist:
            if e.rollNo == stu.rollNo:
                return 1




    def modifyStudent(self):
        '''this modify function will modify existing student details on the basis of unique roll number'''
        for e in Student.stulist:
            if e.rollNo == stu.rollNo:
                e.name = self.name
                e.mobile = self.mobile
                e.age=self.age
                e.dob = self.dob
                e.address = self.address
                e.course = self.course
                e.batch = self.batch
                return 1


    def timetable(self):
        pass


# PL
while(1):
    def showStudent(stu):
        '''this show function will display all the student details.'''
        print('''"STUDENT ROLL NO:''', stu.rollNo,
              '''STUDENT NAME:''', stu.name,
              '''STUDENT MOBILE NO:''', stu.mobile,
              '''STUDENT DOB:''', stu.dob,
              '''STUDENT ADDRESS:''', stu.address,
               '''STUDENT COURSE:''', stu.course,
                '''STUDENT BATCH:''', stu.batch)

    print('''*WELCOME TO Student'S SMS*
    press 1 for add student,
    press 2 for search student
    press 3 for delete student
    press 4 for modify student
    press 5 for display all students
    0 for exit''')
    ch = input("press any number between 0-5 :) ")

    if ch == "1":  # add student
        try:
            stu = Student()
            # Taking the Input of Name
            while(1):
                first_name = input("enter your first name: ").strip( )
                if first_name.isalpha():
                    first_name=first_name.capitalize() #to make the first letter capitalize
                    break
                else:
                    print("Please enter name in alphabets only.")
            while(1):
                second_name=input("Enter your last name: ").strip( )
                if second_name.isalpha():
                    second_name=second_name.capitalize()
                    break
                else:
                    print("Please enter name in alphabets only.")
            stu.name=first_name+" "+second_name

            # Taking the Input of age
            while(1):
                stu.age = input("enter your age: ").strip( )
                if stu.age.isnumeric():
                    if int(stu.age)>=10 and int(stu.age)<=60:
                        break
                    else:
                        print("Student age should be minimum 10 year old and maximum 60 year old. :)")
                else:
                    print("Please enter age in numerics only.")

            # Taking the Input of Mobile Number
            while(1):
                stu.mobile = input("enter your mobile number: ").strip( )
                if stu.mobile.isnumeric():
                    if (len(stu.mobile))==10:
                        break
                    else:
                        print("Mobile number should be of 10 digits.")
                else:
                    print("Please enter mobile number in numerics only.")

            # Taking the Input of Date of Birth
            print("Enter your date of birth in numerical format: ")
            while(1):
                get_dd=input("Please enter date: ").strip( )
                if get_dd.isnumeric():
                    if len(get_dd)<=2:
                        if int(get_dd)>0 and int(get_dd)<32:
                            break
                        else:
                            print("Invalid date.")
                    else:
                        print("Invalid date.")
                else:
                    print("Enter date in numerics only.")
            while(1):
                get_mm=input("Please enter month: ").strip( )
                if get_mm.isnumeric():
                    if len(get_mm)<=2:
                        if int(get_mm) > 0 and int(get_mm) < 13:
                            break
                        else:
                            print("Enter valid month.")
                    else:
                        print("Invalid month.")
                else:
                    print("Enter month in numerics only.")
            while(1):
                get_yy=input("Please enter year: ").strip( )
                if get_yy.isnumeric():
                    if len(get_yy)==4:
                        if int(get_yy) > 1960:
                            if int(get_yy) <= 2011:
                                break
                            else:
                                print("Too young to register as a student.")
                        else:
                            print("Too old to register as a student.")
                    else:
                        print("Invalid year.")
                else:
                    print("Enter year in numerics only.")
            stu.dob=get_dd+"/"+get_mm+"/"+get_yy

            stu.address = input("enter your address: ")

            # Taking the Input of course
            while 1:
                course_choice = input("enter your course BCA ,MCA, BBA, MBA: ").upper()
                if course_choice.isalpha():
                    if course_choice == 'BCA' or course_choice == 'BBA':
                        course_year = 3
                        course = course_choice
                        break
                    elif course_choice == 'MCA' or course_choice == 'MBA':
                        course_year = 2
                        course = course_choice
                        break
                    else:
                        print("incorrect Choice")
                else:
                    print("Only choose from the following")

            # Taking the batch
            while(1):
                batch = input("enter your batch: ").strip( )
                if batch.isnumeric():
                    if int(batch)>1945 and int(batch)<2021:
                        total_time=int(batch)+course_year
                        stu.batch = batch+"-"+str(total_time)
                        break
                    else:
                        print("Enter batch year properly.")
                else:
                    print("Please enter batch in numerics only.")

            stu.rollnoGeneration()  # Genereating Roll number
            stu.addStudent()  # adding Students
            print("Adding...")
            print("Student Added Successfully.")
            print("your roll number is:", stu.rollNo)
        except Exception as err:
            print("ERROR! ", err)

    elif ch == "2":  # search student
        try:
            if Student.stulist==[]:
                print("it's empty, no student found.")
            else:
                stu = Student()
                stu.rollNo = input("enter roll number to search : ").strip( )
                print("Searching...")
                flag=stu.searchStudent()
                if flag:
                    print(f" HERE YOU GO!! NAME:", {stu.name}, "MOBILE NO:", {stu.mobile}, "DOB: ", {stu.dob}, "ADDRESS: ",
                      {stu.address}, "COURSE:", {stu.course},
                      "BATCH:", {stu.batch})
                else:
                    print("Student not found")
        except Exception as err:
            print("ERROR!", err)

    elif ch == "3":  # delete student
        try:
            rollNo = input("enter roll number to delete: ").strip( )
            flag=Student.deleteStudent(rollNo)
            if flag:
                print("Deleting...")
                print("Student deleted successfully.")
            else:
                print("Student not found.")
        except Exception as err:
            print("ERROR!", err)

    elif ch == "4":  # modify student
        try:
            stu = Student()
            stu.rollNo = input("enter your roll number: ").strip( )
            check=stu.check()
            if check:
                stu.name = input("enter your updated name: ")
                stu.age = input("enter your updated age: ")
                stu.mobile = input("enter youur updated mobile number: ")
                stu.dob = input("enter your updated dob: ")
                stu.address = input("enter your updated address: ")
                stu.course = input("enter your updated course: ")
                stu.batch = input("enter your updated batch: ")
                print("Modifying...")
                flag=stu.modifyStudent()
                if flag:
                    print("student modified succesfully.")
                else:
                    print("Student not found.")
            else:
                print("This roll number doesn't exist!")

        except Exception as err:
            print("ERROR!",err)

    elif ch == "5":# display all students
        try:
            if Student.stulist==[]:
                print("it's empty.")
            else:
                print("Displaying...")
                for e in Student.stulist:
                    showStudent(e)
        except Exception as err:
            print("ERROR!",err)
    elif ch == "0":# exit
        print("EXITING...")
        break
    else:
        print("incorrect choice.")

