def best_stock(a):
    """Check which stocks cost more."""
    
    return max(a, key=lambda key: a[key])

"""
Previous solution:

    max_value = max(a.values())
    for key, val in a.items():
        if val == max_value:
            return key
"""

print(best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}))    # ATX
print(best_stock({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}))    # TASI
