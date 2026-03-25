from collections.abc import Iterable, Iterator


def add_matter_4(cls):
    original_init = cls.__init__

    def new_init(self, name: str, note1: float, note2: float, note3: float, note4: float = 0):
        original_init(self, name, note1, note2, note3)
        self.notes.append(note4)

    cls.__init__ = new_init
    return cls


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


class StudentIteratorMatter2(Iterator):

    def __init__(self, students: list):
        self.__students = sorted(students, key=lambda s: s.notes[1], reverse=True)
        self.__index = 0

    def __next__(self):
        if self.__index >= len(self.__students):
            raise StopIteration
        student = self.__students[self.__index]
        self.__index += 1
        return student


class StudentIteratorMatter3(Iterator):

    def __init__(self, students: list):
        self.__students = sorted(students, key=lambda s: s.notes[2], reverse=True)
        self.__index = 0

    def __next__(self):
        if self.__index >= len(self.__students):
            raise StopIteration
        student = self.__students[self.__index]
        self.__index += 1
        return student


class StudentIteratorMatter4(Iterator):

    def __init__(self, students: list):
        self.__students = sorted(students, key=lambda s: s.notes[3], reverse=True)
        self.__index = 0

    def __next__(self):
        if self.__index >= len(self.__students):
            raise StopIteration
        student = self.__students[self.__index]
        self.__index += 1
        return student


@add_matter_4
class Student:
    def __init__(self, name: str, note1: float, note2: float, note3: float):
        self.name = name
        self.notes = [note1, note2, note3]

    def moyenne(self):
        return sum(self.notes) / len(self.notes)

    def __repr__(self):
        return f'Student(name={self.name}, moyenne={self.moyenne():.2f})'


class SchoolClass(Iterable):
    def __init__(self):
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)

    def __iter__(self):
        return StudentIterator(self.students, index=0)

    def iter_matter_2(self):
        return StudentIteratorMatter2(self.students)

    def iter_matter_3(self):
        return StudentIteratorMatter3(self.students)

    def iter_matter_4(self):
        return StudentIteratorMatter4(self.students)

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

    def rank_matter_4(self):
        print(f'\n--- Classement décroissant par Matiere 4 ---')
        ranked = sorted(self.students, key=lambda s: s.notes[3], reverse=True)
        for student in ranked:
            print(f'{student.name} : {student.notes[3]} (moyenne: {student.moyenne():.2f})')


if __name__ == '__main__':
    school_class = SchoolClass()
    school_class.add_student(Student('J', 10, 12, 13, 15))
    school_class.add_student(Student('A', 8, 2, 17, 11))
    school_class.add_student(Student('V', 9, 14, 14, 7))

    school_class.display_ranking('Matiere 1', 0)
    school_class.display_ranking('Matiere 2', 1)
    school_class.display_ranking('Matiere 3', 2)
    school_class.display_ranking('Matiere 4', 3)

    school_class.rank_matter_1()
    school_class.rank_matter_2()
    school_class.rank_matter_3()
    school_class.rank_matter_4()

    print('\n--- Iteration sur Matiere 1 ---')
    for student in school_class:
        print(f'{student.name} : {student.notes[0]} (moyenne: {student.moyenne():.2f})')

    print('\n--- Iteration sur Matiere 2 ---')
    for student in school_class.iter_matter_2():
        print(f'{student.name} : {student.notes[1]} (moyenne: {student.moyenne():.2f})')

    print('\n--- Iteration sur Matiere 3 ---')
    for student in school_class.iter_matter_3():
        print(f'{student.name} : {student.notes[2]} (moyenne: {student.moyenne():.2f})')

    print('\n--- Iteration sur Matiere 4 ---')
    for student in school_class.iter_matter_4():
        print(f'{student.name} : {student.notes[3]} (moyenne: {student.moyenne():.2f})')