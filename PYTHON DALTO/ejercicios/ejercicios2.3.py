#ejecutando una función  Fibonacci

def fibonacci (num):
    a,b = 0,1
    fibonacci_lisa = []
    for i in range (num):
        if b > num: return fibonacci_lisa
        else: 
            fibonacci_lisa.append(b)
            a,b= b, a+b #aqui estoy desempaquetando a= b y b = a+b

resultado = fibonacci(20)
print(resultado)
        