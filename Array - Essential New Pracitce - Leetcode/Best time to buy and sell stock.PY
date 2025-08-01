def maxProfit(arr):
    if not arr or len(arr) < 2:
        return 0

    min_price = arr[0]
    max_profit = 0

    for i in range(1, len(arr)):
        current_price = arr[i]

        # Update the minimum price if a lower price is found
        if current_price < min_price:
            min_price = current_price
        # Calculate potential profit and update max_profit
        else:
            profit = current_price - min_price
            if profit > max_profit:
                max_profit = profit
    
    return max_profit
