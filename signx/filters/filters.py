def remove_leading_duplicates(data):
    """_summary_
    Removes leading duplicates from a serialized signature.
    Args:
        data (tuple(int, int, (float, float))): The serialized signature.
    Returns:
        tuple(int, int, (float, float)): The serialized signature without leading duplicates.
    """
    
    first = data[0]
    for i, d in enumerate(data):
        if d != first:
            return data[i:]