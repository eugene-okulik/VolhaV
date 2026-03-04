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
    name = "Rose"


class Tulip(Flower):
    name = "Tulip"


class Lily(Flower):
    name = "Lily"


class Peony(Flower):
    name = "Peony"


class Orchid(Flower):
    name = "Orchid"


class Bouquet:
    def __init__(self, flowers_list: list):
        self.flowers_list = flowers_list

    def bouquet_total_price(self):
        return f"Total price: {sum(i.price for i in self.flowers_list)} byn."

    def average_life_time(self):
        average_value = sum(i.life_time for i in self.flowers_list) // len(self.flowers_list)
        print(f"Average life time of bouquet: {average_value}d.")

    def average_for_find(self):
        return sum(i.life_time for i in self.flowers_list) // len(self.flowers_list)

    def sort_by(self, param):
        sorted_list = sorted(self.flowers_list, key=lambda x: getattr(x, param))
        print(f"Flowers was sorted by {param}:")
        for flower in range(len(sorted_list)):
            print(f"Flower {flower + 1}.", sorted_list[flower])

    def find_avg_live_time(self):
        avg_life_time = self.average_for_find()
        result = [f for f in self.flowers_list if f.life_time == avg_life_time]
        print(f"Flowers with the average life time {avg_life_time} days: {len(result)} шт.")
        for flower in result:
            print(f"- {flower.name}, {flower.color}")


rose1 = Rose(Rose.name, "red", 75, 11, 1, 7)
rose2 = Rose(Rose.name, "white", 80, 12, 3, 7)
lily1 = Lily(Lily.name, "white", 100, 15, 2, 10)
peony1 = Peony(Peony.name, "rose", 110, 18, 1, 10)
orchid1 = Orchid(Orchid.name, "violet", 60, 25, 1, 30)
tulip1 = Tulip(Tulip.name, "black", 30, 20, 1, 8)

flowers_1 = [rose1, lily1, peony1]
flowers_2 = [orchid1]
flowers_3 = [rose2, rose1, lily1, peony1, tulip1]

bouquet_1 = Bouquet(flowers_1)
bouquet_2 = Bouquet(flowers_2)
bouquet_3 = Bouquet(flowers_3)

print(bouquet_3.bouquet_total_price())
bouquet_2.average_life_time()
bouquet_3.sort_by("price")
bouquet_3.sort_by("length")
bouquet_3.sort_by("freshness")
bouquet_3.sort_by("color")

bouquet_1.find_avg_live_time()
bouquet_2.find_avg_live_time()
bouquet_3.find_avg_live_time()
