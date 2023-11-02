from gurobipy import*


def print_hi():
    m = Model("Furniture Problem")
    x1 = m.addVar(name="chairs")
    x2 = m.addVar(name="tables")
    m.setObjective(45*x1+80*x2,GRB.MAXIMIZE)
    con1 = m.addConstr(5 * x1 + 20 * x2 <= 400, "wood_cons")
    con2 = m.addConstr(10 * x1 + 15 * x2 <= 450, "labor_cons")
    m.optimize()
    for v in m.getVars():
        print(v.varName, v.x)
    print("Revenue = $", m.objVal)

print_hi()



