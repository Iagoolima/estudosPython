

n1 = int(input('digite um numero: '))
n2 = int(input('digite outro numero: '))

res = n1+n2

#true ou false
print('resultado é :', res < 10) 

#condições  -> identação, conforme abaixo, precisa-se de um espaço da mensagem para que de certo
if res > 10:
    print('numero',res,'é maior que 10') #ou print('numero %d é maior que 10'% res)
elif res > 8:
    print('numero',res,'maior que 8')   
else:
    print('numero',res,'é menor que 10')
    

if( n1 < n2):
    aux = n1
    n1 = n2
    n2 = aux
    print(' \n\nvalor do n1: %d'% n1)
    print(' valor do n2: %d'% n2)
    
    
    #repetição for & while 
    
for n in range(10): # no For a variael declarada já começa com 0 tendo esse "range" como fosse um "contar" contando 10 digitos e não até o numero 10
    print(n)
    
for n in range(5,16): #nesse caso o "n" começa a valer 5 pois eu declarei 
    print(n)
    
for n in range(10, 0, -1):# nesse caso é para contar em forma descrescente do numero 10 até o 0
    print(n)
    

x = 1
while x <=15:#em caso do while precisa declara variavel antes e explicar que precisa somar conforme linhas abaixo
    print(x)
    x=x+1
    
#teste