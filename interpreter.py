from nodes import *
from values import Number

class Interpreter:
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        print(method_name)
        method = getattr(self, method_name)
        
        return method(node)

    def visit_NumberNode(self, node):
        return Number(node.value)
    
    def visit_AddNode(self, node):
        print(self.visit(node.node_a).value + self.visit(node.node_b).value)
        return Number(self.visit(node.node_a).value + self.visit(node.node_b).value)
    
    def visit_SubstractNode(self, node):
        return Number(self.visit(node.node_a).value - self.visit(node.node_b).value)

    def visit_MultiplyNode(self, node):
        return Number(self.visit(node.node_a).value * self.visit(node.node_b).value)
    
    def visit_DivideNode(self, node):
        try:
            return Number(self.visit(node.node_a).value / self.visit(node.node_b).value)
        except ZeroDivisionError:
            print("Division by zero!")

    def visit_PlusNode(self, node):
        return self.visit(node.node)

    def visit_MinusNode(self, node):
        return Number(-self.visit(node.node).value)
