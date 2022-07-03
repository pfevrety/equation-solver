def is_the_same(var1, var2):
    if var1.name == var2.name:
        for var in var1.variables.keys():
            if var1.variables[var] != var2.variables[var]:
                return False
        return True
    else:
        return False
