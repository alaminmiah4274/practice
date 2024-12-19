from school import School
from person import Student, Teacher
from subject import Subject
from class_room import ClassRoom


my_school = School("ABC School", "Uttara")


# CLASS SECTION: --->
seven = ClassRoom("seven")
eight = ClassRoom("eight")
nine = ClassRoom("nine")
ten = ClassRoom("ten")

my_school.add_classroom(seven)
my_school.add_classroom(eight)
my_school.add_classroom(nine)
my_school.add_classroom(ten)



# STUDENT SECTION: --->
sabbir = Student("sabbir", seven)
rakib = Student("rakib", seven)
masum = Student("masum", seven)

palash = Student("palash", eight)
sakib = Student("sakib", eight)
tanvir = Student("tanvir", eight)

labib = Student("labib", nine)
adnan = Student("adnan", nine)
sadhin = Student("sadhin", nine)

murshid = Student("murshid", ten)
shafim = Student("shafim", ten)
nahiyan = Student("nahiyan", ten)


# ADDING STUDENT: ----> 
my_school.student_admission(sabbir)
my_school.student_admission(rakib)
my_school.student_admission(masum)
my_school.student_admission(palash)
my_school.student_admission(sakib)
my_school.student_admission(tanvir)
my_school.student_admission(labib)
my_school.student_admission(adnan)
my_school.student_admission(sadhin)
my_school.student_admission(murshid)
my_school.student_admission(shafim)
my_school.student_admission(nahiyan)



# TEACHER SECTION: --->
abul = Teacher("Abul")
babul = Teacher("Babul")
salam = Teacher("Salam")
kalam = Teacher("Kalam")


# SUBJECT SECTION: --->
bangla = Subject("Bangla", abul)
english = Subject("English", babul)
math = Subject("Math", salam)
ict = Subject("ICT", kalam)


# ADDING TEACHER: ---->
my_school.add_teacher(bangla, abul)
my_school.add_teacher(english, babul)
my_school.add_teacher(math, salam)
my_school.add_teacher(ict, kalam)


# ADDING SUBJECT: ----> 
seven.add_subject(bangla)
seven.add_subject(english)
seven.add_subject(math)

eight.add_subject(bangla)
eight.add_subject(english)
eight.add_subject(ict)

nine.add_subject(english)
nine.add_subject(math)
nine.add_subject(ict)

ten.add_subject(math)
ten.add_subject(ict)
ten.add_subject(bangla)



seven.take_semester_final()
eight.take_semester_final()
nine.take_semester_final()
ten.take_semester_final()


print(my_school)