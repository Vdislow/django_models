from credit.models import Client, Account, Credit
import random


def number_generator():
    numbers = []
    for i in range(16):
        numbers.append(str(random.randint(0, 9)))
    return "".join(numbers)


client1 = Client(name="Berdiev N.", birth_year=1994, work_place="Codify")
client1.save()
client2 = Client(name="Kan V.", birth_year=1996, work_place="Mediasign Group")
client2.save()

client1.account_set.create(number=number_generator())
client1.account_set.create(number=number_generator(), account_type=2)
client2.account_set.create(number=number_generator(), account_type=3)
client2.account_set.create(number=number_generator(), account_type=4)

credit1 = Account.objects.get(account_type=1)
credit2 = Account.objects.get(account_type=2)
credit3 = Account.objects.get(account_type=3)
credit4 = Account.objects.get(account_type=4)

credit1.credit_set.create(sum=600000)
credit2.credit_set.create(sum=80000)
credit3.credit_set.create(sum=300000)
credit4.credit_set.create(sum=69696969)


