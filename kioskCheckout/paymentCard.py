
class PaymentCard() :
    def __init__(self, cardNumber, nameOnCard, cardType, cardBank, cardStatus) :
        self.cardNumber = cardNumber
        self.nameOnCard = nameOnCard
        self.cardType = cardType
        self.cardBank = cardBank
        self.cardStatus = 'disapproved'

    def getCardNumber(self) :
        return self.cardNumber

    def getNameOnCard(self) :
        return self.nameOnCard

    def getCardType(self) :
        return self.cardType

    def getCardBank(self) :
        return self.cardBank

    def getCardStatus(self) :
        self.cardStatus

    def __str__(self):
        return self.cardNumber + self.nameOnCard + self.cardStatus

