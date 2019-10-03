from time import sleep

class EstimationFactory:
    pass

class GoodWorker:
    def work_on_task(self, time):
        print('doing well for % hours of time', time/2)


class BadWorker:
    def work_on_task(self, time):
        print('doing bad for % hours of time', time*2)


class Devops:
    def __init__(self):
        print('ide buhat')
        sleep(10000)

def estimate(priority):
    classes = {
        'high': GoodWorker,
        'low': BadWorker
    }
    return classes[priority]()

if __name__ == '__main__':
    estimate('high').work_on_task(9)
    estimate('low').work_on_task(10)
    estimate('high').work_on_task(6)