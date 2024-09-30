import datetime
import random
from collections import OrderedDict

from faker import Faker

fake = Faker(['ru_RU'])
fake.seed_locale('ru_RU', 0)

table_name = 'dog'
column_names = ('dog_num', 'id_obj', 'id_manager', 'id_client', 'date_cdt', 'date_mdt', 'date_sdt', 'arcf')
rows = 5000
filename = f'{table_name}.sql'

with open(filename, 'w') as f:
    columns_str = ', '.join(f"{column}" for column in column_names)
    for i in range(rows):
        project_code = fake.random_choices(
            elements=OrderedDict(
                [('ГЛ', 0.8), ('К', 0.7), ('К4', 0.6), ('ЛГ', 0.5), ('М2', 0.4), ('Но', 0.3), ('П', 0.2), ('ПД', 0.15),
                 ('ПуД', 0.1), ('ЭН', 0.05), ('ЮК', 0.1), ('D', 0.1), ('iL', 0.1)]),
            length=1)
        id_obj = fake.random_int(min=1, max=1000)
        preffix = f'{project_code[0]}-{id_obj}'
        dog_num = fake.bothify(text=preffix + '-########')
        id_manager = fake.random_int(min=1, max=100)
        id_client = fake.random_int(min=1, max=400)

        start_date = datetime.date(2010, 1, 1)
        end_date = datetime.date(2024, 9, 30)
        random_date = start_date + datetime.timedelta(days=random.randint(0, (end_date - start_date).days))

        date_cdt = f"'{random_date.strftime('%Y-%m-%d')}'"
        date_mdt = f"'{random_date.strftime('%Y-%m-%d')}'"
        date_sdt = f"'{random_date.strftime('%Y-%m-%d')}'"

        arcf = fake.boolean()

        values = [f"'{dog_num}'", id_obj, id_manager, id_client, date_cdt, date_mdt, date_sdt, arcf]
        values_str = ', '.join(str(value) for value in values)

        insert_query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({values_str});\n"
        # print(insert_query)
        f.write(insert_query)
    f.close()
