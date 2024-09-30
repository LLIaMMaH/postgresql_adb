from faker import Faker

fake = Faker(['ru_RU'])
fake.seed_locale('ru_RU', 0)

table_name = 'person'
column_names = ('fname', 'lname', 'mname', 'phone_1', 'phone_2', 'email', 'arcf')
rows = 500
filename = f'{table_name}.sql'

with open(filename, 'w') as f:
    columns_str = ', '.join(f"{column}" for column in column_names)
    for i in range(rows):
        person = fake['ru_RU'].name()
        person_part = person.split()
        phone_1 = f"'{fake['ru_RU'].phone_number()}'"
        phone_2 = f"'{fake['ru_RU'].phone_number()}'"
        email = f"'{fake.email()}'"
        actf = fake.boolean()

        values = [f"'{person_part[0]}'", f"'{person_part[1]}'", f"'{person_part[2]}'", phone_1, phone_2, email, actf]
        values_str = ', '.join(str(value) for value in values)

        insert_query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({values_str});\n"
        # print(insert_query)
        f.write(insert_query)
    f.close()
