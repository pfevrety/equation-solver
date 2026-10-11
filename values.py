class Number:
    def __init__(self, constant, variables) -> None:
        self.constant = constant
        combined = {}
        for term in variables or []:
            key = tuple(sorted((name, power) for name, power in term.variables.items() if power))
            combined[key] = combined.get(key, 0) + term.coef
        self.variables = [Variables(coef, dict(key)) for key, coef in combined.items() if coef]

    def __repr__(self):
        terms = []
        if self.constant != 0 or not self.variables:
            terms.append(_format_number(self.constant))
        for variable in self.variables:
            if variable.coef == 0:
                continue
            magnitude = abs(variable.coef)
            monomial = ''.join(
                _format_atom(name) if power == 1 else f'{_format_atom(name)}^{power}'
                for name, power in sorted(variable.variables.items())
            )
            body = ('' if magnitude == 1 else _format_number(magnitude)) + monomial
            if not terms:
                terms.append(('-' if variable.coef < 0 else '') + body)
            else:
                terms.append((' - ' if variable.coef < 0 else ' + ') + body)
        return ''.join(terms) or '0'


def _format_number(value):
    return str(int(value)) if float(value).is_integer() else str(value)


def _format_atom(name):
    if name.startswith('@'):
        return name[1:]
    return name

class Variables:
    def __init__(self, coef: float | int, variables: dict) -> None:
        self.coef = coef
        self.variables = variables
        self.name = ''.join(sorted(variables.keys()))


    def __repr__(self) -> str:
        value = Number(0, [self])
        return str(value)
