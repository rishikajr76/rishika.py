def get_coins(amount):
    coins = [5, 2, 1]
    count = {}
    for coin in coins:
        count[coin] = amount // coin
        amount %= coin
    return count

amount = int(input("Enter the amount of money:"))
count = get_coins(amount)

print("Coins distribution:")
for coin, count in count.items():
    print(f'{coin} rupee coin: {count}')