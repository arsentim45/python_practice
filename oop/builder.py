class Director(object):
    def __init__(self):
        self.builder = None

    def construct(self):
        self.builder.build_wall()
        self.builder.build_toilet()
        self.builder.build_smth()
        return None

    def get_house(self):
        return self.builder.house


class Builder:
    def __init__(self):
        self.building = None

    def get_house(self):
        return

    def build_wall(self):
        pass

    def build_toilet(self):
        pass

    def build_smth(self):
        pass

class BuryatBuilder(Builder):

    def build_smth(self):
        print('Nachalink ne volnuysya')

    def build_toilet(self):
        print('Rabotaem nachalnik')

    def build_wall(self):
        print('Vse horosho nachalnit')

class HipsterBuilder(Builder):

    def build_smth(self):
        print('drinking smusi')

if __name__ == '__main__':
    director = Director()
    builder = BuryatBuilder()
    director.builder = builder
    director.construct()
    bad_house = director.get_house()

