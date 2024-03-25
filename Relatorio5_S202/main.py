from pymongo import MongoClient
from bson.objectid import ObjectId
from LivrosModel import LivrosModel


def main():
    try:
        client = MongoClient('mongodb://localhost:27017')
        database = client["Relatorio5"]
        collection = database["Livros"]
        livrosModel = LivrosModel(collection)
        print(f"Conexão com o banco de dados estabelecida com sucesso!")
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")


# 1- Create
LivrosModel.create_livro("Clean Code", "Robert C. Martin", 2008, 31.0)
LivrosModel.create_livro("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 1997, 31.0)

# 2- Read
LivrosModel.read_book_by_id("65f7c336c5b4cc5485808f4a")

# 3- Update
LivrosModel.update_book("65f7c336c5b4cc5485808f4a", "Diário de um Banana", "Jeff Kinney", 2008, 42.1)

# 4- Delete
LivrosModel.delete_book("65f7c336c5b4cc5485808f49")
