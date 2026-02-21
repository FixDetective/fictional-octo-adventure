# Задание 1
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def _average_grade(self):
        total = 0
        count = 0
        for grades_list in self.grades.values():
            total += sum(grades_list)
            count += len(grades_list)
        if count != 0:
            return total / count if count > 0 else 0
        else:
            return 0

    def __str__(self):
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: {self._average_grade():.1f}\n"
            f"Курсы в прогрессе: {', '.join(self.courses_in_progress)}\n"
            f"Завершенные курсы: {', '.join(self.finished_courses)}"
        )

    def __lt__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Нельзя сравнивать студента с объектом другого типа")
        return self._average_grade() < other._average_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Нельзя сравнивать студента с объектом другого типа")
        return self._average_grade() <= other._average_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Нельзя сравнивать студента с объектом другого типа")
        return self._average_grade() > other._average_grade()

    def __ge__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Нельзя сравнивать студента с объектом другого типа")
        return self._average_grade() >= other._average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Нельзя сравнивать студента с объектом другого типа")
        return self._average_grade() == other._average_grade()

    def __ne__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Нельзя сравнивать студента с объектом другого типа")
        return self._average_grade() != other._average_grade()

    def rate_lecture(self, lecturer_obj, course, grade):
        if (
            isinstance(lecturer_obj, Lecturer)
            and course in lecturer_obj.courses_attached
            and course in self.courses_in_progress
        ):
            if course in lecturer_obj.grades:
                lecturer_obj.grades[course] += grade
            else:
                lecturer_obj.grades[course] = [grade]
        else:
            return "Ошибка!"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_grade(self):
        total = 0
        count = 0
        for grades_list in self.grades.values():
            total += sum(grades_list)
            count += len(grades_list)
        if count != 0:
            return total / count if count > 0 else 0
        else:
            return 0

    def __str__(self):
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за лекции: {self._average_grade():.1f}"
        )

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Нельзя сравнивать лектора с объектом другого типа")
        return self._average_grade() < other._average_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Нельзя сравнивать лектора с объектом другого типа")
        return self._average_grade() <= other._average_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Нельзя сравнивать лектора с объектом другого типа")
        return self._average_grade() > other._average_grade()

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Нельзя сравнивать лектора с объектом другого типа")
        return self._average_grade() >= other._average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Нельзя сравнивать лектора с объектом другого типа")
        return self._average_grade() == other._average_grade()

    def __ne__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Нельзя сравнивать лектора с объектом другого типа")
        return self._average_grade() != other._average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (
            isinstance(student, Student)
            and course in self.courses_attached
            and course in student.courses_in_progress
        ):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


def average_student_grade(students, course):
    total = 0
    count = 0
    for student in students:
        if isinstance(student, Student) and course in student.grades:
            total += sum(student.grades[course])
            count += len(student.grades[course])
    return total / count if count > 0 else 0


def average_lecturer_grade(lecturers, course):
    total = 0
    count = 0
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer) and course in lecturer.grades:
            total += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    return total / count if count > 0 else 0


# Создание экземпляров классов
student1 = Student("Алёхина", "Ольга", "Ж")
student2 = Student("Иван", "Иванов", "М")

lecturer1 = Lecturer("Петр", "Петров")
lecturer2 = Lecturer("Сергей", "Сидоров")

reviewer1 = Reviewer("Анна", "Андреева")
reviewer2 = Reviewer("Мария", "Михайлова")

# Назначение курсов
student1.courses_in_progress += ["Python", "Java"]
student2.courses_in_progress += ["Python", "C++"]

lecturer1.courses_attached += ["Python", "Java"]
lecturer2.courses_attached += ["Python", "C++"]

reviewer1.courses_attached += ["Python", "Java"]
reviewer2.courses_attached += ["Python", "C++"]

# Оценка лекций и домашних заданий
reviewer1.rate_hw(student1, "Python", 9)
reviewer1.rate_hw(student1, "Java", 8)
reviewer1.rate_hw(student2, "Python", 7)

reviewer2.rate_hw(student2, "C++", 9)

student1.rate_lecture(lecturer1, "Python", 10)
student1.rate_lecture(lecturer1, "Java", 9)
student2.rate_lecture(lecturer2, "Python", 8)
student2.rate_lecture(lecturer2, "C++", 9)


print("Студенты:")
print(student1)
print(student2)

print("\nЛекторы:")
print(lecturer1)
print(lecturer2)

print("\nПроверяющие:")
print(reviewer1)
print(reviewer2)

# Сравнение Студентов
print("\nСравнение студентов:")
print(f"{student1.name} < {student2.name}: {student1 < student2}")
print(f"{student1.name} > {student2.name}: {student1 > student2}")

# Сравнение Лекторов
print(f"{lecturer1.name} < {lecturer2.name}: {lecturer1 < lecturer2}")
print(f"{lecturer1.name} > {lecturer2.name}: {lecturer1 > lecturer2}")

# Средние оценки по курсам
print(
    f"Средняя оценка студентов по Python: {average_student_grade([student1, student2], 'Python'):.1f}"
)
print(
    f"Средняя оценка лекторов по Python: {average_lecturer_grade([lecturer1, lecturer2], 'Python'):.1f}"
)
