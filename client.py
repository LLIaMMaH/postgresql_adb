import random

from faker import Faker

fake = Faker(['ru_RU'])
fake.seed_locale('ru_RU', 0)

table_name = 'client'
column_names = ('id_person', 'arcf')
rows = 400
filename = f'{table_name}.sql'

with open(filename, 'w') as f:
    columns_str = ', '.join(f"{column}" for column in column_names)
    for i in range(rows):
        id_person = i+101
        actf = fake.boolean()

        values = [id_person, actf]
        values_str = ', '.join(str(value) for value in values)

        insert_query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({values_str});\n"
        # print(insert_query)
        f.write(insert_query)
    f.close()
