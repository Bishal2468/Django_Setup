class Stocks:

    def  __init__(self,name,price,open,close):
        self.name = name
        self.price = price
        self.open = open
        self.close = close
        self.company = self.Company() # creating a instance company with a class Company

    def fundamental_analysis(self):
        print(f"Company name:{self.name} ")
        print(f"Market Price:{self.price} ")
        print("Opening price:{open}".format(open = self.open))
        print(f"Closing Price:{self.close} ")
        ntc.company.show()

    class Company:
        def __init__(self):
            self.company_name ="Nepal Telecom"
            self.contact = 9845856545

        def show(self):
            print(f"Company Name: {self.company_name} contact: {self.contact}" )



ntc = Stocks("ntc","894","899","854")
nabil = Stocks("nabil",598,602,450)
ntc.fundamental_analysis()
