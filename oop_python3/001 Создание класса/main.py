class Auto:
    brand = 'Lada'
    model = 'Kalina'
    color = 'White'

    def info(self):
        print(f'{self.brand}\n{self.model}\n{self.color}')


auto = Auto()
auto.model = 'Priora'
auto.info()
