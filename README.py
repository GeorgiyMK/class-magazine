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

    def __str__(self):
        return f'Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за домашние задания: {self.average_grade()}\n Курсы в процессе изучения: {self.courses_in_progress}\n Завершенные курсы:{self.finished_courses}'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    def __str__(self):
        return f ''
        

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

    def __str__(self):
        return f'Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за лекции: {self.average_grade()}'

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
        return f'Имя: {self.name}\n Фамилия: {self.surname}'

# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.finished_courses += ['Git']
# best_student.courses_in_progress += ['Python']
# best_student.grades['Git'] = [10, 10, 10, 10, 10]
# best_student.grades['Python'] = [10, 10]