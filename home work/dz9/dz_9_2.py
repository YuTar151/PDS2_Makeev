"""
2. Напишіть клас TextProcessor для обробки текстових даних.
Клас повинен мати публічний метод get_clean_string, який видалить усі знаки пунктуації з рядка, який передається йому аргументом,
та приватним методом іs_punktiantian, який безпосередньо перевіряє символ на рівність зі знаками пунктуації та повертає True/False,
який, у свою чергу, є приватним або захищеним атрибутом.

Напишіть клас Datalnterface, в якому буде захищений атрибут, що є екземпляром класу TextLoader,
а також публічний метод process_texts, який буде приймати список рядків, опрацьовувати їх у циклі і виводити значення в консоль.
"""
class TextProcessor:

    def __init__(self, text):
        self._puncts = puncts = "'.,!?;:*"
        self.text = text

    def __іs_punktiantian(self, text):  # перевіряє символ на рівність зі знаками пунктуації та повертає True/False
        return self._puncts in text

    def get_clean_string(self, text):   # видаляє усі знаки пунктуації з рядка, який передається йому аргументом
        for char in text:
            if char in self._puncts:
                text = text.replace(char, "")
        return text



t = "?,!Напишіть:; клас, да*них.??"
tp = TextProcessor(t)
print(tp.get_clean_string(t))


"""
Потім напишіть клас TextLoader, який має приватний атрибут _text_processor, що є об'єктом класу TextProcessor. 
Клас TextLoader повинен мати приватний атрибут _clean_string і публічний метод set_clean_text, 
який буде викликати метод класу TextProcessor, через свій атрибут _text_processor і записує значення в _сlеаn_string. 
Створіть додатковий рrореrtу для сlеаn_string, який буде виводити повідомлення В консоль
про те, що виводиться вже очищений текст.
"""
class TextLoader:

    def __init__(self, text_processor : TextProcessor):
        self._text_processor = text_processor
        self._clean_string = ''

    @property
    def clean_string(self): #додатковий рrореrtу для сlеаn_string, який буде виводити повідомлення В консоль про те, що виводиться вже очищений текст.
        # print('Ця строка вже очищена: ')
        return 'Ця строка вже очищена: ' + self._clean_string

    def set_clean_text(self, text):   # викликє метод класу TextProcessor, через свій атрибут text_processor і записує значення в сlеаn_string.
        self._clean_string = self._text_processor.get_clean_string(text)
        return


t_loader = TextLoader(tp)
t_loader.set_clean_text("?,!Інший:; клас, да*них.??")
print(t_loader.clean_string)


"""
Напишіть клас Datalnterface, в якому буде захищений атрибут, що є екземпляром класу TextLoader,
а також публічний метод process_texts, який буде приймати список рядків, опрацьовувати їх у циклі і виводити значення в консоль.
"""
class Datalnterface:

    def __init__(self, t_loader : TextLoader):
        self._t_loader = t_loader


    def process_texts(self, text):
        for string in text:
            self._t_loader.set_clean_text(string)
            print(self._t_loader.clean_string)


list = ['sdgjknsd90909', '-sfksdfnm', 'yklio']
di = Datalnterface(t_loader)
di.process_texts(list)


