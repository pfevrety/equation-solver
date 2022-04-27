from operation.utils.get_communs_variables import get_commun_variables
from operation.utils.get_name import get_name
from operation import addition

from values import Number
def linear(node_a, node_b):

    tmp_node_b = {'constant': -node_b['constant'], 'variables': []}
    for variable in node_b['variables']:
        tmp_node_b['variables'].append({'name': variable['name'], 'coef': -variable['coef'], 'variable': variable['variable']})

    return addition.linear(node_a, tmp_node_b)

def derivate(node_a, node_b):
    pass