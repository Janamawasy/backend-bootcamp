class Item():
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

class ElectronicItem(Item):
    # universal charger, Smartphone, Laptop, Smartwatch
    def __init__(self,name, weight, color = None, price = None, size = None,
                 brand = None,os = None, storage = None, display = None,
                 camera = None, materials = None,processor = None,
                 ram = None, graphics = None, battery_life = None,
                 fitness_features = None, connectivity = None):
        super().__init__(name, weight)
                     ## color and price/cost are the same in electronic and none electronic. why not put in item?
        self.color = color
        self.price = price
        self.size = size
        self.brand = brand
        self.os = os
        self.storage = storage
        self.display = display
        self.camera = camera
        self.materials = materials
        self.processor = processor
        self.ram = ram
        self.graphics = graphics
        self.battery_life = battery_life
        self.fitness_features = fitness_features
        self.connectivity = connectivity


class NonElectronicItem(Item):
    # Passport, sunglasses, sneakers, campus
    def __init__(self, name, weight, color=None, cost=None, bought_from=None,
                 have_case=None, origin=None, brand=None, is_new=None,
                 accuracy=None, price=None, materials=None):
        super().__init__(name, weight)
        self.color = color
        self.cost = cost
        self.bought_from = bought_from
        self.have_case = have_case
        self.origin = origin
        self.brand = brand
        self.is_new = is_new
        self.accuracy = accuracy
        self.price = price
        self.materials = materials
# ----------------------------------------------------

class Bag:
    def __init__(self, max_weight = 80, max_items = 6):
        self.max_weight = max_weight
        self.max_items = max_items
        self.items = []
    ## good small functions, good naming
    ### is the if statment easy to read in your mind?
    ### how would you make it more readable?
    def add_item(self, item):
        if len(self.items) < self.max_items and self.get_bag_weight() + item.weight <= self.max_weight:
            print(len(self.items), self.max_items, self.get_bag_weight() + item.weight, self.max_weight)
            self.items.append(item)
            print('item was added')
        else:
            print(f'no left place in the bag, there is {len(self.items)} items and there weight is {self.get_bag_weight()} ')

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print('item was removed')
        else:
            print('the item is not in the bag')
        pass

    def get_bag_weight(self):
        weight = 0
        for i in self.items:
            weight += i.weight
        return weight

    def print_packed_items(self):
        print('bag content :: ')
        for i in self.items:
            print(i.name)
        print(f'bag weight : {self.get_bag_weight()}')
        print(f'number of items in the bag : {len(self.items)}')

    def print_by_category(self):
        categories = {}
        for item in self.items:
            ### nnique implementation. interesting
            cat = item.__class__.__name__
            print(cat , item.name)
            if cat not in categories:
                categories[cat] = [item.name]
            else:
                categories[cat].append(item.name)

        for cat, items in categories.items():
            print(f'{cat}:')
            for item in items:
                print(f'{item}')

    def print_items_from_cat(self,category):
        # self.category = category
        items_in_cat = []
        for i in self.items:
            if isinstance(i,category):
                items_in_cat.append(i.name)
        if items_in_cat:
            print(items_in_cat)
        else:
            print('No items in this category')

### HARDCODING
item1 = ElectronicItem(name="Charger", weight=12, color="Black", price=50, size="Medium", brand="Lenovo")
item2 = ElectronicItem(name="Smartphone", weight=50, brand="Apple", os="iOS", storage="128 GB", display="AMOLED", camera="Dual Lens", materials=["lithium", "plastic"])
item3 = ElectronicItem(name="Laptop", weight=60, brand="Dell", processor="Intel i7", ram="16 GB", storage="512 GB SSD", graphics="NVIDIA GeForce4")
item4 = ElectronicItem(name="Smartwatch", weight=44, brand="Samsung", display="Touchscreen", battery_life="3 days", fitness_features="Heart Rate Monitor", connectivity="Bluetooth")
item5 = NonElectronicItem(name="Campus", weight=4, brand="Samsung", accuracy="High", price=50, materials=["iron", "plastic"])
item6 = NonElectronicItem('Passport',color="blue", weight=1, cost=50, bought_from="USA")
item7 = NonElectronicItem('Sunglasses',have_case="yes", color="black", origin="Italy", weight=10)
item8 = NonElectronicItem('Sneakers',brand="New Balance", is_new=False, bought_from="Spain", weight=14)

bag = Bag()


### good idea - but what is the point? in this implementation the keys are exactly the same as the values, so why put in dict?
items_dict = {
    'item1': item1,
    'item2': item2,
    'item3': item3,
    'item4': item4,
    'item5': item5,
    'item6': item6,
    'item7': item7,
    'item8': item8,
}

while True:
    print('Options:')
    print('1. Add item')
    print('2. Remove item')
    print('3. Print')
    print('4. Exit')

    choice = input('Enter your choice: ')

    if choice == '1':
        item_name = input('Enter item - item1 to item8 : ')
        if items_dict[item_name]:
            bag.add_item(items_dict[item_name])
        else:
            print('no such option')
            break
    elif choice == '2':
        item_name = input('Enter item - item1 to item8 : ')
        ### need better input valdation. try to enter "t", see what happens
        if items_dict[item_name]:
            bag.remove_item(items_dict[item_name])
        else:
            print('no such option')
            break
    elif choice == '3':
        print('OPTIONS: ')
        print('1. print all items in the bag')
        print('2. print by categories')
        print('3. print items in specific category')

        print_choice = input('Enter your choice: ')

        if print_choice == '1':
            bag.print_packed_items()
            continue
        if print_choice == '2':
            bag.print_by_category()
            continue
        if print_choice == '3':
            print('Category OPTIONS:')
            print('1. ElectronicItem')
            print('2. NonElectronicItem')

            cat_choice = input('Enter your choice: ')

            if cat_choice == '1':
                bag.print_items_from_cat(ElectronicItem)
                continue
            if cat_choice == '2':
                bag.print_items_from_cat(NonElectronicItem)
                continue
            else:
                print('no such option')
                break

        else:
            print('no such option')
            break

    elif choice == '4':
        break

    else:
        print('no such option')
        break
