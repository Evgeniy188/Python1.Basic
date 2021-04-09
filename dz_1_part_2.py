#### 2
seconds = int(input('Введите количество секунд для перевода в формат чч:мм:сс : '))
minutes = seconds//60
seconds = seconds%60
hours = minutes//60
minutes = minutes%60
print(f'{hours:02}:{minutes:02}:{seconds:02}')