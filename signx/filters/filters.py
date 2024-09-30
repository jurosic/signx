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
        
def crop_to_content(data):
    """_summary_
    Crop the signature to the content.
    Args:
        data (tuple(int, int, (float, float))): The serialized signature.
    Returns:
        tuple(int, int, (float, float)): The cropped signature.
    """
    
    min_x, min_y, max_x, max_y = 999999, 999999, 0, 0
    for x, y, _ in data:
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)
    return [(x - min_x, y - min_y, (dx, dy)) for x, y, (dx, dy) in data]
