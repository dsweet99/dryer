"""Utility functions with intentional duplicates for testing."""

# =============================================================================
# SHORT DUPLICATES (will appear in models.py too)
# =============================================================================

def validate_email(email):
    """Check if email is valid."""
    if "@" not in email:
        return False
    if "." not in email:
        return False
    return True


def validate_phone(phone):
    """Check if phone is valid."""
    if len(phone) < 10:
        return False
    if not phone.replace("-", "").isdigit():
        return False
    return True


# =============================================================================
# SAME-FILE DUPLICATE (copy-pasted with minor changes)
# =============================================================================

def process_user_data_v1(user_dict):
    """Process user data and return cleaned version."""
    result = {}
    for key, value in user_dict.items():
        if value is None:
            continue
        if isinstance(value, str):
            result[key] = value.strip().lower()
        elif isinstance(value, (int, float)):
            result[key] = value
        else:
            result[key] = str(value)
    return result


def process_user_data_v2(user_dict):
    """Process user data and return cleaned version."""
    result = {}
    for key, value in user_dict.items():
        if value is None:
            continue
        if isinstance(value, str):
            result[key] = value.strip().upper()  # <- only diff: upper vs lower
        elif isinstance(value, (int, float)):
            result[key] = value
        else:
            result[key] = str(value)
    return result


# =============================================================================
# LONG DUPLICATE (will appear in services.py with small edits)
# =============================================================================

def calculate_order_total(items, tax_rate, discount_code=None):
    """
    Calculate the total price for an order including tax and discounts.
    
    This is a longer function that demonstrates detection of substantial
    code blocks that have been duplicated across the codebase.
    """
    subtotal = 0.0
    
    for item in items:
        item_price = item.get("price", 0)
        item_quantity = item.get("quantity", 1)
        item_discount = item.get("discount", 0)
        
        line_total = item_price * item_quantity
        line_total -= line_total * (item_discount / 100)
        subtotal += line_total
    
    # Apply discount code if provided
    if discount_code:
        if discount_code == "SAVE10":
            subtotal *= 0.90
        elif discount_code == "SAVE20":
            subtotal *= 0.80
        elif discount_code == "HALFOFF":
            subtotal *= 0.50
    
    # Calculate tax
    tax_amount = subtotal * tax_rate
    total = subtotal + tax_amount
    
    return {
        "subtotal": round(subtotal, 2),
        "tax": round(tax_amount, 2),
        "total": round(total, 2)
    }

