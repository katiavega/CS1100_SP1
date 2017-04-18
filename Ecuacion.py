#Sabiendo que la Discriminante es B**2 -4AC
import math
A = float(input())
B = float(input())
C = float(input())
discriminante = +B**2 - 4*A*C
#print(discriminante)
if discriminante > 0:
    raiz1 = int((-B + math.sqrt(discriminante))/(2*A))
    raiz2 = int((-B - math.sqrt(discriminante))/(2*A))
    print(raiz1)
    print(raiz2 )
else:
    print ("Raíces imaginarias")
