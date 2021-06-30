class Auto:

    # конструктор
    def __init__(self, color):
        self.brand = 'Opel'
        self.model = 'Omega'
        self.color = color

    # деструктор
    def __del__(self):
        print(self.brand, self.model, '- удалено c памяти')

    def info(self):
        print(f'Бренд: {self.brand}\nМодель: {self.model}\nЦвет: {self.color}')


auto = Auto('Red')
auto.model = 'Cadet'
auto.info()

del auto
