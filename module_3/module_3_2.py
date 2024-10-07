def send_email(recipient, sender='university.help@gmail.com'):
    valid_domains = [".com",".ru",".net"]
    if "@" not in recipient or not any (recipient.endswith(domain) for domain in valid_domains):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    if "@" not in sender or not any(sender.endswith(domain) for domain in valid_domains):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    if sender == recipient:
        print("Нельзя отправить самому себе!")
        return
    if sender == "univercity.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")

send_email('неправильный домен','urban1337@gmail.com',)
send_email('university.help@gmail.com', 'university.help@gmail.com')
send_email('urban1337@mail.ru','univercity.help@gmail.com')
send_email('univercity.help@gmail.com', 'babayaga@gmail.com')
