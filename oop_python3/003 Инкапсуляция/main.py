class Auto:

    # конструктор
    def __init__(self, color: str):
        self.brand = 'Opel'
        self.model = 'Omega'
        # приватная переменная
        self.__color = color
        self.__engine = 2.0
        self.__fuel = 'Дизель'

    # деструктор
    def __del__(self):
        print(self.brand, self.model, '- удалено c памяти')

    def info(self):
        print(f'Бренд: {self.brand}\nМодель: {self.model}\nЦвет: {self.__color}\nОбъём: {self.__engine}\nТопливо: {self.__fuel}')

    def set_fuel(self, fuel: str):
        fuel_list = ['дизель', 'бензин', 'газ']
        if fuel.lower() in fuel_list:
            self.__fuel = fuel
        else:
            print(f'{fuel} - такого топлива нет!')

    def set_engine(self, engine: float):
        self.__engine = engine


auto = Auto('Red')
auto.set_engine(3.0)
auto.set_fuel('Газ')
auto.info()

