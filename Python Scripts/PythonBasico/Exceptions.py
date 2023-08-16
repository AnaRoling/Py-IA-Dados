try:
    age=int(input('Age: '))
    income=2000
    risk = income/age
    print(age)
except ZeroDivisionError:
    print('age connot be 0')
except ValueError:
    print('Invalid value')