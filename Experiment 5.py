# Experiment 5
# Longest Common Subsequence (LCS)
# Using Dynamic Programming

def lcs(X, Y):

    # Find the length of both strings
    m = len(X)
    n = len(Y)

    # Create a DP table
    # Extra row and column are used for empty strings
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            # If characters are same
            if X[i - 1] == Y[j - 1]:

                # Take diagonal value and add 1
                dp[i][j] = dp[i - 1][j - 1] + 1

            else:

                # Characters are different
                # Take maximum of top and left cell
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Start from bottom-right corner
    i = m
    j = n

    # List to store the LCS characters
    result = []

    # Backtracking to find the actual LCS
    while i > 0 and j > 0:

        # If characters match
        if X[i - 1] == Y[j - 1]:

            # Add character to result
            result.append(X[i - 1])

            # Move diagonally
            i -= 1
            j -= 1

        # If top cell is greater
        elif dp[i - 1][j] > dp[i][j - 1]:

            # Move up
            i -= 1

        else:

            # Move left
            j -= 1

    # Backtracking gives the string in reverse order
    result.reverse()

    # Convert list into a string
    lcs_string = ''.join(result)

    # Return LCS length and actual LCS
    return dp[m][n], lcs_string


# --------------------------------
# Main Program
# --------------------------------

# Take first string from user
X = input("Enter first string: ")

# Take second string from user
Y = input("Enter second string: ")

# Find LCS
length, sequence = lcs(X, Y)

# Display result
print("\nLength of LCS:", length)
print("Longest Common Subsequence:", sequence)