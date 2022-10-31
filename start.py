# #
# При выставлении оценок в ведомость преподавателю необходимо не только указать полученную
# студентом оценку, но и расшифровать её. В университете принята следующая шкала
# оценок: меньше 4 — 'неудовлетворительно', 4-5 —'удовлетворительно', 6-7 — 'хорошо', 8 и
# выше — 'отлично'. Напишите программу, которая принимает на вход полученную оценку (mark) и
# расшифровывает её таким образом: вводимая оценка — число от 1 до 10. Для проверки используйте
# mark = 7

"""
mark = 7
if mark < 4:
    print('неудовлетворительно')
elif mark == 4 or mark == 5:
    print('удовлетворительно')
elif mark == 6 or mark == 7:
    print('хорошо')
else:
    print('отлично')
"""

# Иногда человек хочет сходить в ресторан. Он может себе это позволить, если у него до зарплаты
# осталось (balance) больше 5 тысяч рублей. Если же у него меньше 5 тысяч, но больше 2.5 тысяч
# рублей, он может сходить только в фастфуд. Если меньше, то придётся терпеть до зарплаты.
# Напишите программу, которая принимает на вход количество оставшихся денег в рублях и говорит,
# можно ли человеку пойти в ресторан (варианты ответа программы - "Сегодня твой выбор - ресторан!",
# "Эх, только фастфуд." и "Придётся потерпеть!"). Для проверки используйте balance = 455

balance = 455
if balance > 5000:
    print("Сегодня твой выбор - ресторан!")
elif balance > 2500 and balance < 5000:
    print("Эх, только фастфуд.")
else:
    print("Придётся потерпеть!")