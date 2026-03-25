class Note:
    def __init__(self, matiere: str, valeur: float):
        self.matiere = matiere
        self.valeur = valeur

    def __repr__(self):
        return f'Note(matiere={self.matiere}, valeur={self.valeur})'


class Student:
    def __init__(self, name: str):
        self.name = name
        self.notes = []

    def add_note(self, note: Note):
        self.notes.append(note)

    def moyenne(self):
        if not self.notes:
            return 0
        return sum(n.valeur for n in self.notes) / len(self.notes)

    def __repr__(self):
        return f'Student(name={self.name}, moyenne={self.moyenne():.2f})'


class Classe:
    def __init__(self):
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)

    def rank_by_matiere(self, matiere: str):
        return sorted(
            self.students,
            key=lambda s: next((n.valeur for n in s.notes if n.matiere == matiere), 0),
            reverse=True
        )

    def display_ranking(self, matiere: str):
        print(f'\n--- Classement par {matiere} ---')
        for student in self.rank_by_matiere(matiere):
            note = next((n.valeur for n in student.notes if n.matiere == matiere), 0)
            print(f'{student.name} : {note} (moyenne générale: {student.moyenne():.2f})')


if __name__ == '__main__':
    classe = Classe()

    alice = Student('Alice')
    alice.add_note(Note('Maths', 18))
    alice.add_note(Note('Anglais', 14))
    alice.add_note(Note('Python', 16))

    bob = Student('Bob')
    bob.add_note(Note('Maths', 12))
    bob.add_note(Note('Anglais', 17))
    bob.add_note(Note('Python', 15))

    charlie = Student('Charlie')
    charlie.add_note(Note('Maths', 15))
    charlie.add_note(Note('Anglais', 11))
    charlie.add_note(Note('Python', 19))

    classe.add_student(alice)
    classe.add_student(bob)
    classe.add_student(charlie)

    classe.display_ranking('Maths')
    classe.display_ranking('Anglais')
    classe.display_ranking('Python')