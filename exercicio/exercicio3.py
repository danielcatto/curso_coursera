segundos_str = input("informe o numero de segundos que voce queira converter")
segundos = int(segundos_str)
hora = segundos // 3600
segundosRestantes = segundos % 3600
minutos = segundosRestantes // 60
segundos = segundosRestantes % 60
dias = hora // 24

print(dias, " dia(s), ", hora, " horas, ", minutos, " minutos ", segundos," segundos ")
