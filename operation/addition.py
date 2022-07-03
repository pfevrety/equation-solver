from operation.utils.get_name import get_name
from operation.utils.is_the_same import is_the_same

from values import Number, Variables
def linear(node_a, node_b):
    variables = [variable for variable in node_a.variables] + [variable for variable in node_b.variables]

    commun_variables = []
    _commun_variables = []

    while len(variables) > 0:
        variable_testing = variables[0]
        tmp = [variable_testing]
        equal = False
        counter = 1
        max1 = len(variables)
        while counter < max1:
            if len(variables) > 0:
                if is_the_same(variables[counter], variable_testing):
                    tmp.append(variables[counter])
                    variables.pop(counter)
                    max1 -= 1
                    equal = True
                counter += 1
        if not equal:
            _commun_variables.append(variable_testing)
        else:
            commun_variables.append(tmp)
        variables.pop(0)

    var = []
    for i in commun_variables:
        coef = 0 
        for y in i:
            coef += float(y.coef)
        var.append(Variables(coef, i[0].variables))

    for i in _commun_variables:
        var.append(Variables(i.coef, i.variables))

    if var is None:
        var = []
    return Number(node_a.constant + node_b.constant, var)


def derivate(node_a, node_b):
    pass