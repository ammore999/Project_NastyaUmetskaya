class Student:

    def __init__(self, name, surname, grades):
        self.name = name
        self.surname = surname
        self.grades = grades

    def get_average(self):
        srednee = sum(self.grades) / len(self.grades)
        return srednee

    def is_excellent(self):
        if self.get_average() >= 4.5:
            return True
        else:
            return False



st = Student("Иван", "Иванов", [5, 5, 4, 5])

print("Студент:", st.name, st.surname)
print("Средний балл:", st.get_average())
print("Отличник?:", st.is_excellent())
