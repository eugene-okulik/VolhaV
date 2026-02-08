import math

katet_1 = 3
katet_2 = 4

hypotenuse = math.sqrt(katet_1 ** 2 + katet_2 ** 2)
poluperimetr = (katet_1 + katet_2 + hypotenuse) / 2
square = math.sqrt(poluperimetr * (poluperimetr - katet_1) * (poluperimetr - katet_2) * (poluperimetr - hypotenuse))

print(hypotenuse)
print(square)
