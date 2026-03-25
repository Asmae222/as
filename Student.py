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