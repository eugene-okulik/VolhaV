# Создать классы цветов: общий класс для всех цветов и классы для нескольких видов.
# Создать экземпляры (объекты) цветов разных видов.
# Собрать букет (букет - еще один класс) с определением его стоимости.
# В букете цветы пусть хранятся в списке. Это будет список объектов.
#
# Для букета создать метод, который определяет время его увядания по среднему времени жизни всех цветов в букете.
#
# Позволить сортировку цветов в букете на основе различных параметров
# (свежесть/цвет/длина стебля/стоимость)(это тоже методы)
#
# Реализовать поиск цветов в букете по каким-нибудь параметрам
# (например, по среднему времени жизни) (и это тоже метод).

class Flower:
    def __init__(self, name, color, length, price, freshness, life_time):
        self.name = name
        self.color = color
        self.length = length
        self.price = price
        self.freshness = freshness
        self.life_time = life_time

    def __repr__(self):
        flowers = (f"{self.name}, {self.color}, length = {self.length}sm, price = {self.price}ryb, "
                   f"freshness = {self.freshness}d.")
        return flowers


class Rose(Flower):
    def __init__(self, color, length, price, freshness, life_time):
        super().__init__("Rose", color, length, price, freshness, life_time)


class Tulip(Flower):
    def __init__(self, color, length, price, freshness, life_time):
        super().__init__("Tulip", color, length, price, freshness, life_time)


class Lily(Flower):
    def __init__(self, color, length, price, freshness, life_time):
        super().__init__("Lily", color, length, price, freshness, life_time)


class Peony(Flower):
    def __init__(self, color, length, price, freshness, life_time):
        super().__init__("Peony", color, length, price, freshness, life_time)


class Orchid(Flower):
    def __init__(self, color, length, price, freshness, life_time):
        super().__init__("Orchid", color, length, price, freshness, life_time)


class Bouquet:
    def __init__(self, flowers_list: list):
        self.flowers_list = flowers_list

    def bouquet_total_price(self):
        return f"Total price: {sum(f.price for f in self.flowers_list)} byn."

    def average_life_time(self):
        average_value = sum(j.life_time for j in self.flowers_list) // len(self.flowers_list)
        return f"Average life time of bouquet: {average_value}d."

    def average_for_find(self):
        return sum(k.life_time for k in self.flowers_list) // len(self.flowers_list)

    def sort_by(self, param):
        return self.flowers_list.sort(key=lambda x: getattr(x, param))

    def find_by(self, param, value):
        return [flower for flower in self.flowers_list if getattr(flower, param) == value]


rose1 = Rose("red", 75, 11, 1, 7)
rose2 = Rose("white", 80, 12, 3, 7)
lily1 = Lily("white", 100, 15, 2, 10)
peony1 = Peony("pink", 110, 18, 1, 10)
orchid1 = Orchid("violet", 60, 25, 1, 30)
tulip1 = Tulip("black", 30, 20, 1, 8)

flowers_1 = [rose1, lily1, peony1]
flowers_2 = [orchid1]
flowers_3 = [rose2, rose1, lily1, peony1, tulip1]

bouquet_1 = Bouquet(flowers_1)
bouquet_2 = Bouquet(flowers_2)
bouquet_3 = Bouquet(flowers_3)

print(bouquet_3.bouquet_total_price())
print(bouquet_2.average_life_time())

bouquet_1.sort_by("color")
for i, fl in enumerate(bouquet_1.flowers_list, start=1):
    print(f"Flower {i}. {fl}")

print(bouquet_2.find_by("life_time", bouquet_2.average_for_find()))
print(bouquet_3.find_by("price", 15))
