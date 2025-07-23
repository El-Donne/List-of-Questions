# Salário de até 280: aumento de 20%
# 280-700: 15%
# 700-1500: 10%
# 1500<: 5%
# Informar salário antes do reajuste, aumento aplicado, valor do aumento, salário com aumento.

print("Inicialização concluída com sucesso.")
print("BEM-VINDO AO TABAJARA SYSTEM!")
collaborator_sallary = int(input("INSIRA O SEU SALÁRIO ABAIXO:\n"))

if (collaborator_sallary <= 280):
    print(f'Salário antes do reajuste: {collaborator_sallary}')
    percentual = 0.2
    print(f'Reajuste salarial: {percentual*100}%')
    reajuste_salarial = collaborator_sallary * percentual
    print(f'Valor aplicado: {reajuste_salarial}')
    new_sallary = collaborator_sallary + reajuste_salarial
    print(f'Novo salário: {new_sallary}')
elif (280 < collaborator_sallary <= 700):
    print(f'Salário antes do reajuste: {collaborator_sallary}')
    percentual = 0.15
    print(f'Reajuste salarial: {percentual*100}%')
    reajuste_salarial = collaborator_sallary * percentual
    print(f'Valor aplicado: {reajuste_salarial}')
    new_sallary = collaborator_sallary + reajuste_salarial
    print(f'Novo salário: {new_sallary}')
elif (700 < collaborator_sallary <= 1500):
    print(f'Salário antes do reajuste: {collaborator_sallary}')
    percentual = 0.1
    print(f'Reajuste salarial: {percentual*100}%')
    reajuste_salarial = collaborator_sallary * percentual
    print(f'Valor aplicado: {reajuste_salarial}')
    new_sallary = collaborator_sallary + reajuste_salarial
    print(f'Novo salário: {new_sallary}')
elif (collaborator_sallary > 1500):
    print(f'Salário antes do reajuste: {collaborator_sallary}')
    percentual = 0.05
    print(f'Reajuste salarial: {percentual*100}%')
    reajuste_salarial = collaborator_sallary * percentual
    print(f'Valor aplicado: {reajuste_salarial}')
    new_sallary = collaborator_sallary + reajuste_salarial
    print(f'Novo salário: {new_sallary}')
else:
    print('[ERRO]')