def maxBottles(numBottles, numExchange):
    full = numBottles
    empty = 0
    total = 0
    exchange = numExchange

    while full > 0 or empty >= exchange:
        if full > 0:
            total += 1
            empty += 1
            full = 0