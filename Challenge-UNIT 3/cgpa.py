class Student:
  def __init__(self, name, roll_number, cgpa):
      self.name = name
      self.roll_number = roll_number
      self.cgpa = cgpa

def sort_students(student_list):
  sorted_students = sorted(student_list, key=lambda student:student.cgpa, reverse=True)
  return sorted_students

# Example usage:
students=[Student('Hari','A123',7.8),Student('Shree','A124',9.8),Student('Jay','A125',6.9)]
sorted_students=sort_students(students)

for student in sorted_students:
  print('Name:{}, Roll no:{}, CGPA:{}'.format(student.name,student.roll_number, student.cgpa))