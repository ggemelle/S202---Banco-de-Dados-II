from aluno import aluno
from professor import professor
from aula import aula

professor = professor("Lucas")
aluno1 = aluno("Maria")
aluno2 = aluno("Pedro")
aula = aula(professor, "Programação Orientada a Objetos")
aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2)
print(aula.listar_presenca())