#!/usr/bin/python3
'''LockBoxes Challenge'''

def canUnlockAll(boxes):
    '''
    Determines whether all the boxes can be opened or not.

    Args:
        boxes (list of lists): A list of lockboxes, where each box is represented as a list of keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    '''
    # Get the total number of lockboxes
    num_boxes = len(boxes)
    
    # Create a set to keep track of keys we have
    keys = set()
    
    # List to store the indices of opened boxes
    opened_boxes = []
    
    # Start with the first box (index 0)
    i = 0
    
    # Loop until we can't open any more boxes
    while i < num_boxes:
        old_i = i
        
        # Mark the current box as opened
        opened_boxes.append(i)
        
        # Update our set of keys with the keys from the current box
        keys.update(boxes[i])
        
        # Check each key in our set
        for key in keys:
            # If the key is valid (not 0 and within the range of boxes)
            # and we haven't opened the box it unlocks yet
            if key != 0 and key < num_boxes and key not in opened_boxes:
                i = key  # Move to the box unlocked by this key
                break  # Exit the loop to process the new box
        
        # If we didn't move to a new box in this iteration, we can't open more boxes
        if old_i != i:
            continue
        else:
            break
    
    # Check if there are unopened boxes (except the first one, index 0)
    for i in range(num_boxes):
        if i not in opened_boxes and i != 0:
            return False
    
    # If all boxes can be opened, return True
    return True
