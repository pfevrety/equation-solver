from values import Number


def linear(node_a, node_b):
    tmp = {'constant': node_a['constant'] * node_b['constant'], 'variables': []}
    

    # Multiplie tout par la constante a
    for variable_b in node_b['variables']:
        if variable_b['coef'] * node_a['constant'] != 0:
            tmp['variables'].append({'name': variable_b['name'], 'coef': variable_b['coef'] * node_a['constant'], 'variable': variable_b['variable']})

    
    for variable_a in node_a['variables']:
        
        if variable_a['coef'] * node_b['constant'] != 0:
            tmp['variables'].append({'name': variable_a['name'], 'coef': variable_a['coef'] * node_b['constant'], 'variable': variable_a['variable']})
        for variable_b in node_b['variables']:
            tmp1 = {'name': '', 'coef': variable_a['coef'] * variable_b['coef'], 'variable': variable_b['variable'].copy()}
            var_b = variable_b['variable'].keys()
            for var in variable_a['variable'].keys():

                if var in var_b:
                    tmp1['variable'][var] += variable_a['variable'][var]
                else:
                    tmp1['variable'][var] = variable_a['variable'][var]

            tmp1['name'] = ''.join(tmp1['variable'].keys())
            tmp['variables'].append(tmp1)



    return Number(tmp)

