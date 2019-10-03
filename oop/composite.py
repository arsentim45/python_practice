class Composite:

    def __init__(self):
        self.children = []
        super()

    def add(self, children):
        self.children.append(children)
        children.parent = self

    def remove(self, children):
        self.children.remove(children)
        children.parent = None


class Element:
    def __init__(self):
        self.parent = None


class Child(Element):

    pass


if __name__ == '__main__':
    main_menu = Composite()
    main_menu.add(Child())
    sub_ment = Composite()
    sub_ment.add(Child)
    main_menu.add(sub_ment)