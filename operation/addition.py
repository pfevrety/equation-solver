from operation.utils.get_name import get_name
from operation.utils.is_the_same import is_the_same

from values import Number
def linear(node_a, node_b):
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
        
    tmp = {'constant': node_a['constant'] + node_b['constant'], 'variables': []}
    for i in commun_variables:
        tmp['variables'].append({'name': get_name(i[0]['variable']), 'coef': i[0]['coef'] + i[1]['coef'],'variable': i[0]['variable']})
    for i in _commun_variables:
        tmp['variables'].append(i)

    return Number(tmp)


def derivate(node_a, node_b):
    pass