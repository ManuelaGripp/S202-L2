from database import Database
from TeacherCRUD import TeacherCRUD

db = Database("bolt://34.239.121.132:7687", "neo4j", "limes-multimeters-mechanisms")

teacher_db = TeacherCRUD(db)


try:
    teacher_db.create('Chris Lima', 1956, '180.052.396-66')
except:
    print('Erro ao criar teacher')
else:
    print('Criado com sucesso')

print(teacher_db.read('Chris Lima'))

try:
    teacher_db.update('Chris Lima', '162.052.777-77')
except:
    print('Erro ao atualizar o cpf')
else:
    print('Cpf atualizado com sucesso')

print(teacher_db.read('Chris Lima'))

try:
    teacher_db.delete('Chris Lima')
except:
    print('Erro ao deletar')
else:
    print('Deletado com sucesso')

print(teacher_db.read('Chris Lima'))

# Fechando a conexão
db.close()