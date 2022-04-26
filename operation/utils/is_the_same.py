def is_the_same(var1, var2):
    if var1['name'] == var2['name']:
        for var in var1['variable'].keys():
            if var1['variable'][var] != var2['variable'][var]:
                return False
        return True
    else:
        return False
