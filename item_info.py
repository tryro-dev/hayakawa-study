class ItemInfo:
    
    def __init__(self, item_id : int, item_name : str, item_price : int):
        
        self.item_id = item_id
        self.item_name = item_name
        self.item_price = item_price
    
    def display_info(self):
        print(str(self.item_id) + '.' + str(self.item_name) + str(self.item_price) + 'G')
        
        
        
        
        