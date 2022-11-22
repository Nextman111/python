# Напишите программу для. проверки истинности
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def is_bool(name):
    return input(f'Введидте {name} ')

def get_expression():
    return [is_bool('X'), is_bool('Y'), is_bool('Z')]

def check_expression(expr):
    return not(expr[0] or expr[1] or expr[2]) == \
              (not expr[0] and expr[1] and not expr[2])

print(check_expression(get_expression()))
