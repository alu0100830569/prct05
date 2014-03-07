#! /usr/bin/python
#!encoding: UTF-8
n = int (raw_input('Introduce el número de subintervalos '))
pi = 3.1415926535897931159979634685441852
suma = 0
if (n!=0):
  for i in range(1,n+1):
    a = float (i-1)/n
    b = float(i)/n
    print 'Subintervalo: (%f , %f) ' % (a, b)
    x = (i-0.5)/n
    f = 4/(1+x*x)
    suma = suma + f
    print 'Xi: %f f(Xi): %f' % (x, f)
aprox = suma / n
print 'El valor aproximado de PI es: %f' % aprox
print 'El valor de PI con 35 decimales es: %.35f' % pi

  