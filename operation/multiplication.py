from values import Number, Variables


def linear(node_a, node_b):
    var = []
    # Multiplie tout par la constante a
    for variable_b in node_b.variables:
        if variable_b.coef * node_a.constant != 0:
            var.append(Variables(variable_b.coef * node_a.constant, variable_b.variables))
    
    for variable_a in node_a.variables:
        
        if variable_a.coef * node_b.constant != 0:
            var.append(Variables(variable_b.coef * node_a.constant, variable_a.variables))

        for variable_b in node_b.variables:
            print(variable_b.__dict__)
            tmp_var = variable_b.variables.copy()
            var_b = variable_b.variables.keys()
            for vari in variable_a.variables.keys():

                if vari in var_b:
                    tmp_var[vari] += variable_a.variables[vari]
                else:
                    tmp_var[vari] = variable_a.variables[vari]

            var.append(Variables(variable_a.coef * variable_b.coef, tmp_var))



    return Number(node_a.constant * node_b.constant, var)

