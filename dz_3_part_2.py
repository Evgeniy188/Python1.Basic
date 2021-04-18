def user_info(first_name, last_name, year_birth, city_user, email, phone_number):
    info_string = f'Фамилия - {last_name}, Имя - {first_name}, Год рождения - {year_birth}, ' \
                  f'Город проживания - {city_user}, эл. почта - {email}, телефонный номер - {phone_number}'
    return info_string


print(user_info(last_name='Петров', first_name='Иван', year_birth=1950, city_user='Москва',
                email='фыв@asd.ru', phone_number='891500000'))
