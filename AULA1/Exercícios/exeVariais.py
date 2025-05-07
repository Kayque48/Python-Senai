#Use uma vírgula para separar as variáveis e imprimi-las
var1 = 123
var2 = "World"
print("Hello to the", var2, var1)
#Use a formatação de string usando %
var1= 123
var2= "World"
print("Hello to the %s %d", (var2, str(var1)))

#Use a formatação de string usando {}
var1= 123
var2= "World"
print("Hello to the {} {}" + var2 +  str(var1))

#Use o operador + para separar variável na declaração print
var1= 123
var2= "World"
print("Hello to the %s %d", var2, str(var1))

#Use f para formartação string
var1= 123
var2= "World"
print(f"Hello to the {var2} {var1}")