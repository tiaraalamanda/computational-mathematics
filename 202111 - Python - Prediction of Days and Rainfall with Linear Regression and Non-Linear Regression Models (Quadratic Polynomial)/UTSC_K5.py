import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

poly_reg=PolynomialFeatures(degree = 2)

# No. 1
print("NO. 1")
# oktober 2019
print(">> OKTOBER <<")
# METODE REGRESI LINEAR SEDERHANA
print("Metode Regresi Linier Sederhana")
lm1=LinearRegression()
df1=pd.DataFrame([[65,11],[37.9,5],[37.9,29],[345.3,24],[124.8,18]])
df1.columns=['Curah Okt','Jumlah Hari Okt']
x1=df1['Curah Okt'].values[:,np.newaxis]
y1=df1['Jumlah Hari Okt'].values
lm1.fit(x1,y1)
a1=lm1.coef_
b1=lm1.intercept_
# Persamaan garis regresi
print("Persamaan garis regresi untuk jumlah hari hujan bulan Oktober:")
print("y=%.5f x + %.5f" %(a1,b1))
jhh_okt19= a1*84.2+b1
print("Prediksi jumlah hari hujan bulan Oktober 2019 adalah %i hari." %math.ceil(jhh_okt19))
# R square
r_square1=lm1.score(x1,y1)
print("R-square: ",r_square1)
# plot
plt.scatter(x1,y1, color = 'lightcoral')
plt.plot(x1, lm1.predict(x1), color = 'indigo')
plt.title("Regresi Linear Sederhana")
plt.xlabel("Curah Hujan Bulan Oktober")
plt.ylabel("Jumlah Hari Hujan Bulan Oktober")
plt.show()
print("")
# METODE REGRESI POLINOM
print("Metode Regresi Polinomial")
x_poly_okt= poly_reg.fit_transform(x1)
lm1.fit(x_poly_okt,y1)
koef=lm1.coef_
p1=koef[2]
q1=koef[1]
r1=lm1.intercept_
# Persamaan
print("Persamaan garis regresi untuk jumlah hari hujan bulan Oktober:")
print("y=%.5f x^2 + %.5fx + %.5f" %(p1,q1,r1))
jhh_okt19= p1*(84.2*84.2)+q1*(84.2)+r1
print("Prediksi jumlah hari hujan bulan Oktober 2019 adalah %i hari." %math.ceil(jhh_okt19))
# plot
max_x1=np.max(x1) + 10
min_x1=np.min(x1) - 10
x1poly=np.linspace(min_x1, max_x1,500)
ypred1=p1*(x1poly**2) + q1*x1poly + r1
plt.scatter(x1,y1, color = 'lightcoral')
plt.plot(x1poly,ypred1, color = 'indigo')
plt.title("Regresi Polinomial")
plt.xlabel("Curah Hujan Bulan Oktober")
plt.ylabel("Jumlah Hari Hujan Bulan Oktober")
plt.show()
#R Square
r_sq_pol1=lm1.score(x_poly_okt,y1)
print("R-square: ",r_sq_pol1)
print("")

# november 2019
print(">> NOVEMBER <<")
# METODE REGRESI LINIER SEDERHANA
print("Metode Regresi Linier Sederhana")
lm2=LinearRegression()
df2=pd.DataFrame([[296.5,26],[455,24],[455,30],[442.2,25],[483.2,23]])
df2.columns=['Curah Nov','Jumlah Hari Nov']
x2=df2['Curah Nov'].values[:,np.newaxis]
y2=df2['Jumlah Hari Nov'].values
lm2.fit(x2,y2)
a2=lm2.coef_
b2=lm2.intercept_
# Persamaan garis regresi
print("Persamaan garis regresi untuk jumlah hari hujan bulan November:") 
print("y=%.5f x + %.5f" %(a2,b2))
jhh_nov19=a2*270.7+b2
print("Prediksi jumlah hari hujan bulan November 2019 adalah %i hari." %math.ceil(jhh_nov19))
# R square
r_square2=lm2.score(x2,y2)
print("R-square: ",r_square2)
# plot
plt.scatter(x2,y2, color = 'lightcoral')
plt.plot(x2, lm2.predict(x2), color = 'indigo')
plt.title("Regresi Linear Sederhana")
plt.xlabel("Curah Hujan Bulan November")
plt.ylabel("Jumlah Hari Hujan Bulan November")
plt.show()
print("")
# METODE REGRESI POLINOM
print("Metode Regresi Polinomial")
x_poly_nov=poly_reg.fit_transform(x2)
lm2.fit(x_poly_nov,y2)
koef=lm2.coef_
p2=koef[2]
q2=koef[1]
r2=lm2.intercept_
# Persamaan
print("Persamaan garis regresi untuk jumlah hari hujan bulan November:")
print("y=%.5f x^2 + %.5fx + %.5f" %(p2,q2,r2))
jhh_nov19= p2*(270.7*270.7)+q2*(270.7)+r2
print("Prediksi jumlah hari hujan bulan November 2019 adalah %i hari." %math.ceil(jhh_nov19))
# plot
max_x2=np.max(x2) + 10
min_x2=np.min(x2) - 10
x2poly=np.linspace(min_x2, max_x2,500)
ypred2=p2*(x2poly**2) + q2*x2poly + r2
plt.scatter(x2,y2, color = 'lightcoral')
plt.plot(x2poly,ypred2, color = 'indigo')
plt.title("Regresi Polinomial")
plt.xlabel("Curah Hujan Bulan November")
plt.ylabel("Jumlah Hari Hujan Bulan November")
plt.show()
#R Square
r_sq_pol2=lm2.score(x_poly_nov,y2)
print("R-square: ",r_sq_pol2)
print("")

# desember 2019
print(">> DESEMBER <<")
# METODE REGRESI LINIER SEDERHANA
print("Metode Regresi Linier Sederhana")
lm3=LinearRegression()
df3=pd.DataFrame([[316.4,25],[311.5,23],[311.5,23],[129.9,20],[323.5,22]])
df3.columns=['Curah Des','Jumlah Hari Des']
x3=df3['Curah Des'].values[:,np.newaxis]
y3=df3['Jumlah Hari Des'].values
lm3.fit(x3,y3)
a3=lm3.coef_
b3=lm3.intercept_
# Persamaan garis regresi
print("Persamaan garis regresi untuk jumlah hari hujan bulan Desember:")
print("y=%.5f x + %.5f" %(a3,b3))
jhh_des19=a3*313.5+b3
print("Prediksi jumlah hari hujan bulan Desember 2019 adalah %i hari." %math.ceil(jhh_des19))
# R square
r_square3=lm3.score(x3,y3)
print("R-square: ",r_square3)
# plot
plt.scatter(x3,y3, color = 'lightcoral')
plt.plot(x3, lm3.predict(x3), color = 'indigo')
plt.title("Regresi Linear Sederhana")
plt.xlabel("Curah Hujan Bulan Desember")
plt.ylabel("Jumlah Hari Hujan Bulan Desember")
plt.show()
print("")
# METODE REGRESI POLINOM
print("Metode Regresi Polinomial")
x_poly_des=poly_reg.fit_transform(x3)
lm3.fit(x_poly_des,y3)
koef=lm3.coef_
p3=koef[2]
q3=koef[1]
r3=lm3.intercept_
# Persamaan
print("Persamaan garis regresi untuk jumlah hari hujan bulan Desember:")
print("y=%.5f x^2 + %.5fx + %.5f" %(p3,q3,r3))
jhh_des19= p3*(313.5*313.5)+q3*(313.5)+r3
print("Prediksi jumlah hari hujan bulan Desember 2019 adalah %i hari." %math.ceil(jhh_des19))
# plot
max_x3=np.max(x3) + 10
min_x3=np.min(x3) - 10
x3poly=np.linspace(min_x3, max_x3,500)
ypred3=p3*(x3poly**2) + q3*x3poly + r3
plt.scatter(x3,y3, color = 'lightcoral')
plt.plot(x3poly,ypred3, color = 'indigo')
plt.title("Regresi Polinomial")
plt.xlabel("Curah Hujan Bulan Desember")
plt.ylabel("Jumlah Hari Hujan Bulan Desember")
plt.show()
#R Square
r_sq_pol3=lm3.score(x_poly_des,y3)
print("R-square: ",r_sq_pol3)
print("")

# baca data untuk no 2 dan 3
data2=pd.read_csv('D:/MetNum/UTS KELOMPOK 5/Rata2.csv')

# No. 2
print("NO. 2")
x4=data2['Jumlah Hari Hujan'].values[:,np.newaxis]
y4=data2['Curah Hujan'].values
lm4= LinearRegression()
# METODE REGRESI LINIER SEDERHANA
print("Metode Regresi Linier Sederhana")
lm4.fit(x4,y4)
a4=lm4.coef_
b4=lm4.intercept_
# Model prediksi
print("Model prediksi curah hujan:")
print("y=%.5f x + %.5f" %(a4,b4))
# R square
r_sq_lin4=lm4.score(x4,y4)
print("R-square: ",r_sq_lin4)
# plot
plt.scatter(x4,y4, color = 'lightcoral')
plt.plot(x4,lm4.predict(x4), color = 'indigo')
plt.title("Regresi Linear Sederhana")
plt.ylabel("Curah Hujan")
plt.xlabel("Jumlah Hari Hujan")
plt.show()
print("")
# METODE REGRESI POLINOM
print("Metode Regresi Polinomial")
poly_reg=PolynomialFeatures(degree=2)
x_poly1= poly_reg.fit_transform(x4)
lm4.fit(x_poly1,y4)
koef=lm4.coef_
p4=koef[2] #x^2
q4=koef[1] #x
r4=lm4.intercept_
# Model Prediksi Curah Hujan
print("Model prediksi curah hujan:")
print("y=%.5f x^2 + %.5fx + %.5f" %(p4,q4,r4))
# R square
r_sq_pol4=lm4.score(x_poly1,y4)
print("R-square: ",r_sq_pol4)
# plot
max_x4=np.max(x4) + 10
min_x4=np.min(x4) - 10
x4poly=np.linspace(min_x4, max_x4,500)
ypred4=p4*(x4poly**2) + q4*x4poly + r4
plt.scatter(x4,y4, color = 'lightcoral')
plt.plot(x4poly,ypred4, color = 'indigo')
plt.title("Regresi Polinomial")
plt.xlabel("Jumlah Hari Hujan")
plt.ylabel("Curah Hujan")
plt.show()
print("")

# No. 3
print("NO. 3")
x5=data2['Curah Hujan'].values[:,np.newaxis]
y5=data2['Jumlah Hari Hujan'].values
lm5= LinearRegression()
# METODE REGRESI LINIER SEDERHANA
print("Metode Regresi Linier Sederhana")
lm5.fit(x5,y5)
a5=lm5.coef_
b5=lm5.intercept_
# Model prediksi
print("Model prediksi jumlah hari hujan:")
print("y=%.5f x + %.5f" %(a5,b5))
# R square
r_sq_lin5=lm5.score(x5,y5)
print("R-square: ",r_sq_lin5)
# plot
plt.scatter(x5,y5, color = 'lightcoral')
plt.plot(x5,lm5.predict(x5), color = 'indigo')
plt.title("Regresi Linear Sederhana")
plt.xlabel("Curah Hujan")
plt.ylabel("Jumlah Hari Hujan")
plt.show()
print("")
# METODE REGRESI POLINOM
print("Metode Regresi Polinomial")
poly_reg =PolynomialFeatures(degree = 2)
x_poly2=poly_reg.fit_transform(x5)
lm5.fit(x_poly2,y5)
koef=lm5.coef_
p5=koef[2]
q5=koef[1]
r5=lm5.intercept_
# Model Prediksi Jumlah Hari Hujan
print("Model prediksi jumlah hari hujan:")
print("y=%.5f x^2 + %.5fx + %.5f" %(p5,q5,r5))
# R square
r_sq_pol5=lm5.score(x_poly2,y5)
print("R-square: ",r_sq_pol5)
# plot
max_x5= np.max(x5) + 10
min_x5= np.min(x5) - 10
x5poly= np.linspace(min_x5, max_x5,500)
ypred5=p5*(x5poly**2) + q5*x5poly + r5
plt.scatter(x5,y5, color = 'lightcoral')
plt.plot(x5poly,ypred5, color = 'indigo')
plt.title("Regresi Polinomial")
plt.xlabel("Curah Hujan")
plt.ylabel("Jumlah Hari Hujan")
plt.show()

