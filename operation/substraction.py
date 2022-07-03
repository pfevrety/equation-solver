from operation.utils.get_communs_variables import get_commun_variables
from operation.utils.get_name import get_name
from operation import addition
from values import Number, Variables
def linear(node_a, node_b):

    var = []
    for variable in node_b.variables:
        var.append(Variables(-variable.coef, variable.variables))

    return addition.linear(node_a, Number(-node_b.constant, var))

def derivate(node_a, node_b):
    pass