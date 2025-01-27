

class Card:
    def __init__(self,number,expiry,cvv2,person,balance):
        self.number=number
        self.expiry=expiry
        self.cvv2=cvv2
        self.person=person 
        self.balance=balance
    
cards =[Card("1234567890123456","12/25","1232","roghaye", 6000),
Card("2345678901234567","11/24","2344","reyhane", 4000),
Card("3456789012345678","10/23","3451","sahar", 8000),
Card("4567890123456789","09/26","4568","asal", 3000)]

for card in cards:
    if card.balance>5000:
        print(f"person:{card.person},Number:{card.number},Balance:{card.balance}")