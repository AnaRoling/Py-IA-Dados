birth_year = input('Birth year:')# '1982' é diferente de 1982 
print(type(birth_year))
age = 2019 - int(birth_year) # 2019 - '1987':uma string se não tiver o Int:converte o valor para int
print(type(age))
print(age)