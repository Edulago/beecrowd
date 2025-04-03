def converter(entrada):
    horas = entrada // 3600
    minutos = (entrada % 3600) // 60
    segundos = entrada % 60
    print(f"{horas}h {minutos}min {segundos}s")

entrada = int(input())
converter(entrada)