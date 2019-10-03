class Publisher:
    def __init__(self):
        self.subscribers = []

    def addSubscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def removeSubscriber(self, subscriber):
        self.subscribers.remove(subscriber)

    def showSubscribers(self):
        for _subscriber in self.subscribers:
            print(_subscriber.name)

    def notifyAll(self, message):
        print(message)
        for _subscriber in self.subscribers:
            if _subscriber.name != 'bad guy':
                _subscriber.notify_me(message)

    def data_leak(self):
        message = 'Change pin codes!!!'
        self.notifyAll(message)

    def take_moneys(self):
        message = 'give moneys'
        self.notifyAll(message)

class Observer:
    def __init__(self, name):
        self.name = name

    def notify_me(self, message):
        if message == 'Change pin codes!!!':
            print(self.name + ': SHIIIT!!!')
            if self.name == 'bad guy':
                print(self.name + ': I was found')
        else:
            if self.name == 'John':
                print(self.name + ': no')
            else:
                print(self.name + ': I`ll give you moneys')


if __name__ == '__main__':
    kredobank = Publisher()
    client1 = Observer('John')
    client2 = Observer('Doe')
    stolling_moneys = Observer('bad guy')
    kredobank.addSubscriber(client1)
    kredobank.addSubscriber(client2)
    kredobank.addSubscriber(stolling_moneys)
    kredobank.showSubscribers()
    kredobank.data_leak()
    kredobank.removeSubscriber(stolling_moneys)
    kredobank.take_moneys()