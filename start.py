# #
# При выставлении оценок в ведомость преподавателю необходимо не только указать полученную
# студентом оценку, но и расшифровать её. В университете принята следующая шкала
# оценок: меньше 4 — 'неудовлетворительно', 4-5 —'удовлетворительно', 6-7 — 'хорошо', 8 и
# выше — 'отлично'. Напишите программу, которая принимает на вход полученную оценку (mark) и
# расшифровывает её таким образом: вводимая оценка — число от 1 до 10. Для проверки используйте
# mark = 7

mark = 7
if mark < 4:
    print('неудовлетворительно')
elif mark == 4 or mark == 5:
    print('удовлетворительно')
elif mark == 6 or mark == 7:
    print('хорошо')
else:
    print('отлично')