'''
Дано отображение a = 1, b = 2, ... z = 26 и закодированное сообщение, подсчитайте 
количество способов его декодирования. Например, сообщение «111» даст 3, 
поскольку оно может быть декодировано как «aaa», «ka» и «ak».
Вы можете предположить, что сообщения можно декодировать. Например, «001» не допускается.
'''

def is_char(code):
    return 0 if code > 26 or code < 1 else 1

def get_message_count(message):
    msg_str = str(message)

    if len(msg_str) == 1:
        count = 1
    elif len(msg_str) == 2:
        count = 1 + is_char(message)
    else:
        count = get_message_count(int(msg_str[1:]))
        if is_char(int(msg_str[:2])):
            count += get_message_count(int(msg_str[2:]))
    return count

print(get_message_count(1234))