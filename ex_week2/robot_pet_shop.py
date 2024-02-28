class Robot():
    def __init__(self, material = None, price = None, cost_to_fix = None, name = None, id = None, battery_type = None, animal_type = None):
        self.material = material
        self.price = price
        self.cost_to_fix = cost_to_fix
        self.name = name
        self.id = id
        self.battery_type = battery_type
        self.animal_type = animal_type

class Employee(Robot):
    def __init__(self, salary, name, id, battery_type = None):
        self.salary = salary
        super().__init__(name=name, id=id, battery_type=battery_type)


class Store():
    def __init__(self, balance = 1000):
        self.balance = balance
        self.robots = {'sale': [],'broken':[], 'repair': [], 'shipped': [], 'sold': []}
        self.employees = []

    def add_to_store(self,status, material = None, price = None, cost_to_fix = None, name = None, id = None, battery_type = None, animal_type = None):
        new_robot = Robot(material , price , cost_to_fix , name, id , battery_type , animal_type )
        self.robots[status].append(new_robot)

    def add_emp(self,salary, name, id, battery_type = None):
        new_emp = Employee(salary, name, id, battery_type)
        self.employees.append(new_emp)

    def sell_robot(self, robot):
        # add robot price to balance
        if robot.price:
            self.balance += robot.price

    def remove_salary(self):
        # each day remove salary from balance for all emp
        for i in self.employees:
            self.balance -= i.salary

    def print_pets_for_sale(self):
        robots_for_sale = self.robots['sale']
        if robots_for_sale:
            print('available robots for sale :')
            for i in robots_for_sale:
                print(i.name)
        else:
            print('No available robots for sale')

    def print_pets_in_repair(self):
        robots_for_repair = self.robots['repair']
        if robots_for_repair:
            print('available robots in repair :')
            for i in robots_for_repair:
                print(i.name)
        else:
            print('No available robots in repair')

    def print_pets_for_sale_by_price(self,start,end):
        robots_for_sale = self.robots['sale']
        res = []
        if robots_for_sale:
            for i in robots_for_sale:
                if i.price >= int(start) and i.price <= int(end):
                    res.append(i.name)
            if len(res) > 0:
                print('available robots for sale in this range:')
                for i in res:
                    print(i)
            else:
                print('NO available robots for sale in this range')
        else:
            print('No available robots for sale')

    def print_employees_salary(self):
        print('employees salary: ')
        for i in self.employees:
            print(i.name, i.salary)

    def print_store_balance(self):
        print(self.balance)

    def print_robot_by_info(self,id, name):
        found = False
        for status, robots in self.robots.items():
            for robot in robots:
                if robot.name == name and robot.id == id:
                    found = robot
                    break
        if found:
            print('Robot info: ')
            print(f'name : {found.name}')
            print(f'material : {found.material}')
            print(f'price : {found.price}')
            print(f'cost to fix : {found.cost_to_fix}')
            print(f'battery type : {found.battery_type}')
            print(f'animal type : {found.animal_type}')
        else:
            print('NO robot found!')


# Creating 5 robots
robot1 = Robot(name="Robot1", id=1, material="Metal", price=100, cost_to_fix=50, battery_type="Lithium", animal_type="herbivore")
robot2 = Robot(name="Robot2", id=2, material="Plastic", price=80, cost_to_fix=30, battery_type="Alkaline", animal_type="carnivore")
robot3 = Robot(name="Robot3", id=3, material="Aluminum", price=120, cost_to_fix=40, battery_type="Alkaline", animal_type="herbivore")
robot4 = Robot(name="Robot4", id=4, material="Carbon Fiber", price=150, cost_to_fix=60, battery_type="Alkaline", animal_type="carnivore")
robot5 = Robot(name="Robot5", id=5, material="Titanium", price=200, cost_to_fix=70, battery_type="Lithium", animal_type="herbivore")

store = Store()
# status : 'sale' / 'broken' / 'repair' / 'shipped' / 'sold'

# add robots to the store
store.add_to_store(status='sale', name="Robot1", id=1, material="Metal", price=100, cost_to_fix=50, battery_type="Lithium", animal_type="herbivore")
store.add_to_store(status='sale', name="Robot2", id=2, material="Plastic", price=80, cost_to_fix=30, battery_type="Alkaline", animal_type="carnivore")
store.add_to_store(status='sale', name="Robot3", id=3, material="Aluminum", price=120, cost_to_fix=40, battery_type="Alkaline", animal_type="herbivore")
store.add_to_store(status='broken', name="Robot1", id=1, material="Metal", price=100, cost_to_fix=50, battery_type="Lithium", animal_type="herbivore")
store.add_to_store(status='repair', name="Robot2", id=2, material="Plastic", price=80, cost_to_fix=30, battery_type="Alkaline", animal_type="carnivore")
store.add_to_store(status='shipped', name="Robot3", id=3, material="Aluminum", price=120, cost_to_fix=40, battery_type="Alkaline", animal_type="herbivore")

# add emp to the store
store.add_emp(salary=150, name='rob1', id='01')
store.add_emp(salary=150, name='rob2', id='02')
store.add_emp(salary=150, name='rob3', id='03')

#
store.sell_robot(robot1)

store.print_store_balance()
store.print_pets_for_sale()
store.print_employees_salary()
store.print_robot_by_info(id = 2,name = 'Robot2')
