import smtplib
from os import getenv
from dotenv import load_dotenv


website = 'https://dvmn.org/referrals/Vh1vCBYwIFjcGLNZLI23UsXrT9O9uHpsO6FH40Hx/'
friend_name = 'Петя'
my_name = 'Артем'
email_to = 'radecki@mail.ru'
email_from = "radecki.ab@yandex.ru"
subject = 'Важно!'
mime = 'MIME-Version: 1.0'
charset = "Content-Type: text/plain; charset='utf-8'"


def make_letter(website, friend_name, my_name):
    message = f'''\
    Привет, {friend_name}! 
    {my_name} приглашает тебя на сайт {website}!
    {website} — это новая версия онлайн-курса по программированию. 
    Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

    Как будет проходить ваше обучение на {website}? 

    → Попрактикуешься на реальных кейсах. 
    Задачи от тимлидов со стажем от 10 лет в программировании.
    → Будешь учиться без стресса и бессонных ночей. 
    Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
    → Подготовишь крепкое резюме.
    Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

    Регистрируйся → {website}  
    На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.
    '''
    body = "\r\n".join((f'From: {email_from}', f'To: {email_to}',
                       f'Subject: {subject}', charset, "", message))
    letter = body.encode('utf-8')
    return letter


letter = make_letter(website, friend_name, my_name)

load_dotenv()
mail_login = getenv('LOGIN')
mail_pass = getenv('PASSWD')


def send_mail(mail_login, mail_pass, letter):
    server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
    server.login(mail_login, mail_pass)
    rezult = server.sendmail(email_from, email_to, letter)
    server.quit()
    if rezult == {}:
        print('Письмо отправлено успешно')
    else:
        print('Что-то поломалось - читайте логи')


send_mail(mail_login, mail_pass, letter)
