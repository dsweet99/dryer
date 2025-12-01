"""Service layer with intentional duplicates for testing."""

from typing import Dict, List, Any, Optional


# =============================================================================
# LONG DUPLICATE FROM utils.py (near-miss: small edits throughout)
# =============================================================================

def compute_order_total(order_items, tax_percentage, promo_code=None):
    """
    Calculate the total price for an order including tax and discounts.
    
    This is a longer function that demonstrates detection of substantial
    code blocks that have been duplicated across the codebase.
    """
    subtotal = 0.0
    
    for item in order_items:
        item_price = item.get("price", 0)
        item_qty = item.get("quantity", 1)
        item_discount = item.get("discount", 0)
        
        line_total = item_price * item_qty
        line_total -= line_total * (item_discount / 100)
        subtotal += line_total
    
    # Apply promo code if provided
    if promo_code:
        if promo_code == "SAVE10":
            subtotal *= 0.90
        elif promo_code == "SAVE20":
            subtotal *= 0.80
        elif promo_code == "HALFOFF":
            subtotal *= 0.50
    
    # Calculate tax
    tax_amount = subtotal * tax_percentage
    total = subtotal + tax_amount
    
    return {
        "subtotal": round(subtotal, 2),
        "tax": round(tax_amount, 2),
        "total": round(total, 2)
    }


# =============================================================================
# MEDIUM DUPLICATE (error handling pattern repeated 3x in this file)
# =============================================================================

def fetch_user_by_id(user_id: int) -> Optional[Dict]:
    """Fetch a user by ID from the database."""
    try:
        # Simulated database call
        result = {"id": user_id, "name": "Test User"}
        if result is None:
            raise ValueError(f"User with id {user_id} not found")
        return result
    except ConnectionError as e:
        print(f"Database connection failed: {e}")
        return None
    except TimeoutError as e:
        print(f"Database query timed out: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error fetching user: {e}")
        return None


def fetch_product_by_id(product_id: int) -> Optional[Dict]:
    """Fetch a product by ID from the database."""
    try:
        # Simulated database call
        result = {"id": product_id, "name": "Test Product"}
        if result is None:
            raise ValueError(f"Product with id {product_id} not found")
        return result
    except ConnectionError as e:
        print(f"Database connection failed: {e}")
        return None
    except TimeoutError as e:
        print(f"Database query timed out: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error fetching product: {e}")
        return None


def fetch_order_by_id(order_id: int) -> Optional[Dict]:
    """Fetch an order by ID from the database."""
    try:
        # Simulated database call
        result = {"id": order_id, "status": "pending"}
        if result is None:
            raise ValueError(f"Order with id {order_id} not found")
        return result
    except ConnectionError as e:
        print(f"Database connection failed: {e}")
        return None
    except TimeoutError as e:
        print(f"Database query timed out: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error fetching order: {e}")
        return None


# =============================================================================
# VERY SIMILAR LOOPS (same structure, different operations)
# =============================================================================

def summarize_sales(transactions: List[Dict]) -> Dict[str, float]:
    """Summarize sales data from transactions."""
    total_revenue = 0.0
    total_units = 0
    total_discounts = 0.0
    
    for txn in transactions:
        amount = txn.get("amount", 0)
        units = txn.get("units", 0)
        discount = txn.get("discount", 0)
        
        total_revenue += amount
        total_units += units
        total_discounts += discount
    
    return {
        "total_revenue": total_revenue,
        "total_units": total_units,
        "total_discounts": total_discounts,
        "average_transaction": total_revenue / len(transactions) if transactions else 0
    }


def summarize_expenses(transactions: List[Dict]) -> Dict[str, float]:
    """Summarize expense data from transactions."""
    total_spent = 0.0
    total_items = 0
    total_taxes = 0.0
    
    for txn in transactions:
        amount = txn.get("amount", 0)
        items = txn.get("items", 0)
        tax = txn.get("tax", 0)
        
        total_spent += amount
        total_items += items
        total_taxes += tax
    
    return {
        "total_spent": total_spent,
        "total_items": total_items,
        "total_taxes": total_taxes,
        "average_transaction": total_spent / len(transactions) if transactions else 0
    }

