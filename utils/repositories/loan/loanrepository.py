from api.models.loan import Loan

class LoanRepository():
    
    
    def get_customer_loans(pk: int):
        try:
            listCustomerLoan = Loan.objects.filter(id=pk)
            return listCustomerLoan
        except:
            return []