
from typing import Optional


class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instance: Optional['Singleton'] = None

    def __call__(self) -> 'Singleton':
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance



class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        """

        # ...


if __name__ == "__main__":
    # The client code.
    s3 = Singleton
    s1 = Singleton()
    s2 = Singleton()
    s1.some_business_logic()
    s2.some_business_logic()
    s3 = s3()
    if id(s3) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")