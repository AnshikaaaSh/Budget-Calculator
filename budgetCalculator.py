import os
class Budget(object):
    def __init__(self):
        os.system('cls')
        self.budget =float(input("How much is your budget?\n"))
        self.spending=self.budget*0.5
        self.main()
        
    def main(self):
        os.system('cls')
        print("This calculator follows the 50-20-30 budget rule.\n")
        print("Your total budget is \nRs", '{:.2f}'.format(self.budget))
        main_option= int(input('\nWhat do you want to do? \n 1) View overall budget \n 2) View spending budget'))
        if main_option ==1:
            self.overall_budget()
        elif main_option ==2:
            self.spending_budget()
        else:
            quit 
            
    def overall_budget(self):
        os.system('cls')
        option=int(input('How much do you want to save?\n1) 20%\n2) 30%'))
        if option ==1:
            self.saving=0.2
        elif option ==2:
            self.saving =0.3
        else:
            print("Error. Please select only 1 or 2!")
        self.final_saving= self.budget * self.saving
        self.extra=self.budget- self.final_saving - self.spending
        print('\nSpending: Rs', '{:.2f}'.format(self.spending), '\nTo save: Rs', '{:.2f}'.format(self.final_saving), '\nExtra: Rs', '{:.2f}'.format(self.extra))
        os.system('pause')
        
    def spending_budget(self):
        os.system('cls')
        print('Soending Budget: Rs', '{:.2f}'.format(self.spending))
        rent= float(input("\n how much rent do you pay?\n"))
        bills= float(input("\n how much are your monthly expenses and bills?\n"))
        groceries= self.spending - rent-bills
        print('Spending Budget: Rs', '{:.2f}'.format(rent), '\nBills: Rs', '{:.2f}'.format(bills), '\nGroCerires: Rs', '{:.2f}'.format(groceries))
        os.system('pause')
        self.main()
            
Budget()