import mouse


class graphic_object:

    def __init__(self, position_x, position_y, width, height):
        self.position_x = position_x
        self.position_y = position_y
        self.width = width
        self.height = height
        print('I am graphic_object')


class Rectangle(graphic_object):
    def __init__(self, position_x, position_y, width, height):
        super().__init__(position_x, position_y, width, height)
        print('I am rectangle')


class Click:

    def click_me(self):
        while True:
            if mouse.is_pressed():
                print('Thanks for pressing!')
                break


class Button(Rectangle, Click):
    def __init__(self, position_x, position_y, width, height):
        super().__init__(position_x, position_y, width, height)
        print('I am button')


if __name__ == '__main__':
    button1 = Button(15, 65, 10, 6)  # Задание 3 - выводит потому что именно так отработал метод super, ссылаясь на
    # прямоугольник где он уже при инициализации ссылается на графический обьект
    rectangle1 = Rectangle(10, 35, 15, 5)
    button1.click_me()
