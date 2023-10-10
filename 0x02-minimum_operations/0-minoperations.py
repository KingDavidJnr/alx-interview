#!/usr/bin/python3
'''Minimum Operations python3 challenge'''

def minOperations(n):
    '''
    Calculates the fewest number of operations needed to result
    in exactly n 'H' characters in this file.

    Args:
        n (int): The desired number of 'H' characters.

    Returns:
        int: The minimum number of operations required to achieve n 'H' characters,
             or 0 if it's impossible to achieve n.
    '''

    # Initialize variables to keep track of state and count operations.
    pasted_chars = 1  # How many characters are currently in the file.
    clipboard = 0     # How many 'H' characters are copied to the clipboard.
    counter = 0       # Operations counter.

    # Continue looping until the desired number of 'H' characters is achieved.
    while pasted_chars < n:
        # If nothing is copied to the clipboard yet.
        if clipboard == 0:
            # Copy all 'H' characters in the file.
            clipboard = pasted_chars
            # Increment the operations counter.
            counter += 1

        # If only one character is in the file.
        if pasted_chars == 1:
            # Paste the contents of the clipboard.
            pasted_chars += clipboard
            # Increment the operations counter.
            counter += 1
            # Continue to the next iteration of the loop.
            continue

        remaining = n - pasted_chars  # Calculate the remaining characters needed to paste.

        # Check if it's impossible to achieve the desired number of 'H' characters
        # by checking if the clipboard has more characters than needed to reach n.
        # This means the number of characters in the file is equal to or greater
        # than what is in the clipboard, making it impossible.
        if remaining < clipboard:
            return 0

        # If the remaining characters can't be divided evenly by the current
        # number of characters in the file, paste the clipboard.
        if remaining % pasted_chars != 0:
            # Paste the current contents of the clipboard.
            pasted_chars += clipboard
            # Increment the operations counter.
            counter += 1
        else:
            # Copy all 'H' characters in the file to the clipboard.
            clipboard = pasted_chars
            # Paste the contents of the clipboard.
            pasted_chars += clipboard
            # Increment the operations counter by 2 because both copy and paste occurred.

    # If the desired result (n 'H' characters) is achieved, return the operations counter.
    if pasted_chars == n:
        return counter
    else:
        # If it's not possible to achieve n, return 0.
        return 0
