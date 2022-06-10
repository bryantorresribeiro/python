class Empresa():

    @staticmethod
    def format_name(name):
        format = name.title().split()
        return  " ".join(format) 
    
    @staticmethod
    def format_name_dunde(name):
        format = name.lower().split()
        return  "_".join(format) 
    
    contratados = []

    def __init__(self, nome:str, cnpj:str):
        self.nome = self.format_name(nome)
        self.cnpj = cnpj
        self.contratados = Empresa.contratados
    def __len__(self):
        return len(self.contratados)
    
    def contratar_funcionario(self, funcionario):

        for funcionarios in self.contratados:
            if funcionarios.get("cpf") == funcionario.cpf:
                return "Funcionário com esse CPF já foi contratado"

        name = self.format_name_dunde(funcionario.nome)
        email = f'{name}@{self.nome.lower()}.gmail.com'
        empresa = self.nome

        Empresa.contratados.append(({**vars(funcionario), "email":email, "empresa":empresa}))
    
    def gerar_holerite(self, cadastrar_usuario, func_salvar):

        nome = self.format_name_dunde(cadastrar_usuario.nome)
        empresa = f"_{self.nome}_"

        for funcionarios in self.contratados:
            if funcionarios.get("nome") == cadastrar_usuario.nome:
                func_salvar(vars(cadastrar_usuario), empresa, nome)
                return True
        
        return False