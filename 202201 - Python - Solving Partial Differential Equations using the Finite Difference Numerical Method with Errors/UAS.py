import numpy as np
import matplotlib.pyplot as plt

#Syarat awal
u_1_0 = 3
u_0 = 9

#Syarat batas
a = 0
b = 1
delta_x = 0.01
n = (b-a)/delta_x + 1

#Analitik
analitik = []

def u_x(x):
    # Buat fungsi u_x nya biar tidak perlu diketik panjang-panjang
    f_x = -np.sin(x)+4*x+9
    return f_x

for i in range(int(n)):
    analitik.append(u_x(a+i*delta_x)) 

print(analitik)

#Numerik
numerik = [u_0,u_0+u_1_0*delta_x]

def u_j_x(x,a):
    # Fungsi aproksimasi turunan kedua dengan metode beda hingga
    u_j = 2*numerik[a-1] +delta_x**2*np.sin(x)-numerik[a-2]
    return u_j

for i in range(2,int(n)):
    numerik.append(u_j_x(a+delta_x*(i-1),i)) 

print(numerik)

# Grafik
x_a = np.arange(a,b+delta_x,delta_x)
y_a = analitik

x_n = np.arange(a,b+delta_x,delta_x)
y_n = numerik

plt.plot(x_a,y_a, label ="Metode Analitik")
plt.plot(x_n,y_n, label ="Metode Numerik", linestyle ="--")
plt.xlabel('Nilai x')
plt.ylabel('Nilai u(x)')
#plt.xlim([a,b])
#plt.ylim([0,13])
plt.title('Perhitungan Secara Analitik dan Numerik')
plt.legend()
plt.show()