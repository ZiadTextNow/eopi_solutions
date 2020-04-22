import collections
import bisect


Student = collections.namedtuple('Student', ('name', 'grade_point_average'))


def comp_gpa(student):
    return -student.grade_point_average, student.name


def search_students(students, target, comp_gpa):
    i = bisect.bisect_left([comp_gpa(s) for s in students], comp_gpa(target))
    return 0 <= i < len(students) and students[i] == target


if __name__ == "__main__":
    student_1 = Student('a', 100)
    student_2 = Student('b', 80)
    student_3 = Student('c', 50)
    student_4 = Student('d', 20)
    student_5 = Student('e', 10)
    students = [student_1, student_2, student_3, student_4]
    target = student_3
    print(search_students(students, target, comp_gpa))
