#NOTE dont forget
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
        self.address = address


        

    def load(self, line_number): 

        self.f = open(self.address, 'r+')
        self.lines = self.f.readlines()
        # print('self.lines:',self.lines) #debugger

        len_line = len(self.lines)
        if line_number <= len_line: 
            # print('len_line:',len_line) #debugger
            # print('line_number:',line_number) #debugger

            arbitary_line = self.lines[line_number - 1]
            arbitary_line_split = arbitary_line.split(' ')
            # print('result load:', arbitary_line_split) #debugger
            return (Grade(arbitary_line_split[0], arbitary_line_split[1], arbitary_line_split[2]))
            
        else:
            return None


    def calc_student_average(self, student_id):
        lst_st = []
        student_id = str(student_id)
        for line in self.lines:
            line_word = line.split(' ')[0] #return just student number
            if student_id == line_word:  
                grade = line.split(' ')[2].split("\n")[0]
                grade = float(grade)
                lst_st.append(grade)

        # print('lst_student average is :',lst_st) #debugger
        avg_st = sum(lst_st)/len(lst_st)
        return avg_st
    def calc_course_average(self, course_code):#[x]
        
        lst_co = []
        course_code = str(course_code)
        for line in self.lines: 
            line_word = line.split(' ')[1] #return just course number
            if course_code == line_word:    
                grade = line.split(' ')[2].split("\n")[0]
                grade = float(grade)
                lst_co.append(grade)
                

        # print('lst_course average is :',lst_co) #debugger
        if len(lst_co) > 0:
            avg_co = sum(lst_co) / len(lst_co)
        else:
            avg_co = 0

        return avg_co
       

    def count(self):   #[x]
        self.f = open(self.address, 'r+')
        self.lines = self.f.readlines()
        return len(self.lines)



    def save(self, grade):
            find = False
            grade_str = str(grade) 
            course_code = grade_str.split(' ')[1]
            student_code = grade_str.split(' ')[0]
            for line in self.lines:
                if line.find(student_code) != -1 and line.find(course_code) != -1:
                    find = True
            if find == False:
                self.f.write(f"\n{grade}")

# file  = "all_grades.txt"
# x = CourseUtil()
# x.set_file(file)
# print(x.calc_course_average(333))




