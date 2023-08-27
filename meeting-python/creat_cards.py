from file_operations import render_template
from faker import Faker
from random import randint,sample
from codecs import open

def make_card_npc():
    fake = Faker('ru_RU')
    
    file = open('meeting-python\src\skills.txt','r','utf-8',)
    file_skills = file.readlines()
    file.close()
    skills = []
    for line in file_skills:
        skills.append(line) 
    npc_skills = sample(skills,3)
    
    context = {
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'job': fake.job(),
        'town': fake.city(),
        'strength' : randint(3,18),
        'agility' : randint(3,18),
        'endurance' : randint(3,18),
        'intelligence' : randint(3,18),
        'luck' : randint(3,18),
        'skill_1': npc_skills[0],
        'skill_2': npc_skills[1],
        'skill_3': npc_skills[2]
    }
    
    

    
    
    render_template('meeting-python\src\charsheet.svg',
                    f'meeting-python\Repl\\{context["first_name"]}_{context["last_name"]}.svg', context)


def main():
    make_card_npc()


if __name__ == '__main__':
    main()
