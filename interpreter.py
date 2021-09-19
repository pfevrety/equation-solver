from nodes import *
from values import Number, Literal


class Interpreter:
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        method = getattr(self, method_name)

        return method(node)

    def visit_NumberNode(self, node):
        return Number(node.value)

    def visit_LiteralNode(self, node):
        return Literal(node.value)

    def visit_AddNode(self, node):
        node_a = self.visit(node.node_a)
        node_b = self.visit(node.node_b)

        if node_a.type() == "LITERAL" and node_b.type() == "LITERAL":
            tmp = [None, None]
            if node_a.value[0] != None and node_b.value[0] != None:
                tmp[0] = node_a.value[0] + node_b.value[0]
            elif node_a.value[0] != None:
                tmp[0] = node_a.value[0]
            else:
                tmp[1] = node_b.value[1]
            if node_a.value[1] != None or node_b.value[1] != None:
                tmp[1] = node_a.value[1] + node_b.value[1]

            return Literal(tmp)

        if node_a.type() == "LITERAL":
            tmp = [None, None]
            if node_a.value[0] != None:
                tmp[0] = node_a.value[0] + node_b.value
            else:
                tmp[0] = node_b.value
            if node_a.value[1] != None:
                tmp[1] = node_a.value[1]

            return Literal(tmp)

        if node_b.type() == "LITERAL":
            tmp = [None, None]
            if node_b.value[0] != None:
                tmp[0] = node_a.value + node_b.value[0]
            else:
                tmp[0] = node_a.value
            if node_b.value[1] != None:
                tmp[1] = node_b.value[1]

            return Literal(tmp)

        return Number(self.visit(node.node_a).value + self.visit(node.node_b).value)

    def visit_SubstractNode(self, node):
        node_a = self.visit(node.node_a)
        node_b = self.visit(node.node_b)

        if node_a.type() == "LITERAL" and node_b.type() == "LITERAL":
            tmp = [None, None]
            if node_a.value[0] != None and node_b.value[0] != None:
                tmp[0] = node_a.value[0] - node_b.value[0]
            elif node_a.value[0] != None:
                tmp[0] = node_a.value[0]
            else:
                tmp[1] = - node_b.value[1]
            if node_a.value[1] != None or node_b.value[1] != None:
                tmp[1] = node_a.value[1] - node_b.value[1]

            return Literal(tmp)

        if node_a.type() == "LITERAL":
            tmp = [None, None]
            if node_a.value[0] != None:
                tmp[0] = node_a.value[0] - node_b.value
            else:
                tmp[0] = - node_b.value
            if node_a.value[1] != None:
                tmp[1] = node_a.value[1]

            return Literal(tmp)

        if node_b.type() == "LITERAL":
            tmp = [None, None]
            if node_b.value[0] != None:
                tmp[0] = node_a.value - node_b.value[0]
            else:
                tmp[0] = node_a.value
            if node_b.value[1] != None:
                tmp[1] = - node_b.value[1]

            return Literal(tmp)

        return Number(self.visit(node.node_a).value - self.visit(node.node_b).value)

    def visit_MultiplyNode(self, node):
        return Number(self.visit(node.node_a).value - self.visit(node.node_b).value)

    def visit_DivideNode(self, node):
        try:
            return Number(self.visit(node.node_a).value / self.visit(node.node_b).value)
        except ZeroDivisionError:
            print("Division by zero!")

    def visit_PlusNode(self, node):
        return self.visit(node.node)

    def visit_MinusNode(self, node):
        return Number(-self.visit(node.node).value)
