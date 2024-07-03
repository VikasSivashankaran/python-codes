is_num=lambda q:q.replace('.','',1).isdigit()
print(is_num('26.54'))
is_num1 = lambda r: is_num(r[1:]) if r[0] == '-' else is_num(r)

print(is_num1('-125.47'))