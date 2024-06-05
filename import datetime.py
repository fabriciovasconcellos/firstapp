import datetime

def calcular_horas(E1, S1, E2):
    # Converter as strings de hora para objetos datetime
    formato_hora = "%H:%M"
    entrada1 = datetime.datetime.strptime(E1, formato_hora)
    saida1 = datetime.datetime.strptime(S1, formato_hora)
    entrada2 = datetime.datetime.strptime(E2, formato_hora)

    # Calcular o intervalo entre E1 e S1
    intervalo1 = saida1 - entrada1

    # Calcular a hora de saída 2 considerando um total de 8 horas
    intervalo2 = datetime.timedelta(hours=8) - intervalo1
    saida2 = entrada2 + intervalo2

    # Exibir os resultados
    # print(f"Intervalo entre E1 e S1: {intervalo1}")
    print(f"Entrada 1 = {E1}")
    print(f"Saída 1 = {S1}")
    print(f"Entrada 2 = {E2}")
    print(f"Saída 2 = {saida2.strftime(formato_hora)}")
    # print(f"")

# Exemplo de uso
E1 = "08:12"
S1 = "12:11"
E2 = "13:30"

calcular_horas(E1, S1, E2)