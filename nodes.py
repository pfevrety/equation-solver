from dataclasses import dataclass


@dataclass
class NumberNode:
    value: dict
    # def __repr__(self):
    #     if self.value['variables'] is None:
    #         return f"{self.value['constant']}"
    #     elif self.value['constant'] == 0:
    #         result = ""
    #         for i in self.value['variables']:
    #             print(i['coef'])
    #             result += str(i['coef']) if i['coef'] != 0 else ''
    #             for x in i["name"]:
    #                 result += f'{x}^' + str(i['variable'][x]) if i['variable'][x] != 1 else x
    #         return result
    #     else:
    #         result = str(self.value['constant']) + ' '
    #         for i in self.value['variables']:
    #             result += str(i['coef']) if i['coef'] != 1 else ''
    #             for x in i["name"]:
    #                 result += f'{x}^' + str(i['variable'][x]) if i['variable'][x] != 1 else x
    #         return result

    def __repr__(self):
        if self.value['variables'] is None:
            return f"{self.value['constant']}"
        result = str(self.value['constant']) + ' + ' if self.value['constant'] != 0.0 else ''
        for index, variable in enumerate(self.value['variables']):
            result += ' + ' + str(variable['coef']) if (variable['coef'] != 1) else ''
            for x in variable["name"]:
                result += f'{x}^' + str(variable['variable'][x]) + '+' if variable['variable'][x] != 1 else x + '+' if index < len(self.value['variables']) - 1 else x
        return result



@dataclass
class AddNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}+{self.node_b})"


@dataclass
class SubtractNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}-{self.node_b})"


@dataclass
class MultiplyNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}*{self.node_b})"


@dataclass
class DivideNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}/{self.node_b})"


@dataclass
class PlusNode:
    node: any

    def __repr__(self):
        return f"(+{self.node})"


@dataclass
class MinusNode:
    node: any

    def __repr__(self):
        return f"(-{self.node})"
