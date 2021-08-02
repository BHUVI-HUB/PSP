# Harmful

def apply_operation(left_operand, right_operand, operator):
if operator == '+':
return left_operand + right_operand
elif operator == '-':
return left_operand - right_operand
elif operator == '*':
return left_operand * right_operand
elif operator == '/':
return left_operand / right_operand


# Idiomatic

def apply_operation(left_operand, right_operand, operator):
import operator as op
operator_mapper = {'+': op.add, '-': op.sub,
'*': op.mul, '/': op.truediv}
return operator_mapper[operator](left_operand,
right_operand)
