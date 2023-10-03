# from os import system as s
# s("cls")
class Grade:
    def __init__(self, stu_id, crc_code, score):
        self.student_id = stu_id
        self.course_code = crc_code
        self.score = score

    def __str__(self) -> str:
        return f"{self.student_id} {self.course_code} {self.score}"


class CourseUtil:

    def set_file(self, address):
        self.f = open(address, 'r+')
        self.lines = self.f.readlines()
        self.add = address


        

    def load(self, line_number): 

        self.count_lines = len(self.lines)
        if line_number <= self.count_lines: 
            arbitary_line = self.lines[self.count_lines - 1]
            arbitary_line_split = arbitary_line.split(' ')
            return (Grade(arbitary_line_split[0], arbitary_line_split[1], arbitary_line_split[2]))
        else:
            return None

    def calc_student_average(self, student_id):
        grade_student_lst = []
        avg = 0
        for line in self.lines:
            if line.find(student_id):
                grade = line.split(' ')[2].split("\n")[0]
                grade = float(grade)
                grade_student_lst.append(grade)
                avg = sum(grade_student_lst)/len(grade_student_lst)
        return avg
    def calc_course_average(self, course_code):
        grade_student_lst = []
        avg = 0
        for line in self.lines:
            if line.find(course_code):
                grade = line.split(' ')[2].split("\n")[0]
                grade = float(grade)
                grade_student_lst.append(grade)
                avg = sum(grade_student_lst)/len(grade_student_lst)
        return avg

    def count(self):
        self.f = open(self.add, 'r+')
        self.lines = self.f.readlines()
        return len(self.lines)


    def save(self, grade): 
            self.f.write(f"\n{grade}")
    

# file  = "all_grades.txt"
# x = CourseUtil()
# x.set_file(file)
# x.load(3)