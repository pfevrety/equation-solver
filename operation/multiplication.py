from values import Number, Variables


def linear(node_a, node_b):
    var = []
    for variable_b in node_b.variables:
        if variable_b.coef * node_a.constant != 0:
            var.append(Variables(variable_b.coef * node_a.constant, variable_b.variables))
    
    for variable_a in node_a.variables:
        if variable_a.coef * node_b.constant != 0:
            var.append(Variables(variable_a.coef * node_b.constant, variable_a.variables))

        for variable_b in node_b.variables:
            tmp_var = variable_b.variables.copy()
            for vari, power in variable_a.variables.items():
                tmp_var[vari] = tmp_var.get(vari, 0) + power

            var.append(Variables(variable_a.coef * variable_b.coef, tmp_var))



    return Number(node_a.constant * node_b.constant, var)

