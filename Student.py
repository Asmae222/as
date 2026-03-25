class Student:
    def __init__(self, name: str, note1: float, note2: float, note3: float):
        self.name = name
        self.notes = [note1, note2, note3]

    def moyenne(self):
        return sum(self.notes) / len(self.notes)

    def __repr__(self):
        return f'Student(name={self.name}, moyenne={self.moyenne():.2f})'


class SchoolClass:
    def __init__(self):
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)

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