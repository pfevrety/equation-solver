from operation.utils.get_communs_variables import get_commun_variables
from operation.utils.get_name import get_name

from values import Number
def linear(node_a, node_b):
    commun_variables, _commun_variables = get_commun_variables(node_a, node_b)
    tmp = {'constant': node_a['constant'] - node_b['constant'], 'variables': []}

    for i in commun_variables:
        if i[0]['coef'] - i[1]['coef'] != 0:
            tmp['variables'].append({'name': get_name(i[0]['variable']), 'coef': i[0]['coef'] - i[1]['coef'],'variable': i[0]['variable']})
    for i in _commun_variables:
        tmp['variables'].append(i)

    return Number(tmp)


def derivate(node_a, node_b):
    pass