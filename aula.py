class aula:
    def __init__(self,professor,assunto):
        self.professor = professor
        self.assunto = assunto
        self.alunos = []

    def adicionar_aluno(self,aluno):
        self.alunos.append(aluno)

    def listar_presenca(self):
        listaAlunos = ", ".join([aluno.nome for aluno in self.alunos])
        print(f'Presença na aula sobre {self.assunto}, ministrada pelo professor {self.professor.nome}:\n{listaAlunos}')