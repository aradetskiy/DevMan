from file_operations import VERSION ,render_template
from faker import Faker

fake = Faker('ru_RU')



context = {
    'first_name':fake.first_name(),
    'last_name' : 'Пупкин',
    'town' : 'Пупкино',
    'job': 'Дворник',
    'strength': 81,
    'agility' : 56,
    'endurance': 65,
    'intelligence': 45,
    'luck': 56,
    'skill_1' : 'Любит морковку',
    'skill_2' : 'Супер плевок',
    'skill_3' : 'Супер прыжок',
}
card_artem=render_template('meeting-python\\src\\charsheet.svg','meeting-python\\src\\artem_charsheet.svg',context)
