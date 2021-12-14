class Person:
    def __init__(self, name="", address=""):
        self.name = name
        self.address = address
    
    def setName(self, name):
        self.name = name
    def setAddress(self, address):
        self.address = address
    
    def getName(self):
        return self.name
    def getAddress(self):
        return self.address

    def __str__(self):
        return f"{self.getName()}({self.getAddress()})"


class Student(Person):
    def __init__(self, name, address,):
        Person().__init__(name, address)
        self.courses = []
        self.grades = []
    
    def addCourseGrade(self, courses, grades):
        self.courses.append(courses)
        self.grades.append({courses: grades})
    
    def getAverageGrade(self):
        sumGrade = 0
        for i in range(self.courses):
            sumGrade += self.grades[self.courses.index(i)][i]
        return sumGrade / len(self.courses)
    
    def printGrades(self):
        for i in self.courses:
            print(f"Course: {i}")
            print(f"Grade: {self.grades[self.courses.index(i)][i]}")
    
    def __str__(self):
        return f"Student: {self.getName()}({self.getAddress()})"


class Teacher(Person):
    def __init__(self, name, address):
        Person().__init__(name, address)
        self.courses = []
        self.numCourses = len(self.courses)

    def getNumCourses(self):
        return self.numCourses
    
    def addCourse(self, courses):
        if courses in self.courses:
            return False
        else:
            self.courses.append(courses)
            self.numCourses = len(self.courses)
            return True
    
    def removeCourse(self, courses):
        if courses in self.courses:
            self.courses.remove(courses)
            self.numCourses = len(self.courses)
            return True
        else:
            return False
    
    def __str__(self):
        return f"Teacher: {self.name}({self.address})"