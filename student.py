from payment import payment 

class Student:
    reg_stds = []
    def __init__(self, name, age, paid_amount):
        self.name = name
        self.age = age
        self.paid_amount = payment(self,paid_amount)
        Student.reg_stds.append(self)
    
    @classmethod
    def get_reg_stds(cls):
        return cls.reg_stds
    
    def __str__(self):
        return f'Name: {self.name}\nAge: {self.age}\n{self.paid_amount}'

    
# std1 = Student('Isa', 23, 300)
# std2 = Student('Joe', 25, 600)
# std3 = Student('Musa', 30, 1500)
# std4 = Student('Abudu', 20, 200)

# stds = Student.get_reg_stds()
# i=0
# for std in stds:
#     print(f'Student {i+1} Details')
#     print(std,'\n')
#     i+=1