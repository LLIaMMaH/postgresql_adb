import datetime
import random

from faker import Faker

fake = Faker(['ru_RU'])
fake.seed_locale('ru_RU', 0)

table_name = 'dog_promo'
column_names = ('id_dog', 'id_promo', 'start_promo', 'end_promo', 'arcf')
rows = 5000
filename = f'{table_name}.sql'

with open(filename, 'w') as f:
    columns_str = ', '.join(f"{column}" for column in column_names)
    for i in range(rows):
        is_luck = fake.random_int(min=1, max=100)
        if is_luck > 50:
            amount_promo = fake.random_int(min=1, max=5)
            id_dog = 70 + i
            for p in range(amount_promo):
                id_promo = fake.random_int(min=1, max=50)

                start_date = datetime.date(2010, 1, 1)
                end_date = datetime.date(2024, 9, 30)
                random_date_start = start_date + datetime.timedelta(
                    days=random.randint(0, (end_date - start_date).days))
                random_date_end = random_date_start + datetime.timedelta(
                    days=random.randint(0, (end_date - start_date).days))

                start_promo = f"'{random_date_start.strftime('%Y-%m-%d')}'"
                end_promo = f"'{random_date_end.strftime('%Y-%m-%d')}'"

                arcf = fake.boolean()

                values = [id_dog, id_promo, start_promo, end_promo, arcf]
                values_str = ', '.join(str(value) for value in values)

                insert_query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({values_str});\n"
                # print(insert_query)
                f.write(insert_query)
    f.close()
