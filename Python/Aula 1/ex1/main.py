class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def mostraInfo(self):
        print("nome: ", self.nome)

class aluno(pessoa):
    def __init__(self, nome, idade, id):
        super().__init__(nome, idade)
        self.id = id
    
    def mostraid(self):
        print("A matricula é: ", self.id)

    def mostraidade(self):
        print("Idade: ", str(self.idade))

class professor(pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    
    def mostraidade(self):
        print("idade: ", str(self.idade))


aluno = aluno("Lucas", 22, 350)
professor = professor("Renzo", 35)

print(aluno.mostraInfo())
print(aluno.mostraid())
print(professor.mostraidade())
