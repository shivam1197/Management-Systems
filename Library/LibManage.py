import random
import datetime
#Library Management
class LibraryManage:
    author_list = []
    title_list = []

    def __init__(self):
        self.name=None
        self.Id=None
        self.book=None
        self.fine=None
        self.duedate=None
        self.issueddate=None
        self.timeissue=None
        self.cardno=None
        self.mobile=None
        self.location=None


    def IDgenerator(self):
        randid=random.randint(1,100)
        self.id=self.name[0:4]+self.mobile[6:10]+str(randid)
        return

    def Availablebooks(self):

        listofbooks = {
                        "Author": ["Salman Rushdie", "Javier Moro", "Dalai Lama"],
                       "Title": ["Two Year Eight Months and Twenty", "The Red Sari", "Freedom in Exile"]
                       }
        for author in listofbooks["Author"]:
            LibraryManage.author_list.append(author)

        for title in listofbooks["Title"]:
            LibraryManage.title_list.append(title)

        for i in range(3):
            print(LibraryManage.author_list[i]+"-"+LibraryManage.title_list[i])

        return

    def issuebook(self):
        for i in range(len(LibraryManage.title_list)):
            if lib.book==LibraryManage.title_list[i]:
                print("book is available to isssue")
                todaytime = datetime.datetime.now()
                self.timeissue=todaytime.strftime("%H:%M:%S")
                #print(self.timeissue)
                self.issueddate=todaytime.strftime("%d/%m/%Y")
                #print(self.issueddate)
                self.duedate=todaytime+datetime.timedelta(days=7,seconds=0)
                self.duedate.strftime("%d/%m/%Y")
            else:
                i=i+1
        return



#PL
if (__name__=="__main__"):
    lib=LibraryManage()
    lib.name=input("Name here :- ")
    lib.mobile=str(input("Enter the Mobile Number :-"))
    lib.IDgenerator()

    print("Your ID for Reference is :",lib.id)

    todaytime = datetime.date.today()
    lib.Availablebooks()
    lib.book = input("Name of the book :-")
    lib.issuebook()
    cardno = input("Number of Your card :-")


