class TotalMarks:
    """
    student's marks in different subjects
    """
    num_students = 0
    student: str
    marks: float
    def __init__(self, student, marks):
        self.student = student
        self.marks = marks
        TotalMarks.num_students += 1

    def __repr__(self):
        return f"Student: {self.student}, Marks: {self.marks}"

    def chemistry(self, marks:float):
        self.marks += marks
    
    def maths(self, marks:float):
        self.marks += marks

    def inquiry(self) -> float:
        return self.marks

id_1 = TotalMarks('Mahesh', 100)
id_2 = TotalMarks('Gunn', 150)

id_1.chemistry(50)
id_2.maths(70)

print(id_1)
print(id_1.student)

print(vars(id_1), vars(id_2))

print(type(id_1))
print(type(id_1).chemistry)

print(id_1.student)          #get
id_1.marks = 300             #set
print(id_1.marks)
#del id_1.marks              #delete

id_1.result_date = '2022-2-19'
id_1.nickname    = 'Genius'
print(id_1.result_date)
print(id_1.nickname)

getattr(id_1, 'student')
setattr(id_1, 'marks', 500)
#delattr(id_1, 'marks')

print(hasattr(id_1, 'student'))   #to check the existence of an attribute

getattr(id_1, 'maths')(100)
print(id_1.marks)

print(getattr(id_1, 'attendance', 'unknown'))  #to check the existence of an attribute

bm = id_1.chemistry               #bound method
print(bm)

bm(100)
print(id_1)

#inheritance
class Great(TotalMarks):
    def genius(self):
        self.inquiry() > 500
        print('Genius')

id_3 = Great('Santa', 501)
id_3.genius()                     #return Genius

print(TotalMarks.num_students)
