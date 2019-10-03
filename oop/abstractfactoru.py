# class Water:
#     def drink(self):
#         print('drinking zapivon')
#
# class Alcohol:
#     def drink(self):
#         print('drinking alcohol')
#         print('need zakus or zapivon')
#
# class Food:
#     def drink(self):
#         print('you drunk? how you can drink zakus?')
#
# class Magazine:
#     def __init__(self, market_factory):
#         self.market_factory = market_factory
#
#     def get_water(self):
#         self.market_factory.drink()
# factory = Magazine()
# lowcost = AtbMarket()
# midcost =

class CodeFactory:
    def get_python_code(self):
        return PythonCode()

    def get_lisp_code(self):
        return LispCode()

class PythonCode:
    def write_code(self):
        print('slow but easy to write code')

class CppCode:
    def write_code(self):
        print('fast but enormous big code')

class LispCode:
    def write_code(self):
        print('(((((((((((((((((((((print(1))))))))))))))))))))))')

class JSCode:
    def write_code(self):
        print('[] is 0 is True')