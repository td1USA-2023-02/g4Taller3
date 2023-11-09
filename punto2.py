import pulp

# Crear el problema
problema = pulp.LpProblem("Dieta", pulp.LpMinimize)

# Variables de decisión
x1 = pulp.LpVariable("Manzanas", 0, 6, pulp.LpInteger)
x2 = pulp.LpVariable("Plátanos", 0, 4, pulp.LpInteger)
x3 = pulp.LpVariable("Yogur", 0, 10, pulp.LpInteger)

# Función objetivo
problema += 0.5 * x1 + 0.4 * x2 + 1.2 * x3

# Restricciones de calorías
problema += 50 * x1 + 89 * x2 + 150 * x3 >= 2000, "Calorías"

# Restricciones de proteínas
problema += 5 * x1 + 5 * x2 + 3.4 * x3 >= 80, "Proteínas"

# Resolver el problema
problema.solve()
print("Estado:", pulp.LpStatus[problema.status])
print("Cantidad óptima de manzanas a comer por dia:", x1.varValue)
print("Cantidad óptima de plátanos a comer por dia:", x2.varValue)
print("Cantidad óptima de yogur a comer por dia:", x3.varValue)
print("Costo total mínimo diario:", pulp.value(problema.objective))

#La solución óptima sugiere que se debe consumir 6 manzanas, 4 plátanos y 9 yogures al día para satisfacer las
#necesidades nutricionales mientras se minimiza el costo total a $15.40 diarios.