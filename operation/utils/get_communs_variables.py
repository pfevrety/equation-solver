
from statistics import variance
from operation.utils.is_the_same import is_the_same


def get_commun_variables(node_a, node_b):
    node_a_variables = [variable for variable in node_a['variables']]
    node_b_variables = [variable for variable in node_b['variables']]

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
    if len(node_a_variables) > len(node_b_variables):
        for v in node_a_variables:
            is_equal = False
            for index, c in enumerate(node_b_variables):
                if is_the_same(v, c):
                    commun_variables.append([v, c])
                    node_b_variables.pop(index)
                    is_equal = True
            if not is_equal:
                _commun_variables.append(v)
    else:
        for v in node_b_variables:
            is_equal = False
            for index, c in enumerate(node_a_variables):
                print("vc",v, c, is_the_same(v, c))
                if is_the_same(v, c):
                    commun_variables.append([v, c])
                    node_b_variables.pop(index)
                    is_equal = True
            if not is_equal:
                _commun_variables.append(c)
        
    return commun_variables, _commun_variables