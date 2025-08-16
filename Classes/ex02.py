# Calcula áreas e perímetros de figuras geométricas

class calcularArea:
    """def __init__(self, decisao):
        self.decisao = decisao"""
    def CalculadoraArea(self):
        while True:
            print('*'*50)
            print('BEM-VINDO AO CALCULADOR DE ÁREAS GEOMÉTRICAS!\nBuscamos sempre a excelência em nossos serviços! ;)')
            print('*'*50)
            self.decisao = input('Sua figura geométrica é um losângulo?\nS\tN\n').lower()
            if self.decisao == 's':
                diagMaior = float(input('Insira o valor da diagonal maior: '))
                diagMenor = float(input('Insira o valor da diagonal menor: '))
                
                areaLosangulo = (diagMaior + diagMenor)/2
                
                print(areaLosangulo)
                
                decisao2 = input('Deseja calcular outra área?\nS\tN\n').lower()
                if decisao2 == 's':
                    continue
                elif decisao2 == 'n':
                    print('Obrigado por usar o nosso programa!')
                    print('[PROGRAMA ENCERRADO]')
                    break
            else:
                base = float(input('Insira o valor da base: '))
                altura = float(input('Insira o valor da altura: '))
                option = int(input('Escolha a sua figura geométrica:\n1 - Retângulo/Quadrado/Paralelogramo\n2 - Triângulo\n3 - Trapézio\n'))
                if option == 1:
                    resultado = base*altura
                    print(resultado)
                    
                    decisao2 = input('Deseja calcular outra área?\nS\tN\n').lower()
                    if decisao2 == 's':
                        continue
                    elif decisao2 == 'n':
                        print('Obrigado por usar o nosso programa!')
                        print('[PROGRAMA ENCERRADO]')
                        break
                elif option == 2:
                    resultado = base*altura/2
                    print(resultado)
                    
                    decisao2 = input('Deseja calcular outra área?\nS\tN\n').lower()
                    if decisao2 == 's':
                        continue
                    elif decisao2 == 'n':
                        print('Obrigado por usar o nosso programa!')
                        print('[PROGRAMA ENCERRADO]')
                        break
                elif option == 3:
                    base2 = float(input('Insira o valor da outra base: '))
                    resultado = (base + base2)*altura / 2
                    print(resultado)
                    
                    decisao2 = input('Deseja calcular outra área?\nS\tN\n').lower()
                    if decisao2 == 's':
                        continue
                    elif decisao2 == 'n':
                        print('Obrigado por usar o nosso programa!')
                        print('[PROGRAMA ENCERRADO]')
                        break
                
x = calcularArea()
x.CalculadoraArea()