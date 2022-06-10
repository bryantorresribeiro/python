from models.empresa import Empresa
from models.funcionario import Funcionario
from models.gerente import Gerente
from helper import save_to_database

if __name__ == "__main__":
    empresa = Empresa("Kenzie", "00.111.222.333")
    funcionario = Funcionario("jordan cardoso poole ", "32112343215")
    funcionario2 = Funcionario("jordan cardoso poole ", "22112343215")
    empresa.contratar_funcionario(funcionario)
    empresa.gerar_holerite(funcionario, save_to_database)
    gerente = Gerente("jordan", "32112343215")
    print(gerente.adicionar_funcionario(funcionario2))
