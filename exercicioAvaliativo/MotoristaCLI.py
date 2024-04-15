from MotoristaDAO import MotoristaDAO


class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class MotoristaCLI(SimpleCLI):
    def __init__(self, motoristaDAO: MotoristaDAO):
        super().__init__()
        self.motoristaDAO = motoristaDAO
        self.add_command("create", self.create_motorista)
        self.add_command("read", self.read_motorista)
        self.add_command("update", self.update_motorista)
        self.add_command("delete", self.delete_motorista)

    def create_motorista(self):
        name = input("Enter the name: ")
        nota = int(input("Enter the nota: "))

        corridas = []
        while True:
            nota_corrida = int(input("Enter the nota: "))
            distancia = float(input("Enter the distance: "))
            valor = float(input("Enter the value: "))
            nome_passageiro = input("Enter passenger name: ")
            documento_passageiro = input("Enter the passenger document: ")

            passageiro = {"nome": nome_passageiro, "documento": documento_passageiro}
            corrida = {"nota": nota_corrida, "distancia": distancia, "valor": valor, "passageiro": passageiro}
            corridas.append(corrida)

            add_corrida = input("Do you want to add another race? (y/n): ")
            if add_corrida.lower() != "s":
                break

        motorista = {"nome": name, "nota": nota, "corridas": corridas}

        self.motorista_dao.criar_motorista(motorista)


    def read_motorista(self):
        id = input("Enter the id: ")
        motorista = self.motoristaDAO.read_motorista(id)
        if motorista:
            print(f"Name: {motorista['name']}")
            print(f"Grade: {motorista['nota']}")


    def update_motorista(self):
        id = input("Enter the id: ")
        name = input("Enter the new name: ")
        nota = int(input("Enter the new nota: "))
        self.motoristaDAO.update_motorista(id, name, nota)


    def delete_motorista(self):
        id = input("Enter the id: ")
        self.motoristaDAO.delete_motorista(id)


    def run(self):
        print("Welcome to the motorista CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()
        