class StoreItem:
    def __init__(self, Item:str,Price:float):
        self.Item = Item
        self.Price = Price
        


chips = StoreItem("Chips", 1.99) # Don't modify this line

# TODO: Access the attributes of the chips object and display them

print(chips.Item)
print(chips.Price)
