"""Data models with intentional duplicates for testing."""

from dataclasses import dataclass
from typing import Optional, List


# =============================================================================
# SHORT DUPLICATE FROM utils.py (exact copy)
# =============================================================================

def validate_email(email):
    """Check if email is valid."""
    if "@" not in email:
        return False
    if "." not in email:
        return False
    return True


# =============================================================================
# SHORT DUPLICATE FROM utils.py (near-miss: variable renamed)
# =============================================================================

def validate_phone_number(phone_number):
    """Check if phone is valid."""
    if len(phone_number) < 10:
        return False
    if not phone_number.replace("-", "").isdigit():
        return False
    return True


# =============================================================================
# MEDIUM-LENGTH SAME-FILE DUPLICATES (config parsing)
# =============================================================================

def parse_database_config(config_dict):
    """Parse database configuration from dict."""
    host = config_dict.get("host", "localhost")
    port = config_dict.get("port", 5432)
    username = config_dict.get("username", "admin")
    password = config_dict.get("password", "")
    database = config_dict.get("database", "main")
    
    connection_string = f"postgresql://{username}:{password}@{host}:{port}/{database}"
    return connection_string


def parse_cache_config(config_dict):
    """Parse cache configuration from dict."""
    host = config_dict.get("host", "localhost")
    port = config_dict.get("port", 6379)
    username = config_dict.get("username", "admin")
    password = config_dict.get("password", "")
    database = config_dict.get("database", "0")
    
    connection_string = f"redis://{username}:{password}@{host}:{port}/{database}"
    return connection_string


# =============================================================================
# DATA CLASSES (structural similarity but different fields)
# =============================================================================

@dataclass
class User:
    id: int
    username: str
    email: str
    created_at: str
    updated_at: str
    is_active: bool = True
    
    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "is_active": self.is_active,
        }
    
    def validate(self):
        if not self.username:
            raise ValueError("Username is required")
        if not self.email:
            raise ValueError("Email is required")
        return True


@dataclass
class Product:
    id: int
    name: str
    price: float
    created_at: str
    updated_at: str
    is_active: bool = True
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "is_active": self.is_active,
        }
    
    def validate(self):
        if not self.name:
            raise ValueError("Name is required")
        if self.price < 0:
            raise ValueError("Price must be positive")
        return True


# =============================================================================
# VERY DIFFERENT (control - should NOT match anything)
# =============================================================================

def fibonacci(n: int) -> int:
    """Calculate nth Fibonacci number recursively."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def quicksort(arr: List[int]) -> List[int]:
    """Sort a list using quicksort algorithm."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

