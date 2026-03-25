from collections.abc import Iterable, Iterator


class Student:
    def __init__(self, name: str, note1: float, note2: float, note3: float):
        self.name = name
        self.notes = [note1, note2, note3]

    def moyenne(self):
        return sum(self.notes) / len(self.notes)

    def __repr__(self):
        return f'Student(name={self.name}, moyenne={self.moyenne():.2f})'


class StudentIterator(Iterator):

    def __init__(self, students: list, index: int = 0):
        self.__students = sorted(students, key=lambda s: s.notes[index], reverse=True)
        self.__index = 0

    def __next__(self):
        if self.__index >= len(self.__students):
            raise StopIteration
        student = self.__students[self.__index]
        self.__index += 1
        return student


class SchoolClass(Iterable):
    def __init__(self):
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)

    def __iter__(self):
        return StudentIterator(self.students, index=0)

    def rank_by_matiere(self, index: int):
        return sorted(
            self.students,
            key=lambda s: s.notes[index],
            reverse=True
        )

    def display_ranking(self, matiere: str, index: int):
        print(f'\n--- Classement par {matiere} ---')
        for student in self.rank_by_matiere(index):
            print(f'{student.name} : {student.notes[index]} (moyenne: {student.moyenne():.2f})')

    def rank_matter_1(self):
        print(f'\n--- Classement décroissant par Matiere 1 ---')
        ranked = sorted(self.students, key=lambda s: s.notes[0], reverse=True)
        for student in ranked:
            print(f'{student.name} : {student.notes[0]} (moyenne: {student.moyenne():.2f})')

    def rank_matter_2(self):
        print(f'\n--- Classement décroissant par Matiere 2 ---')
        ranked = sorted(self.students, key=lambda s: s.notes[1], reverse=True)
        for student in ranked:
            print(f'{student.name} : {student.notes[1]} (moyenne: {student.moyenne():.2f})')

    def rank_matter_3(self):
        print(f'\n--- Classement décroissant par Matiere 3 ---')
        ranked = sorted(self.students, key=lambda s: s.notes[2], reverse=True)
        for student in ranked:
            print(f'{student.name} : {student.notes[2]} (moyenne: {student.moyenne():.2f})')


if __name__ == '__main__':
    school_class = SchoolClass()
    school_class.add_student(Student('J', 10, 12, 13))
    school_class.add_student(Student('A', 8, 2, 17))
    school_class.add_student(Student('V', 9, 14, 14))

    school_class.display_ranking('Matiere 1', 0)
    school_class.display_ranking('Matiere 2', 1)
    school_class.display_ranking('Matiere 3', 2)

    school_class.rank_matter_1()
    school_class.rank_matter_2()
    school_class.rank_matter_3()

    print('\n--- Iteration sur Matiere 1 ---')
    for student in school_class:
        print(f'{student.name} : {student.notes[0]} (moyenne: {student.moyenne():.2f})')