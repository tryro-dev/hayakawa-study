import json
from item_info import ItemInfo

with open('shop_item.json', 'r', encoding = 'utf-8') as shop_item:
    json_data = json.load(shop_item)
    

item_list=[]    
for item in json_data.get('items', []):
    item_obj = ItemInfo(
        item_id = item['item_id'],
        item_name = item['item_name'],
        item_price = item['item_price']
    )
    item_list.append(item_obj)
    
for item in item_list:
    item.display_info()

selected_item = None

def item_select():
    while True:
        buy_sell_choice = input('購入しますか？売却しますか？ （0=購入, 1=売却）')
        if buy_sell_choice == '0':
            buy_sell = '購入'
            break
        elif buy_sell_choice == '1':
            buy_sell = '売却'
            break
        else:
            print('0か1で入力してください')
        
    while True:
        order_item_id = input(str(buy_sell) + 'するアイテム番号を入力してください: ') 
        try:
            order_item_id = int(order_item_id)
        except:
            print('1~12の半角数字で入力してください')
            return item_select()
        if order_item_id < 1 or order_item_id > 12:
            print('アイテム番号は1~12です')
            return item_select()
    
        selected_item = next(
            (item for item in item_list if item.item_id == order_item_id),
            None
        )
        if selected_item == None :
            print('該当するアイテムがありません')
    
        else:
            selected_item.display_info()
            return selected_item, buy_sell

def item_count(selected_item,buy_sell ):
    math = 0
    while math == 0:   
        count = (input('個数を入力してください: '))
        try:
            count = int(count)
            math = 1
        except:
            print('半角数字で入力してください')
            return item_count(selected_item)
        if count < 1 :
            print('入力された個数が正しくありません')
            return item_count(selected_item)

        selected_and_count_total = selected_item.item_price * count
        print(selected_item.item_name + 'を' + str(count) + '個' + str(buy_sell) + 'しました')
        print('合計金額は' + str(selected_and_count_total) + 'Gです')
    


def shopping_choice():
        flag = 0
        while flag == 0:
            selected_item, buy_sell = item_select()
            item_count(selected_item, buy_sell)
            
            while True:
            
                choice = (input('買い物を続けますか？(0:いいえ, 1:はい)'))
                if choice == '0' :
                    print('終了します')
                    flag = 1
                    break
                elif  choice == '1':
                    break
                else :
                    print('0か1を入力してください')
            
shopping_choice()
        