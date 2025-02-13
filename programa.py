import math

# input
print("···························")
n =int(input("Digite el valor de n: "))


# processing
S = 0
i = 1

while i<=n:
    S = S+i
    i = i+1

# output
print("················")
print("La suma de los " + str(n) + "primeros números naturales es: " + str(S))
print("················")