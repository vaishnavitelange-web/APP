# Define a function named knapsack that takes weights, profits, and bag capacity as input
def knapsack(weights, profits, capacity):

    # Find the total number of items using len() function
    n = len(weights)

    # Create a 2D DP table with (n+1) rows and (capacity+1) columns
    # Initially, all values are set to 0
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Start a loop for each item
    # i represents the current item number
    for i in range(1, n + 1):

        # Start a loop for every possible bag capacity from 0 to the given capacity
        for w in range(capacity + 1):

            # Check whether the current item's weight is greater than the current capacity
            if weights[i-1] > w:

                # If the item is too heavy, we cannot include it
                # So, copy the answer from the previous row
                dp[i][w] = dp[i-1][w]

            # If the current item can fit inside the bag
            else:

                # We have two choices:
                # 1. Do not take the current item
                # 2. Take the current item
                # max() selects the choice that gives higher profit
                dp[i][w] = max(
                    dp[i-1][w],  # Case 1: Exclude the current item
                    profits[i-1] + dp[i-1][w - weights[i-1]]  # Case 2: Include the current item
                )

    # Start from the full capacity of the bag
    # We will use this value while finding which items were selected
    w = capacity

    # Create an empty list to store the selected item indexes
    selected_items = []

    # Start checking the DP table from the last item towards the first item
    # -1 means we move backwards
    for i in range(n, 0, -1):

        # If the value in the current row is different from the previous row,
        # it means the current item was included in the optimal solution
        if dp[i][w] != dp[i-1][w]:

            # Add the current item's index to the selected_items list
            # i-1 is used because Python list indexing starts from 0
            selected_items.append(i-1)

            # Reduce the remaining capacity by the weight of the selected item
            w -= weights[i-1]

    # The items were found in reverse order during backtracking
    # Reverse the list to display them in their original order
    selected_items.reverse()

    # Return two values:
    # 1. Maximum profit
    # 2. List of selected item indexes
    return dp[n][capacity], selected_items


# Create a list containing the weights of all items
weights = [3, 2, 4, 5, 1]

# Create a list containing the profits/values of all items
profits = [50, 40, 70, 80, 10]

# Define the maximum capacity of the knapsack/bag
capacity = 7

# Call the knapsack function
# Store the returned maximum profit in max_profit
# Store the selected item indexes in items
max_profit, items = knapsack(weights, profits, capacity)

# Display the maximum profit obtained
print("Maximum Profit:", max_profit)

# Display the indexes of the items selected in the knapsack
print("Items in Knapsack:", items)