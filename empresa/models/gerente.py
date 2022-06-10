from models.funcionario import Funcionario
from models.empresa import Empresa
class Gerente(Funcionario):
    
    def __init__(self, nome_completo: str, cpf, salario=8000):
       
        super().__init__(nome_completo, cpf, salario)

        self.funcionarios = []

    def __len__(self):
        return len(self.funcionarios)
    
    def adicionar_funcionario(self, funcionario):

        list = [*Empresa.contratados, *self.funcionarios]

        for pessoas in list:

            if pessoas.get("cpf") == funcionario.cpf:
                return False

        self.funcionarios.append(vars(funcionario))
        return True      