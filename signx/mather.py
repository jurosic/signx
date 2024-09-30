import json

def create_database():
    """Create a database for signatures"""
    with open('signatures.json', 'w+') as f:
        f.write("{}")
        
def register_signature(name, signature):
    """Register a signature to the database"""
    with open('signatures.json', 'r') as f:
        data = json.load(f)
    data[name] = signature
    with open('signatures.json', 'w+') as f:
        json.dump(data, f)
        
def match_signature(signature):
    """Match a signature to the database"""
    with open('signatures.json', 'r') as f:
        data = json.load(f)
    
    # Compare the signature to all signatures in the database, and return the closest match
    closest_match = None
    closest_distance = 999999
    for name, sig in data.items():
        distance = 0
        for i, (x1, y1, _) in enumerate(sig):
            x2, y2, _ = signature[i]
            distance += (x1 - x2)**2 + (y1 - y2)**2
        if distance < closest_distance:
            closest_match = name
            closest_distance = distance
    
    return None