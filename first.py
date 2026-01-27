class AuctionSystem:

    def __init__(self):
        self.items={}

    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
        if itemId not in self.items:
            self.items[itemId]={userId:bidAmount}
        else:
            if userId not in self.items[itemId]:
                self.items[itemId]={userId:bidAmount}
            else:
                self.items[itemId][userId]=bidAmount


    def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
        self.items[itemId][userId]=newAmount

    def removeBid(self, userId: int, itemId: int) -> None:
        self.items[itemId].pop(userId)

    def getHighestBidder(self, itemId: int) -> int:
        if itemId not in self.items:
            return -1
        li_tu=[[value,key] for key,value in  self.items[itemId].items()]
        print(li_tu)
        li_tu.sort(key=lambda x: (x[0], x[1]), reverse=True)
        return li_tu[0][0]



# Your AuctionSystem object will be instantiated and called as such:
userId=1
itemId=7
bidAmount=5
newAmount=8
obj = AuctionSystem()
obj.addBid(userId,itemId,bidAmount)
print(obj.items)
obj.updateBid(userId,itemId,newAmount)
print(obj.items)
obj.removeBid(userId,itemId)
print(obj.items)
param_4 = obj.getHighestBidder(itemId)
print(param_4)