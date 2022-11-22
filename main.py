class Human:
    height = 170
    age = 20
    post = 'Worker'
    alive = True

class Boss(Human):
    height = 180
    age = 48
    money = 1000
    energy = 100
    def __init__(self):
        self.post = 'Boss'

class Worker(Human):
    age = 37
    money = 0
    energy = 80
    progress = 0
    def work(self):
        if self.alive == True and self.post == 'Worker':
            self.money += 1
            self.energy -= 29
            self.progress += 3
        p.check_all()
    def get_pay(self):
        if self.alive == True and self.post == 'Worker':
            self.money += 10
        p.check_all()
    def sleep(self):
        if self.alive == True and self.post == 'Worker':
            p.get_pay()
            self.energy = 80
        p.check_all()
    def post_up(self):
            super().__init__()

    def check_all(self):
        if self.energy <= 0:
            self.alive = False
            print('You die!')
        elif self.progress >= 100:
            self.progress = 100
            p.post_up()
            print('You win!')

p = Worker()
while True:
    if p.alive == True and p.post == 'Worker':
        print(f'\nWhat you can choose:\n\t1 - Work\n\t\tEnergy - 29\n\t\tMoney + 1\n\t\tProgress + 3\n\t2 - Sleep\n\t\tEnergy = 80\n\t\tGet pay\n\nYour stats:\n\tEnergy - {p.energy}\n\tMoney - {p.money}\n\tPost - {p.post}\n\tProgress - {p.progress}')
        choice = input('\nWhat do you choose: ')
        if choice == '1':
            p.work()
        elif choice == '2':
            p.sleep()
        else:
            print(f'\nPlease try something else')
            continue