import time


def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    result = {}
    for coin in coins:
        count = amount // coin
        if count:
            result[coin] = count
            amount -= coin * count
    return result


def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [0] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    result = {}
    i = amount
    while i > 0:
        c = coin_used[i]
        result[c] = result.get(c, 0) + 1
        i -= c
    return result


def test_algorithms(amount, coins):
    start = time.time()
    greedy_result = find_coins_greedy(amount, coins)
    greedy_time = time.time() - start

    start = time.time()
    dp_result = find_min_coins(amount, coins)
    dp_time = time.time() - start

    print(f"Greedy: {greedy_result}, Time: {greedy_time:.6f}s")
    print(f"DP: {dp_result}, Time: {dp_time:.6f}s")


if __name__ == "__main__":
    amount = 113
    coins = [50, 25, 10, 5, 2, 1]
    print("Жадібний алгоритм:", find_coins_greedy(amount, coins))
    print("Динамічне програмування:", find_min_coins(amount, coins))
    test_algorithms(10000, coins)
