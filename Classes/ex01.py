# Classe PESSOAIMC que recebe altura e peso e possui métodos de acesso.
# Método 'CALCULAIMC()'
# Retorna os dados da pessoa e qual sua situação

class PessoaIMC:
    def __init__(self, nome, dataNascimento, peso, altura):
        self.nome = str(nome)
        self.dataNascimento = str(dataNascimento)
        self.peso = float(peso)
        self.altura = float(altura)
        
    def dadosUusuario(self):
        print(f'DADOS DO USUÁRIO\nNome: {self.nome}\nData de nascimento: {self.dataNascimento}\nPeso: {self.peso}kg\nAltura: {self.altura}m')
        
    def calculaIMC(self):
        imc = self.peso / (self.altura**2)
        
        if 16 < imc < 16.99:
            print('Baixo peso (Grau II)')
        elif 17 < imc < 18.49:
            print('Baixo peso (Grau I)')
        elif 18.50 < imc < 24.99:
            print('Peso normal')
        elif 25 < imc < 29.99:
            print('Acima do peso')
        elif 30 < imc < 34.99:
            print('Obesidade (Grau I)')
        elif (35 < imc < 39.99):
            print('Obesidade (Grau II)')
        elif imc > 39.99:
            print('VOCÊ ESTÁ MUITO ACIMA DO PESO!')
        else:
            print('[ERRO]')
            
pessoa = PessoaIMC('Dom Henrique', '29/12/2006', 57, 1.70)
pessoa.dadosUusuario()
pessoa.calculaIMC()