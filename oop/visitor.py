class Museum:
    def accept(self, visitor):
        visitor.visit_museum(self)

    def kick(self):
        return 'not allowed to museum'

    def not_kick(self):
        return 'allowed to museum'


class Pub:
    def accept(self, visitor):
        visitor.visit_pub(self)

    def kick(self):
        return 'not allowed to pub'

    def not_kick(self):
        return 'allowed to pub'


class Visitor1:
    def __init__(self, name):
        self.name = name

    def visit_pub(self, component):
        print(f"{self.name} allowed? {component.kick()}")

    def visit_museum(self, component):
        print(f"{self.name} allowed? {component.not_kick()}")


class Visitor2:
    def __init__(self, name):
        self.name = name

    def visit_pub(self, component):
        print(f"{self.name} allowed? {component.not_kick()}")

    def visit_museum(self, component):
        print(f"{self.name} allowed? {component.kick()}")


if __name__ == '__main__':
    sites = [Museum(), Pub()]
    visitors = [Visitor1('NotArsen'), Visitor2('Arsen')]
    for visitor in visitors:
        for site in sites:
            site.accept(visitor)