import random
import time


class Memento:
    def __init__(self, some_state):
        self.some_state = some_state
        self.timestamp = time.time()

    def get_el(self):
        return self.some_state

    def __str__(self):
        return f'At {self.timestamp} I was in state {self.some_state}'


class AGV:
    def __init__(self, state):
        self._state = state

    def do_smth(self):
        self._state = random.randint(1,100)

    def save(self):
        return Memento(self._state)


class BackupService:
    def __init__(self, orginator, history=None):

        self.originator = orginator
        self._history = []

    def backup(self):
        self._history.append(self.originator.save())

    def undo(self):
        self._history.pop()
        if self._history:
            self.originator._state = self._history[-1].get_el()

    @property
    def history(self):
        for history in self._history:
            print(history)
        return None


if __name__ == '__main__':
    agv1 = AGV('initial')
    backup = BackupService(agv1)
    backup.backup()

    agv1.do_smth()
    agv1.do_smth()
    backup.backup()
    agv1.do_smth()
    backup.backup()
    backup.history

    backup.undo()
    print(agv1._state)
