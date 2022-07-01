from numpy import append

def lemonadeChange(bills):
        PRICE = 5
        changes=[]

        for customer in bills:
            if(customer== 5):
                changes.append(5)

            elif(customer == 10):
                if(5 in changes):
                    changes.append(customer)
                    changes.remove(5)
                else:
                    return False
            elif(customer == 20):
                if(10 in changes and 5 in changes):
                    changes.append(20)
                    changes.remove(10)
                    changes.remove(5)
                
                elif(changes.count(5) >= 3):
                    changes.append(20)
                    changes.remove(5)
                    changes.remove(5)
                    changes.remove(5)

                else:
                    return False
        return True