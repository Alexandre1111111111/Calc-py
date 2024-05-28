prmnum = int(input("Escolha o Primeiro Número:"))

operador = input("Escolha o Operador:")

segnum = int(input("Escolha o Segundo Número:"))

res = int;

if operador == "+":

    res = prmnum + segnum;

elif operador == "-":

    res = prmnum - segnum;

elif operador == "*":

    res = prmnum * segnum;

elif operador == "/":

    res = prmnum / segnum;

print(prmnum, operador, segnum, " = ", res);
