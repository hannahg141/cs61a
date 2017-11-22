############
# Mutation #
############

def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> w(90, 'hax0r')
    'Insufficient funds'
    >>> w(25, 'hwat')
    'Incorrect password'
    >>> w(25, 'hax0r')
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    """
    passwords = [password]
    incorrect = []
    def withdraw(amount, password_attempt): #pass in what I am comparing it too
        if len(incorrect) >= 3:
            return 'Your account is locked. Attempts: ' + str(incorrect)
        elif password_attempt == password:
            nonlocal balance
            if amount > balance:
                return 'Insufficient funds'
            balance -= amount
            return balance
        else:
            incorrect.append(password_attempt)
            return 'Incorrect password'

    return withdraw



def make_joint(withdraw, old_password, new_password):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    
    #this type(value) == int was testing to see if the withdraw funciton with my old
     #password would even work, returns an error lets just print that error
      #if it returns a number, it worked and will return joint_withdraw and go through mumbo jumbo
    value = withdraw(0, old_password)
    if type(value) == str:
        return value

    def joint_withdraw(amount, password):
        if password == old_password or password == new_password:
            return withdraw(amount, old_password)
        return withdraw(amount, password)

    return joint_withdraw
    

###########
# Objects #
###########

class VendingMachine(object):
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    #returns strings describing its interactions
    def __init__(self, item, price):
        self.item = item #the thing in the machine
        self.price = price #how much the thing costs
        self.stock = 0 #NOT PASSED IN, no change / item and price, how many of the thing are inside
        self.balance = 0 #NOT PASSED IN, no change / item and price, how much money has been put towards a purchase
        #item_name, price,

    def vend(self):
        if self.stock == 0:
            return 'Machine is out of stock.'
        if self.price > self.balance:
            return 'You must deposit $' + str(self.price - self.balance) + ' more.'
        else:
            self.stock -= 1 #self.item - 1? decrease the name by 1? NO decrease how much of the item I have by 1
            change = self.balance - self.price
            self.balance = 0
            if change == 0:
                return 'Here is your ' + str(self.item) + '.'
            else:
                return "Here is your " + str(self.item) + ' and $' + str(change) + ' change.'

    def restock(self, amount):
        self.stock += amount
        return 'Current ' + str(self.item) + ' stock: ' + str(self.stock)

    def deposit(self, amount):
        if self.stock < 1:
            return "Machine is out of stock. Here is your $" + str(amount) + '.'
        else:
            self.balance += amount
            return 'Current balance: $' + str(self.balance)

    


class MissManners:
    """A container class that only forward messages that say please.

    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'

    >>> m = MissManners(v)
    >>> m.ask('vend')
    'You must learn to say please first.'
    >>> m.ask('please vend')
    'You must deposit $10 more.'
    >>> m.ask('please deposit', 20)
    'Current balance: $20'
    >>> m.ask('now will you vend?')
    'You must learn to say please first.'
    >>> m.ask('please hand over a teaspoon')
    'Thanks for asking, but I know not how to hand over a teaspoon.'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'

    >>> double_fussy = MissManners(m) # Composed MissManners objects
    >>> double_fussy.ask('deposit', 10)
    'You must learn to say please first.'
    >>> double_fussy.ask('please deposit', 10)
    'Thanks for asking, but I know not how to deposit.'
    >>> double_fussy.ask('please please deposit', 10)
    'Thanks for asking, but I know not how to please deposit.'
    >>> double_fussy.ask('please ask', 'please deposit', 10)
    'Current balance: $10'
    """
    def __init__(self, obj):
        self.obj = obj

    def ask(self, message, *args):
        magic_word = 'please '
        if not message.startswith(magic_word):
            return 'You must learn to say please first.'
        elif message.startswith(magic_word):
            if hasattr(self.obj, message[7:]):
                return getattr(self.obj, message[7:])(*args) #self.obj.message(*args)
            else:
                return 'Thanks for asking, but I know not how to ' + message[7:] + '.'
        
       
#hasattr: are the arguments a string and in the attributes?
#getattr: returns the value of he named attribute
#of OBJECT and name- must be a string
#objects in python have attributes, i can access these by writing person.name (etc)
    #what if i dont know name of attribute?






