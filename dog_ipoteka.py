from faker import Faker

fake = Faker(['ru_RU'])
fake.seed_locale('ru_RU', 0)

table_name = 'dog_ipoteka'
column_names = ('id_dog', 'id_ipoteka', 'arcf')
rows = 5000
filename = f'{table_name}.sql'

with open(filename, 'w') as f:
    columns_str = ', '.join(f"{column}" for column in column_names)
    for i in range(rows):
        is_luck = fake.random_int(min=1, max=100)
        if is_luck > 50:
            id_dog = 70 + i
            id_ipoteka = fake.random_int(min=1, max=10)
            arcf = fake.boolean()

            values = [id_dog, id_ipoteka, arcf]
            values_str = ', '.join(str(value) for value in values)

            insert_query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({values_str});\n"
            # print(insert_query)
            f.write(insert_query)
    f.close()
