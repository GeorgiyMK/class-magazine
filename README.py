from builtins import PythonFinalizationError


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course,grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        total = 0
        count = 0
        for grades in self.grades.values():
            total += sum(grades)
            count += len(grades)
        return total / count if count > 0 else 0

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.average_grade() >= other.average_grade()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_grade() == other.average_grade()
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() > other.average_grade()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Student):
            return self.average_grade() <= other.average_grade()
        return NotImplemented

    def __str__(self):
        return (f'Имя: {self.name}\n Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average_grade()}\n'
                f'Курсы в процессе изучения: {self.courses_in_progress}\n'
                f'Завершенные курсы:{self.finished_courses}')

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
   
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    def average_grade(self):
        total = 0
        count = 0
        for grades in self.grades.values():
            total += sum(grades)
            count += len(grades)
        return total / count if count > 0 else 0

    def __ge__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() >= other.average_grade()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() == other.average_grade()
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() < other.average_grade()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() > other.average_grade()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() <= other.average_grade()
        return NotImplemented

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}'

class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

def average_student_grade(students, course):
    total = 0
    count = 0
    for student in students:
        if course in student.grades:
            total += sum(student.grades[course])
            count += len(student.grades[course])
    return total / count if count > 0 else 0

def average_lecturer_grade(lecturers, course):
    total = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.courses_attached:
            total += lecturer.average_grade()
            count += 1
    return total / count if count > 0 else 0

best_student = Student('John', 'Rambo', 'man')
best_student.finished_courses += ['Git']
best_student.courses_in_progress += ['Python']
best_student.grades['Git'] = [10, 10, 10, 10, 10]
best_student.grades['Python'] = [10, 10]

worst_student = Student('{Pamella}', 'Anderson', 'woman')
worst_student.finished_courses += ['Git']
worst_student.courses_in_progress += ['Python']
worst_student.grades['Git'] = [10, 5, 7, 8, 10]
worst_student.grades['Python'] = [10, 3]

best_lecturer = Lecturer('Михаил','Ломоносов')
best_lecturer.courses_attached += ['Python']
best_lecturer.grades['Python'] = [8, 4, 10, 10]

worst_lecturer = Lecturer('Иван','Васильев')
worst_lecturer.courses_attached += ['Python','GIT','OOP']
worst_lecturer.grades['GIT'] = [4, 4, 6, 6, 10, 10]

best_reviewer = Reviewer('Дмитрий','Менделеев')
best_reviewer.courses_attached += ['Python']

worst_reviewer = Reviewer('Иосиф', 'Кобзон')
worst_reviewer.courses_attached += ['Python']

worst_student.rate_lecturer(worst_lecturer, 'Python',9)

best_reviewer.rate_student(worst_student, 'Python', 10)

print(worst_lecturer.average_grade())

print(best_student > worst_student)
