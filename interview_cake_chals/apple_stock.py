'''I wanna know how much money I could have made yesterday if I'd been trading
 Apple stocks all day.

So I grabbed Apple's stock prices from yesterday and put them in a list called 
stock_prices, where:

The indices are the time (in minutes) past trade opening time, 
which was 9:30am local time.
The values are the price (in US dollars) of one share of Apple stock at that time.
So if the stock cost $500 at 10:30am, that means stock_prices[60] = 500.

Write an efficient function that takes stock_prices and returns the best profit
I could have made from one purchase and one sale of one share of Apple stock yesterday.

For example:

>>> stock_prices = [10, 7, 5, 8, 11, 9]
>>> get_max_profit(stock_prices)
6
>>> stock_prices = [10, 7, 5, 8, 4, 9]
>>> get_max_profit(stock_prices)
5

# Returns 6 (buying for $5 and selling for $11)

No "shorting"—you need to buy before you can sell. Also, you can't buy and sell in the same time step—at least 1 minute has to pass.'''

def get_max_profit(stock_prices):

    if len(stock_prices) < 2:
        raise ValueError('Getting a profit requires at least 2 prices')

    max_val = 0 
    min_val = stock_prices[0]
    max_indx = None
    
    for i in range(1, len(stock_prices)):
        if stock_prices[i] > max_val:
            max_val = stock_prices[i]
            max_indx = i
    
    for i, price in enumerate(stock_prices):
        if i >= max_indx:
            break
        if price < min_val:
            min_val = price
            

    return (max_val - min_val)








if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print('***\n TEST PASSED***\n')