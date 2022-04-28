from dataclasses import dataclass
@dataclass
class Number:
    value: dict

    def __repr__(self):
        if self.value['constant'] % 1 == 0.0 and self.value['constant'] != 0.0:
            result = str(int(self.value['constant']))
        else:
            result = str(self.value['constant']) if self.value['constant'] != 0.0 else ''
        for variable in self.value['variables']:
            if variable['coef'] != 0:
                if variable['coef'] == 1:
                    result += ' + '
                elif variable['coef'] == -1:
                    result += ' - '
                else:
                    result += ' + ' + str(variable['coef']) if (variable['coef'] >= 0) else ' - ' + str(variable['coef']*-1)
                for x in variable["name"]:
                    result += f'{x}^' + str(variable['variable'][x]) if variable['variable'][x] != 1 else x

        if result.startswith(" + "):
            return result[3:]
        return result

    def generate_latex(self):
        latex = ''
        if self.value['constant'] % 1 == 0.0 and self.value['constant'] != 0.0:
            latex = str(int(self.value['constant']))
        else:
            latex = str(self.value['constant']) if self.value['constant'] != 0.0 else ''

        for variable in self.value['variables']:
            if variable['coef'] != 0:
                if variable['coef'] == 1:
                    latex += ' + '
                elif variable['coef'] == -1:
                    latex += ' - '
                else:
                    latex += ' + ' + str(variable['coef']) if (variable['coef'] >= 0) else ' - ' + str(variable['coef']*-1)
                for x in variable["name"]:
                    if x != variable["name"][-1]:
                        latex += x+'^{' + str(variable['variable'][x]) + '}*' if variable['variable'][x] != 1 else x + '*'
                    else:
                        latex += x+'^{' + str(variable['variable'][x]) + '}' if variable['variable'][x] != 1 else x

        return latex