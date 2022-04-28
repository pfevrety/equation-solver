from ast import operator
from values import Number

from operation import conversion, addition, substraction, multiplication

def apply_minus(node):
    if node['variables'] is None:
        return {'constant': -node['constant'], 'variables': None}
    tmp = {'constant': -node['constant'], 'variables': []}
    for i in node['variables']:
        tmp['variables'].append({'name': i['name'], 'coef': -i['coef'], 'variable': i['variable']})
    return tmp


class Interpreter:
    def __init__(self):
        self.counter = True

    def visit(self, node):
        if type(node).__name__  == "NumberNode":
            return Number(node.value)

        elif self.counter:   
            node_a = self.visit(node.node_a).value
            node_b = self.visit(node.node_b).value

            return eval(f"{conversion.conversion[type(node).__name__]}.linear(node_a, node_b)")


    def visit_AddNode(self, node):
        
        node_a = self.visit(node.node_a).value
        node_b = self.visit(node.node_b).value
        
        commun, type = self.get_commun(node_a, node_b)
        if type == 0:
            return Number({'constant': node_a['constant'] + node_b['constant'], 'variables': None})
        elif type == 1:
            return Number({'constant': node_a['constant'] + node_b['constant'], 'variables': node_a['variables']})
        elif type == 2:
            return Number({'constant': node_a['constant'] + node_b['constant'], 'variables': node_b['variables']})
        else:
            tmp = {'constant': node_a['constant'] + node_b['constant'], 'variables': []}
            for c in commun[0]:
                tmp['variables'].append({'name': self.get_name(c[0]['variable']), 'coef': c[0]['coef'] + c[1]['coef'],
                                         'variable': c[0]['variable']})

            for nn in commun[1]:
                tmp['variables'].append(nn)

            return Number(tmp)

    def visit_SubtractNode(self, node):
        node_a = self.visit(node.node_a).value
        node_b = apply_minus(self.visit(node.node_b).value)
        commun, type = self.get_commun(node_a, node_b)

        if type == 0:

            return Number({'constant': node_a['constant'] + node_b['constant'], 'variables': None})
        elif type == 1:

            return Number({'constant': node_a['constant'] + node_b['constant'], 'variables': node_a['variables']})
        elif type == 2:
            return Number({'constant': node_a['constant'] + node_b['constant'], 'variables': node_b['variables']})
        else:
            tmp = {'constant': node_a['constant'] + node_b['constant'], 'variables': []}
            for c in commun[0]:
                tmp['variables'].append({'name': self.get_name(c[0]['variable']), 'coef': c[0]['coef'] + c[1]['coef'],
                                         'variable': c[0]['variable']})

            for nn in commun[1]:
                tmp['variables'].append(nn)
            return Number(tmp)

    def visit_MultiplyNode(self, node):
        node_a = self.visit(node.node_a).value
        node_b = apply_minus(self.visit(node.node_b).value)
        commun, type = self.get_commun(node_a, node_b, False)
        if type == 0:
            return Number({'constant': node_a['constant'] * node_b['constant'], 'variables': None})
        elif type == 1:
            return Number({'constant': node_a['constant'] * node_b['constant'], 'variables': node_a['variables']})
        elif type == 2:
            return Number({'constant': node_a['constant'] * node_b['constant'], 'variables': node_b['variables']})


        return Number(self.visit(node.node_a).value * self.visit(node.node_b).value)

    def visit_DivideNode(self, node):
        try:
            return Number(self.visit(node.node_a).value / self.visit(node.node_b).value)
        except:
            raise Exception("Runtime math error")

    def multiply(self, var, factor):
        tmp = []
        for i in var:
            tmp.append({'name': var['name'], 'coef': var['coef'] * factor, 'variable': var['variable']})
        return tmp
    def is_the_same(self, var1, var2, tx):
        if var1['name'] == var2['name']:
            if not tx:
                return True
            for var in var1['variable'].keys():
                if var1['variable'][var] != var2['variable'][var]:
                    return False
            return True
        else:
            return False

    def get_name(self, var):
        return ''.join(var.keys())

    def get_commun(self, node_a, node_b, tx=True):
        if node_a['variables'] is None and node_b['variables'] is None:
            return None, 0
        elif node_a['variables'] is not None and node_b['variables'] is None:
            return None, 1
        elif node_a['variables'] is None and node_b['variables'] is not None:
            return None, 2

        var_1 = [variable for variable in node_a['variables']]
        var_2 = [variable for variable in node_b['variables']]
        same = []
        not_same = []
        for v in var_1:
            is_equal = False
            for index, c in enumerate(var_2):
                if self.is_the_same(v, c, tx):
                    same.append((v, c))
                    var_2.pop(index)
                    is_equal = True
            if not is_equal:
                not_same.append(v)

        return (same, not_same + var_2), 3
