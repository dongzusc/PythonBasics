class Student:
    def __init__(self, name, major, age, gpa, is_registered):
        self.name = name
        self.age = age
        self.gpa = gpa
        self.is_registered = is_registered
        
    def is_good(self):
        if self.gpa >=3.5:
            return True
        else:
            return False
    
    def year(self):
        if self.age == 18:
            return 1
        elif self.age == 19:
            return 2
        elif self.age == 20:
            return 3
        elif self.age < 18:
            return 0
        elif self.age == 21:
            return 4
        else:
            return 5
        
        
class Questions:
    def __init__(self, question_prompt, answer):
        self.question_prompt = question_prompt
        self.answer = answer
    
class Chef:
    def make_chicken(self):
        print("The chef makes you a chicken.")
        
    def make_salad(self):
        print("The chef makes you a salad.")
        
    def make_special(self):
        print("The chef makes you a lobster.")

class ChineseChef(Chef): # inheritance
    def make_special(self): # overwrite
        print("The chef makes you a fish soup.")
    def make_rice(self):
        print("The chef makes you a bowl of rice.")
    




        
        
        
        
        