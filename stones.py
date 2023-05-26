import random
import requests
import pprint


def get_data_from_api(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print('Error occurred while retrieving data from the API.')
        return None


data = get_data_from_api('https://restcountries.com/v3.1/all')

random_10_countries = []
country = []

p1 = 10
p2 = 10

while p1 > 0 and p2 > 0:
    print(f'You have {p2} stone(s).\n')
    print('Computer has made a bet.')

    bet1 = random.randint(1, p1)

    while True:
        try:
            choice2 = int(input('Now please choose 1 or 2 stone(s): '))
            if choice2 != 1 and choice2 != 2:
                raise ValueError
            break
        except ValueError:
            print('Invalid input.')

    turn1 = random.randint(0, 1)
    if turn1 == 0:
        print('Computer says that you have 2 stones in your hand.')
    else:
        print('Computer says that you have 1 stone in your hand.')

    if choice2 % 2 == turn1:
        print('Computer won!')
        p2 -= bet1
        p1 += bet1
    else:
        print('You won!')
        p2 += bet1
        p1 -= bet1

    print(f'Computer bet was {bet1} stone(s)')

    if p1 > 0 and p2 > 0:
        print(f'Now you have {p2} stone(s). And Computer has {p1} stone(s)\n')
        print('Your turn...')

        while True:
            try:
                bet2 = int(input('Make your bet: '))
                if bet2 < 1 or bet2 > p2:
                    raise ValueError
                break
            except ValueError:
                print('Invalid input. You can enter number from range of stones you have.')

        while True:
            turn2_word = input('How many stones does Computer have in his hand - 1 or 2?: ')
            if turn2_word != 'Even!' and turn2_word != 'Odd!':
                print('Invalid Input.')
            else:
                break

        choice1 = random.randint(1, 2)
        turn2 = -1
        if turn2_word == 'Even!':
            turn2 = 0
        elif turn2_word == 'Odd!':
            turn2 = 1

        print(f'Computer has {choice1} stone(s) in his hand')

        if choice1 % 2 == turn2:
            print('Computer won!')
            p2 -= bet2
            p1 += bet2
        else:
            print('You won!')
            p2 += bet2
            p1 -= bet2

if p1 <= 0:
    print('Congratulations! You won the game! Here is your recipe!')
    for i in range(10):
        num = random.randint(0, 100)
        name = data[num].get('name', {}).get('common', 'N/A')
        capital = data[num].get('capital', ['N/A'])[0]
        flag = data[num].get('flag', 'N/A')
        subregion = data[num].get('subregion', 'N/A')
        population = data[num].get('population', 'N/A')
        country = [name, capital, flag, subregion, population]
        random_10_countries.append(country)
    pprint.pprint(random_10_countries)

    import psycopg2

    # Connect to the DATABASE
    connection = psycopg2.connect(
        database='countries',
        user='postgres',
        password='root',
        host='localhost',
        port='5432'
    )
    # Creating a cursor object
    cursor = connection.cursor()

    # for i in random_10_countries:
    #     save_to_table = f'''
    #     INSERT INTO countries (name, capital, flag, subregion, population)
    #     VALUES (%s, %s, %s, %s, %s)
    #     '''
    #     cursor.execute(save_to_table, i)
    # connection.commit()
    cursor.close()
    connection.close()
else:
    print('Sorry, You lost the game')