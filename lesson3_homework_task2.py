# имя, фамилия, год рождения, город проживания, email, телефон
def personal_details(name, surname, year_of_birth, town, email, phone_number):
    str = ' '.join([name, surname, year_of_birth, town, email, phone_number])
    print(str)


personal_details('Elle', 'McPheurson', '1980', 'Melbourne', 'elm@yahoo.com', '+55777888999')
