class Mediator:
    def __init__(self, components):
        self.components = components

    def add_component(self, component, component_name):
        self.components[component_name] = component

    def notify(self, component_name, job):
        if job == 'doing job1':
            self.components[component_name].do_else()
        elif job == 'help':
            for items in self.components.keys():
                self.components[items].do_help()

class Component:
    def __init__(self, mediator, component_name):
        self.mediator = mediator
        self.mediator.components[component_name] = self
        self.component_name = component_name

    def do_smth(self):
        print('doing smth')
        self.mediator.notify(self.component_name, 'doing job1')\

    def do_else(self):
        print('need help')
        self.mediator.notify(self.component_name, 'help')

    def do_help(self):
        print(self.component_name, ' is helping')

if __name__ == '__main__':
    med = Mediator({})
    com1 = Component(med, 'component1')
    com2 = Component(med, 'component2')
    com3 = Component(med, 'component3')
    com1.do_smth()