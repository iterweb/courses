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
        return (f'Бренд: {self.brand}\nМодель: {self.model}\nЦвет: {self.__color}\nОбъём: {self.__engine}\nТопливо: {self.__fuel}')

    def set_fuel(self, fuel: str):
        fuel_list = ['дизель', 'бензин', 'газ']
        if fuel.lower() in fuel_list:
            self.__fuel = fuel
        else:
            print(f'{fuel} - такого топлива нет!')

    def set_engine(self, engine: float):
        self.__engine = engine


class AutoReg(Auto):

    def set_number(self, nmb: str):
        self.__nmb = nmb

    def get_number(self):
        return (f'\nНомер: {self.__nmb}')


auto = AutoReg('Серый')
auto.set_engine(1.4)
inf = auto.info()
auto.set_number('A 1240 OB')
nmb = auto.get_number()

print(inf, nmb)

