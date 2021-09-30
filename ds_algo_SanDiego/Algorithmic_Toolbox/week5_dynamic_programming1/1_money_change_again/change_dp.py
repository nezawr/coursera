# Uses python3
import sys

def get_change(money):
    coins = [1,3,4]
    min_num_coins = [0]  * (money + 1)
    for m in range(1, money+1):
        min_num_coins[m] = float('inf')
        for coin in coins:
            if m >= coin:
                num_coin = min_num_coins[m - coin] + 1
                if num_coin < min_num_coins[m]:
                    min_num_coins[m] = num_coin
    return min_num_coins[money]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
