import operations as op
import os
os.system("cls")

from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler
from config import TOKEN

bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

flag_g1 = 1
operation_a_b = 0
value_a = 0
value_b = 0

def start(update, context):
    arg = context.args
    if not arg:
        context.bot.send_message(update.effective_chat.id, "Привет, введите /info")
    else:
        context.bot.send_message(update.effective_chat.id, f"{' '.join(arg)}")


def info(update, context):
    context.bot.send_message(update.effective_chat.id,
                             """Доступны следующие команды:
                             /info - информация,
                             /q - Если хотиете завершить работу, в любой момент введите: /q,
                             /go - Если хотите продолжить """)

def q(update, context):
    context.bot.send_message(update.effective_chat.id,
                             """До свидания! Если хотите продолжить, нажмите /info """)

def go(update, context):
    global flag_g1
    context.bot.send_message(update.effective_chat.id,
                             f"""Укажите, какого типа будет число {flag_g1}? \n a - Рациональное \n b - Комплексное \n """)                             


def message(update, context):
    text = update.message.text
    if text.lower() == 'привет':
        context.bot.send_message(update.effective_chat.id, 'Привет..')
    else:
        context.bot.send_message(update.effective_chat.id, 'я тебя не понимаю')


def unknown(update, context):
    context.bot.send_message(update.effective_chat.id, f'Шо сказал, не пойму')

def get_number(i,update,context):
    '''
    Получение числа с учетом типа и проверка корректности ввода.
    '''
    # number_type = ch.check_number_type(
    #     f'Укажите, какого типа будет число {i}? \n 1 Рациональное \n 2 Комплексное \n')
    if i == 1:
        context.bot.send_message(update.effective_chat.id, f"Введите число ")
    elif i == 2:
        print("!!@!!")
        context.bot.send_message(update.effective_chat.id,
            f'Введите через запятую 2 числа. Для комплексного числа вида z = a + bj, первое из них - действительная часть a, второе - мнимая часть b:\n')
    else:    
        context.bot.send_message(update.effective_chat.id, "вы ввели неправльное число, повторите ввод")


def flag_op():
    global flag_g1
    flag_g1 = flag_g1 + 1


def give_word(update,context):
    global flag_g1
    global operation_a_b
    global value_b
    global value_a
    word = update.message.text
    if "a" in word: # если ввели "а", то значит - это рациональное число
        get_number(1,update,context)
    elif "b" in word:
        get_number(2,update,context)   
    else:     
        if flag_g1 == 1:
            value_a = int(word)
            flag_op()  # для определения - первое это число или второе
            go(update,context)                       
        elif flag_g1 == 2:
            value_b = int(word)
            flag_op()
            get_operation(update,context)
        elif flag_g1 == 3:
            if "1" in word:
                result = op.sum_numbers(value_a, value_b)
                print(result)
            elif "2" in word:
                result = op.diff_numbers(value_a, value_b)
            elif "3" in word:
                result = op.mult_numbers(value_a, value_b)
            elif "4" in word:
                ch.check_exceptions_div(value_a, value_b)
                result = op.div_numbers(value_a, value_b)
            elif "5" in word:
                ch.check_exceptions_exp(value_a, value_b)
                result = op.exp_numbers(value_a, value_b)
            context.bot.send_message(update.effective_chat.id, f'\nРезультат:\n{result}')   

def get_operation(update,context):
    '''
    Функция получает номер опреации и проверяет его на корректность.
    '''
    context.bot.send_message(update.effective_chat.id,
            f'Какую операцию вы хотите выполнить? \n 1 Сложение \n 2 Вычитание \n 3 Умножение \n 4 Деление \n 5 Возведение в степень\n')



    
 


    # if "бар" in word:
    #     joke = '''Белый медведь заходит в паб и говорит бармену:
    #             - Дайте мне виски и... кока-колу.
    #             - А почему такая пауза? - спрашивает бармен.
    #             - Это всё, что вас удивляет? - с обидой говорит медведь.'''
    #     context.bot.send_message(update.effective_chat.id, joke)
    #     return joke
    # elif "пока" in word:
    #     context.bot.send_message(update.effective_chat.id, 'Покачивай шляпой из бара')
    #     return word
    # context.bot.send_message(update.effective_chat.id, 'Вы, как всегда, правы, милорд')

start_handler = CommandHandler('start', start)
info_handler = CommandHandler('info', info)
q_handler = CommandHandler('q', q)
go_handler = CommandHandler('go', go)
message_handler = MessageHandler(Filters.text, give_word)
unknown_handler = MessageHandler(Filters.command, unknown)  # /game


dispatcher.add_handler(start_handler)
dispatcher.add_handler(info_handler)
dispatcher.add_handler(q_handler)
dispatcher.add_handler(go_handler)
#dispatcher.add_handler(conv_handler)
dispatcher.add_handler(unknown_handler)
dispatcher.add_handler(message_handler)


print('server started')
updater.start_polling()
updater.idle()




