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
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        grades_list = []
        for grades in self.grades.values():
            for grade in grades:
                grades_list.append(grade)
        if len(grades_list) > 0:
            average = sum(grades_list)/len(grades_list)
        else:
            average = 0
        return average

    def __str__(self):
        avg_grade = self.average_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {avg_grade:.1f}\n'
                f'Курсы в процессе изучения: {courses_in_progress}\n'
                f'Завершенные курсы: {finished_courses}')
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка'
        return self.average_grade() < other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name,surname)
        self.grades = {}

    def average_grade(self):
        grades_list = []
        for grades in self.grades.values():
            for grade in grades:
                grades_list.append(grade)
        if len(grades_list) > 0:
            average = sum(grades_list)/len(grades_list)
        else:
            average = 0
        return average
    
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade():.1f}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка'
        return self.average_grade() < other.average_grade()


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
        return f"Имя: {self.name}\nФамилия: {self.surname}"


def average_student_grade(students, course):
    total_grades = []
    for student in students:
        if course in student.grades:
            total_grades.extend(student.grades[course])
    if total_grades:
        return sum(total_grades)/len(total_grades)
    else:
        return 0
    
def average_lecturer_grade(lecturers, course):
    total_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades.extend(lecturer.grades[course])
    if total_grades:
        return sum(total_grades)/len(total_grades)
    else:
        return 0

student1 = Student('Harry', 'Potter', 'male')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в программирование']
 
student2 = Student('Hermione', 'Granger', 'female')
student2.courses_in_progress += ['Python', 'Git']
student2.finished_courses += ['Введение в программирование']

reviewer1 = Reviewer('Severus', 'Snape')
reviewer1.courses_attached += ['Python', 'Введение в программирование']

reviewer2 = Reviewer('Minerva', 'McGonagall')
reviewer2.courses_attached += ['Git', 'Введение в программирование']

lecturer1 = Lecturer('Dolores', 'Umbridge')
lecturer1.courses_attached += ['Python', 'Введение в программирование']

lecturer2 = Lecturer('Gilderoy', 'Lockhart')
lecturer2.courses_attached += ['Git', 'Введение в программирование']

student1.rate_lecturer(lecturer1, 'Python', 2)
student2.rate_lecturer(lecturer1, 'Python', 3)
student1.rate_lecturer(lecturer2, 'Git', 10)
student2.rate_lecturer(lecturer2, 'Git', 10)

reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student2, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 7)
reviewer1.rate_hw(student2, 'Python', 9)

reviewer2.rate_hw(student1, 'Git', 9)
reviewer2.rate_hw(student2, 'Git', 10)
reviewer2.rate_hw(student1, 'Git', 8)
reviewer2.rate_hw(student2, 'Git', 10)

print(reviewer1)
print(lecturer1)
print(student1)
print(student1 > student2)
print(lecturer1 < lecturer2)