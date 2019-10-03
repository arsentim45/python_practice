class User:
    def __init__(self):
        self.username = None
        self.mail = None
        self.password = None
        self.card = None
        self.isAdmin = False

    def register(self, username, mail, password):
        self.username = username
        self.mail = mail
        self.password = password

    def add_payment(self, card):
        self.card = card


class PaymentCheck:
    def __init__(self, user):
        self.user = user
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return self

    def check(self):
        if self.user.card:
            if self.next_handler:
                return self.next_handler.check()
            else:
                return True
        else:
            print('{} not allowed to buy'.format(self.user))
            return False


class AdminCheck:
    def __init__(self, user, magazine):
        self.magazine = magazine
        self.user = user
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return self

    def check(self):
        if self.user in self.magazine.admins_list:
            if self.next_handler:
                return self.next_handler.check()
            else:
                return True
        else:
            print('{} not an admin'.format(self.user))
            return False


class Magazine:
    def __init__(self):
        self.products_list = []
        self.admins_list = []
        self.users_list = []

    def watch_products(self):
        return self.products_list

    def buy_product(self, user, product):
        if user.card:
            return product
        else:
            raise ValueError

    def remove_user(self, user, user_to_remove):
        if user.isAdmin:
            self.products_list.remove(user_to_remove)
        else:
            return None

    def __iter__(self):
        self.a = 0

if __name__ == '__main__':
    magazine = Magazine()
    admin = User()
    admin.register('a', 'a@.com', 'a')
    admin.add_payment('acav')
    magazine.admins_list.append(admin)
    user1 = User()
    user1.register('a', 'a', 'a')
    user2 = User()
    user2.register('a', 'a', 'a')
    user2.add_payment('a')
    print('is user admin ', PaymentCheck(admin).set_next(AdminCheck(admin, magazine)).check())
    print('is user allowed to buy ', PaymentCheck(user1).check())
    print('is user admin ', PaymentCheck(user1).set_next(AdminCheck(user1, magazine)).check())
    print('is user admin ', PaymentCheck(user2).set_next(AdminCheck(user2, magazine)).check())