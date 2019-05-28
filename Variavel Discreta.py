from math import sqrt
from time import sleep
# ------DECLARAÇÃO DE LISTAS------
valores = list()
soma_acumulada = list()
soma_f = list()
frequencia_acumulada_relativa = list()
xifi = list()
xi_menos_xmedio_elevado_ao_quadrado_vezes_fi = list()
vareancia = list()
dms = list()
# ------DECLARAÇÃO DE VARIAVEIS------
soma = h = xmedio = 0
mostra_item = -1
print('\033[7;33m<<< Calculo de variável discreta >>>\033[m')
sleep(1.2)
oque = str(input('O que você está analisando? '))
q = int(input(f'Numero total de \033[31m{oque}\033[m: '))
for c in range(1, q + 1):
    itens = int(input(f'{c}° item: '))
    valores.append(itens)
for x in set(valores):
    soma_f.append(valores.count(x))
print('\033[4;32mDados coletados e contados.')
print('Processando os dados coletados.\033[m')
for h in range(0, 3):
    print('.', end='')
    sleep(1)
print()
print('\033[7m  \033[m'*36)
print(f'\033[1;30m{"X":<7}\033[m'
      f'\033[1;31m{"f":<5}\033[m'
      f'\033[1;32m{"fr":<5}\033[m'
      f'\033[1;33m{"F":<5}\033[m'
      f'\033[1;34m{"Fr":<5}\033[m'
      f'\033[1;35m{"xifi":<5}\033[m'
      f'\033[1;36m{"   |xi - xmedio|.fi":<10}\033[m'
      f'\033[1;37m{"   (xi - xmedio)².fi":>10}\033[m')
# esse "for" serve para fazer a SOMA ACUMULADA
for i in range(len(soma_f)):
    soma += soma_f[i]
    soma_acumulada.append(soma)
# esse "for" serve para calcular (xi - xmedio)² * f
for f in set(valores):
    xifi.append(valores.count(f) * f)
    xmedio = sum(xifi)/sum(soma_f)
# esse "for" serve para calcular vareancia
for f in set(valores):
    dmsvalores = ((f - xmedio)*valores.count(f))
    if dmsvalores < 0:
        dmsvalores *= -1
    dms.append(dmsvalores)
    vareancia.append((((f - xmedio) ** 2) * valores.count(f)))
# esse "for" serve para calcular FREQUENCIA ACUMULADA RELATIVA
for t in soma_acumulada:
    Fr = (t / sum(soma_f) * 100)
    frequencia_acumulada_relativa.append(Fr)
# esse "for" serve para mostrar os valores calculados
for f in set(valores):
    mostra_item += 1
    print(f'\033[1;30m{f:<7}\033[m'
          f'\033[1;31m{valores.count(f):<5}\033[m'
          f'\033[1;32m{(valores.count(f) / sum(soma_f)) * 100:<5.0f}\033[m'
          f'\033[1;33m{soma_acumulada[mostra_item]:<5}\033[m'
          f'\033[1;34m{frequencia_acumulada_relativa[mostra_item]:<5.0f}\033[m'
          f'\033[1;35m{valores.count(f) * f:<6}\033[m'
          f'\033[1;36m{dms[mostra_item]:>13.2f}\033[m'
          f'\033[1;37m{vareancia[mostra_item]:>18.2f}\033[m')
    sleep(0.5)
print('\033[7m  \033[m'*36)
print(f'\033[1;31mΣf = {sum(soma_f)}\033[m')
print(f'\033[7;32mValor médio de {oque} = {xmedio:.2f}\033[m')
print(f'\033[1;36mDesvio Médio Simples = {sum(dms)/sum(soma_f):.2f}\033[m')
vareanciacalculo = sum(vareancia) / sum(soma_f)
print(f'\033[1;34mVareância = {vareanciacalculo:.2f}\033[m')

print(f'\033[1;35mDesvio Padrão:\n\033[m'
      f'\033[4;30mCorresponde a 68%\n\033[m'
      f'\033[1;33m    xmedio + σ = {xmedio + sqrt(vareanciacalculo):.2f}\n\033[m'
      f'\033[1;35m    xmedio - σ = {xmedio - sqrt(vareanciacalculo):.2f}\n\033[m'
      f'\033[4;30mCorresponde a 95%\n\033[m'
      f'\033[1;33m    xmedio + 2σ = {xmedio + (2*sqrt(vareanciacalculo)):.2f}\n\033[m'
      f'\033[1;35m    xmedio - 2σ = {xmedio - (2*sqrt(vareanciacalculo)):.2f}\n\033[m'
      f'\033[4;30mCorresponde a 99%\n\033[m'
      f'\033[1;33m    xmedio + 3σ = {xmedio + (3*sqrt(vareanciacalculo)):.2f}\n\033[m'
      f'\033[1;35m    xmedio - 3σ = {xmedio - (3*sqrt(vareanciacalculo)):.2f}\033[m')
print()
print(' \033[7mInformativo\033[m')
print('\033[1;30mx = Item\033[m')
print('\033[1;31mf = quantidade de vezes que o item aparece.\033[m')
print('\033[1;32mfr = Frequencia Relativa ((f/ total de f) * 100.\033[m')
print("\033[1;33mF = Frequencia Acumulada (Σf's em sequência).\033[m")
print("\033[1;34mFr = Frequencia Acumulada Relativa ((F/ total de f) * 100).\033[m")
print("\033[1;35mxifi = Item multiplicado por qunatidade de vezes que ele aparece.\033[m")
