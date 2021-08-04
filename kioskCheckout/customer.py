class Customer():
    def __init__(self, customerName, customerLastName, customerEmail, customerPhoneNo):
        self.customerName = customerName
        self.customerLastName = customerLastName
        self.customerEmail = customerEmail
        self.customerPhoneNo = customerPhoneNo

    def getCustomerName(self):
        return self.customerName

    def getCustomerLastName(self):
        return self.customerLastName

    def getCustomerEmail(self):
        return self.customerEmail
        
    def getCustomerPhoneNo(self):
        return self.customerPhoneNo

    def __str__(self):
        return self.customerName
