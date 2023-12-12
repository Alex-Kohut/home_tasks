class GroupIsFullError(Exception):
    def __init__(self, message="Group is full. Cannot add more than 10 students."):
        self.message = message
        super().__init__(self.message)

class Student:
    def __init__(self, gender, age, first_name, last_name, student_id):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id

    def __str__(self):
        return f'{self.first_name} {self.last_name}, ID: {self.student_id}'

class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupIsFullError()
        self.group.add(student)

    def delete_student(self, last_name):
        student_to_delete = self.find_student(last_name)
        if student_to_delete:
            self.group.remove(student_to_delete)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number: {self.number}\n{all_students}'


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)

try:
    for i in range(10):
        gr.add_student(Student('Male', 20, f'Student{i}', 'Lastname', f'RB{i}'))
except GroupIsFullError as e:
    print(e)

print(gr)

gr.delete_student('Taylor')
print(gr)

gr.delete_student('Taylor')