class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades_lectors:
                lecturer.grades_lectors[course] += [grade]
            else:
                lecturer.grades_lectors[course] = [grade]
        else:
            return 'Ошибка'

    def average_student_grade(self):  #Average student grade
        sum = 0
        count = 0
        for i in self.grades.values():
            for j in i:
                sum += j
                count += 1
        return sum/count

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {round(self.avarage_student_grade(), 1)}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}')


    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Ошибка')
            return
        p = self.average_student_grade() < other.average_student_grade()
        if p == True:
            return f'Высокая средняя оценка у: {self.name} {self.surname}'
        else:
            return f'Высокая средняя оценка у: {other.name} {other.surname}'


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lectors = {}

    def average_lecturer_grade(self):  #Average lecturer grade
        sum = 0
        count = 0
        for i in self.grades_lectors.values():
            for j in i:
                sum += j
                count += 1
        return sum/count

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Ошибка')
            return
        p = self.average_lecturer_grade() < other.average_lecturer_grade()
        if p == True:
            return f'Высокая средняя оценка у: {self.name} {self.surname}'
        else:
            return f'Высокая средняя оценка у: {other.name} {other.surname}'

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {round(self.avarage_lecturer_grade(), 1)}')


class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}')

def all_average_student_grade(list_students, course_name):
    sum = 0
    count = 0
    for i in list_students:
        for j in i.grades[course_name]:
            sum += j
            count += 1
    return round(sum / count, 2)


def all_average_lecturer_grade(list_lectors, course_name):
    sum = 0
    count = 0
    for i in list_lectors:
        for j in i.grades_lectors[course_name]:
            sum += j
            count += 1
    return round(sum / count, 2)


#List of all people
Student_1 = Student('Ruoy', 'Eman', 'M')
Student_2 = Student('Alina', 'Emanor', 'F')

Lecturer_1 = Lecturer('Иван', 'Иванов')
Lecturer_2 = Lecturer('Петр', 'Петров')

Reviewer_1 = Reviewer('Алексей', 'Алексеев')
Reviewer_2 = Reviewer('Даниил', 'Данилов')

#Who teach courses
Lecturer_1.courses_attached += (['Git'])
Lecturer_1.courses_attached += (['Python'])

Lecturer_2.courses_attached += (['JavaScript'])
Lecturer_2.courses_attached += (['Python'])

Reviewer_1.courses_attached += (['Python'])
Reviewer_1.courses_attached += (['Git'])

#Finished courses and grades
Student_1.finished_courses += ['Введение в программирование']
Student_1.grades['Введение в программирование'] = [10, 10, 6, 8, 10]
Student_2.finished_courses += ['Введение в программирование']
Student_2.grades['Введение в программирование'] = [10, 8, 10, 7, 7]

#Courses in progress
Student_1.courses_in_progress += ['Git']
Student_1.courses_in_progress += ['Python']
Student_2.courses_in_progress += ['Python']
Student_2.courses_in_progress += ['JavaScript']

#Other
Reviewer_1.rate_hw(Student_1, 'Python', 7)
Reviewer_1.rate_hw(Student_1, 'Git', 8)

Reviewer_1.rate_hw(Student_2, 'Python', 7)
Reviewer_1.rate_hw(Student_2, 'JavaScript', 8)

Student_1.rate_lecturer(Lecturer_1, 'Git', 8)
Student_1.rate_lecturer(Lecturer_2, 'Python', 6)

Student_2.rate_lecturer(Lecturer_1, 'Python', 6)
Student_2.rate_lecturer(Lecturer_2, 'JavaScript', 10)

Mentor_1 = Mentor('Иван', 'Иванов')
Mentor_2 = Mentor('Петр', 'Петров')
Mentor_3 = Mentor('Алексей', 'Алексеев')
Mentor_4 = Mentor('Даниил', 'Данилов')

print(all_average_student_grade([Student_1, Student_2], 'Python'))
print(all_average_lecturer_grade([Lecturer_1, Lecturer_2], 'Python'))
