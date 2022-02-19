#создаем класс, который будет принимать в себя параметры
class Group:

    def __init__(self, name, header, footer):     #параметры, которые будут передаваться в конструктор из другого файла
        self.name = name
        self.header = header
        self.footer = footer



