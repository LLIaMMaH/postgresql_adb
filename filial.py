from faker import Faker

fake = Faker(['ru_RU'])
fake.seed_locale('ru_RU', 0)

table_name = 'filial'
column_names = ('name_filial', 'arcf')
rows = 20
filename = f'{table_name}.sql'

with open(filename, 'w') as f:
    columns_str = ', '.join(f"{column}" for column in column_names)
    for i in range(rows):
        name_filial = f"'{fake.company()}'"
        actf = fake.boolean()

        values = [name_filial, actf]
        values_str = ', '.join(str(value) for value in values)

        insert_query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({values_str});\n"
        # print(insert_query)
        f.write(insert_query)
