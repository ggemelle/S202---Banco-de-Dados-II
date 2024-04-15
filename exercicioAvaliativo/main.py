from database import Database
from MotoristaCLI import MotoristaCLI
from MotoristaDAO import MotoristaDAO

def main():
    
    db = Database("ExercicioAV", "Motoristas")
    motoristaDAO = MotoristaDAO("ExercicioAV", "Motoristas")

    motoristaCLI = MotoristaCLI(motoristaDAO)

    motoristaCLI.run()