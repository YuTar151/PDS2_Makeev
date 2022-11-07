"""
2. Напишіть клас TextProcessor для обробки текстових даних. Клас повинен мати публічний метод get_clean_string,
який видалить усі знаки пунктуації з рядка, який передається йому аргументом, та приватним методом іs_punktiantian,
який безпосередньо перевіряє символ на рівність зі знаками пунктуації та повертає True/False, який, у свою чергу,
є приватним або захищеним атрибутом. Потім напишіть клас TextLoader, який має приватний атрибут text_processor,
що в об'єктом класу TextProcessor. Клас TextLoader повинен мати приватний атрибут clean_string і публічний
метод set_clean_text, який буде викликати метод класу TextProcessor, через свій атрибут text_processor і записує
значення в сlеаn_string. Створіть додатковий рrореrtу для сlеаn_string, який буде виводити повідомлення В консоль
про те, що виводиться вже очищений текст. Напишіть клас Datalnterface, в якому буде захищений атрибут,
що є екземпляром класу TextLoader, а також публічний метод process_texts, який буде приймати список рядків,
опрацьовувати їх у циклі і виводити значення в консоль.
"""




class TextProcessor:
    def init(self):
        self._punktuation = '.,!?;:*'

    def __is_punktuation(self, char):
        return char in self._punktuation

    def get_clean_string(self, text):
        clean_text = ""
        for char in text:
            if self.__is_punktuation(char):
                continue
            clean_text += char
        return clean_text