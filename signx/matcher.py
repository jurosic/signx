from collections import Counter
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
    with open('signatures.json', 'r') as f:
        data = json.load(f)
        
    for name, sig in data.items():
        shorter = sig if len(sig) < len(signature) else signature
        longer = sig if len(sig) > len(signature) else signature
        
        matches = []
        
        for i, (x1, y1, _) in enumerate(shorter):
            x2, y2, _ = longer[i]
            if x1 != x2 or y1 != y2:
                matches.append(abs(x1 - x2) + abs(y1 - y2)/2)
        
        avg_distance = sum(matches)/len(matches)
        
        if avg_distance < 20:
            return name

    return None