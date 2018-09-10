#def suma(valor_uno, valor_dos):
 #   return valor_uno + valor_dos

#resultado = suma(10, 20)

#mi_funcion = suma
#resultado = mi_funcion(10,20)

#Las lambdas regresan algo
mi_funcion = lambda valor_uno, valor_dos : valor_uno + valor_dos

formato = lambda sentencia : '¿{}?'.format(sentencia)

no_valor = lambda : 10

no_resultado = lambda : print('Deben de ejecutar un acción')


resultado = no_resultado()

print(resultado)