import scipy.optimize as sp

resultado=sp.linprog(
    [50,80], #Funcion de coste:50x_1 + 80x_2
    A_ub=[[5,2], [-10,-12]], #Coeficientes para las desigualdades
    b_ub=[20,-90], #Restricciones para las desigualdades
)

if resultado.success:
    print(f"X1:{round(resultado.x[0], 2)} horas")
    print(f"X2:{round(resultado.x[1], 2)} horas")

else:
    print("Sin solución")
    