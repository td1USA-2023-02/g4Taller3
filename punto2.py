import pulp

problema = pulp.LpProblem("Dieta", pulp.LpMinimize)

x1 = pulp.LpVariable("Manzanas", 0, 6, pulp.LpInteger)
x2 = pulp.LpVariable("Bananos", 0, 4, pulp.LpInteger)
x3 = pulp.LpVariable("Yogurt", 0, 10, pulp.LpInteger)


problema += 0.5 * x1 + 0.4 * x2 + 1.2 * x3


problema += 50 * x1 + 89 * x2 + 150 * x3 >= 2000, "Cal"


problema += 5 * x1 + 5 * x2 + 3.4 * x3 >= 80, "Proteínas"


problema.solve()
print("Estado:", pulp.LpStatus[problema.status])
print("Cantidad de manzans que se recomienda comer:", x1.varValue)
print("Cantidad de bananos que se recomienda comer:", x2.varValue)
print("Cantidad de yogurt que se recomienda comer:", x3.varValue)
print("Costo total mínimo diario:", pulp.value(problema.objective))

