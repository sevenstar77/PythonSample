class Color:
    count = 0

    def __init__(self):
        Color.count += 1

    @classmethod
    def color_count(cls):
        print(cls.count)

c1 = Color()
c2 = Color()

Color.color_count()

