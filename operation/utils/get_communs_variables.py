
from statistics import variance
from operation.utils.is_the_same import is_the_same


def get_commun_variables(node_a, node_b):
    
    variables = [variable for variable in node_a['variables']] + [variable for variable in node_b['variables']]

    commun_variables = []
    _commun_variables = []

    while len(variables) > 0:
        variable_testing = variables[0]
        tmp = [variable_testing]
        equal = False
        for i in range(1, len(variables)):
            if is_the_same(variables[i], variable_testing):
                tmp.append(variables[i])
                variables.pop(i)
                equal = True
        if not equal:
            _commun_variables.append(variable_testing)
        else:
            commun_variables.append(tmp)
        variables.pop(0)
    
    return commun_variables, _commun_variables