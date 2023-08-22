from file_operations import VERSION ,render_template
from faker import Faker
from random import randint,choice
fake = Faker('ru_RU')

skills = [
    'Стремительный прыжок',
    'Электрический выстрел',
    'Ледяной удар',
    'Стремительный удар',
    'Кислотный взгляд',
    'Тайный побег',
    'Ледяной выстрел',
    'Огненный заряд'
]

context = {
    'first_name':fake.first_name(),
    'last_name' : fake.last_name(),
    'town' : fake.city(),
    'job': fake.job(),
    'strength': randint(3,18),
    'agility' : randint(3,18),
    'endurance': randint(3,18),
    'intelligence': randint(3,18),
    'luck': randint(3,18),
    'skill_1' : choice(skills),
    'skill_2' : choice(skills),
    'skill_3' : choice(skills),
}
card_artem=render_template('meeting-python\\src\\charsheet.svg',f'meeting-python\\src\\{context["first_name"]}_{context["last_name"]}_charsheet.svg',context)
