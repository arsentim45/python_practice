class Adapter:
    def __init__(self, origin, adapted):
        self.origin = origin
        self.adapted = adapted

    def __getattr__(self, item):
        return getattr(self.origin, item)


class Client:
    pass


class XML:
    def display(self):
        print('display xml')

class JSON:
    def display(self):
        print('display json')
        
if __name__ == '__main__':
    adapted_xml = Adapter(XML(), JSON())
    adapted_xml.display()
    adapted_json = Adapter(JSON(), XML())