is_hot = False
is_cold = True
if is_hot:
    print("It's a hot day. Drink plenty of water")
elif is_cold:
    print("It's a cold day. Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")

#%%
# Exercise
price = 1000000
good_credit = True
if good_credit:
    down_payment = price * 0.1
else:
    down_payment = price * 0.2

print(f"Down payment: ${down_payment}")