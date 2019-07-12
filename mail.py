import imaplib
import pprint

mail = imaplib.IMAP4_SSL('imap.yandex.ru')
mail.login('soti-asso@yandex.ru', 'sotiasso')
mail.list()

mail.select('inbox')

# result, data = mail.search(None, 'ALL')
# ids = data[0]                       # Получаем сроку номеров писем
# id_list = ids.split()               # Разделяем ID писем
# latest_email_id = id_list[-3]       # Берем последний ID

# print(result)
# print(data)
# print(id_list)
# print(latest_email_id)

# print()
# result, data = mail.fetch(latest_email_id, '(RFC822)')
# print(result)
# print(data)
# print()
# [pprint.pprint(d) for d in data]


# еще вариант
result, data = mail.uid('search', None, "ALL") # Выполняет поиск и возвращает UID писем.
latest_email_uid = data[0].split()[-1]
result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
# print(result, latest_email_uid)


raw_email = data[0][1]  # Тело письма в необработанном виде
# включает в себя заголовки и альтернативные полезные нагрузки


import email

email_message = email.message_from_bytes(raw_email)

# for e in email_message:
#     print('\033[96m{} =>\033[0m'.format(e), email_message[e])

print('To:', email_message['To'])
print('From:', email.utils.parseaddr(email_message['From'])[1]) # получаем имя отправителя
# print(email_message.items())


# print('From:', email_message['From'])
# print('Reply-To:', email_message['Reply-To'])
# print('Date:', email_message['Date'])


def get_first_text_block(email_message_instance):
    maintype = email_message_instance.get_content_maintype()
    if maintype == 'multipart':
        for part in email_message_instance.get_payload():
            if part.get_content_maintype() == 'text':
                return part.get_payload()
    elif maintype == 'text':
        return email_message_instance.get_payload()


tt = get_first_text_block(email_message)

print(tt)
