class Payment:
    debit=0
    credit = 0
    total_fees = 0

    def __init__(self, fees):
        if fees > 0.5 * self.total_fees:
            self.fees = fees
        else:
            self.fees = 0
    
    @classmethod
    def set_total_fees(cls, lib_fee, med_fee, tuition, func_fee):
        cls.total_fees = lib_fee+med_fee+tuition+func_fee
    
    def get_total_fee(self):
        return self.total_fees
    
    def set_debit(self):
        if self.fees < self.total_fees:
            self.debit = self.total_fees - self.fees

    def get_debit(self):
        self.set_debit()
        return self.debit

    def set_credit(self):
        if self.fees > self.total_fees:
            self.credit = self.fees - self.total_fees

    def get_credit(self):
        self.set_credit()
        return self.credit
    

    def __str__(self):
        return f'Fees Paid: {self.fees}\nCredit: {self.get_credit()}\nDebit: {self.get_debit()}'

Payment.set_total_fees(50, 100, 600, 60)
pay1 = Payment(950)
print(pay1, '\n\n')
pay2 = Payment(200)
print(pay2)