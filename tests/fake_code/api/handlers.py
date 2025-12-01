"""API handlers with duplicates across directory boundaries."""

from typing import Dict, Any


# =============================================================================
# CROSS-DIRECTORY DUPLICATE (same as services.py fetch pattern)
# =============================================================================

def get_user_handler(user_id: int) -> Dict[str, Any]:
    """API handler to get user by ID."""
    try:
        # Simulated database call
        result = {"id": user_id, "name": "Test User"}
        if result is None:
            raise ValueError(f"User with id {user_id} not found")
        return {"status": "success", "data": result}
    except ConnectionError as e:
        print(f"Database connection failed: {e}")
        return {"status": "error", "message": str(e)}
    except TimeoutError as e:
        print(f"Database query timed out: {e}")
        return {"status": "error", "message": str(e)}
    except Exception as e:
        print(f"Unexpected error fetching user: {e}")
        return {"status": "error", "message": str(e)}


# =============================================================================
# RESPONSE BUILDING (repeated pattern with variations)
# =============================================================================

def build_success_response(data: Any, message: str = "Success") -> Dict:
    """Build a standardized success response."""
    return {
        "status": "success",
        "message": message,
        "data": data,
        "error": None,
        "timestamp": "2024-01-01T00:00:00Z"
    }


def build_error_response(error: str, code: int = 500) -> Dict:
    """Build a standardized error response."""
    return {
        "status": "error",
        "message": error,
        "data": None,
        "error": {"code": code, "details": error},
        "timestamp": "2024-01-01T00:00:00Z"
    }


def build_warning_response(data: Any, warning: str) -> Dict:
    """Build a standardized warning response."""
    return {
        "status": "warning",
        "message": warning,
        "data": data,
        "error": None,
        "timestamp": "2024-01-01T00:00:00Z"
    }


# =============================================================================
# VALIDATION DUPLICATE (from utils.py but with different docstring)
# =============================================================================

def check_valid_email(email):
    """Validate that an email address is properly formatted."""
    if "@" not in email:
        return False
    if "." not in email:
        return False
    return True


# =============================================================================
# LONG COMMENT BLOCK (tests that we don't match comments if configured)
# =============================================================================

# This is a very long comment block that explains the purpose of this module.
# The API handlers module provides HTTP endpoint handlers for the REST API.
# Each handler follows a similar pattern:
# 1. Parse and validate input parameters
# 2. Call the appropriate service layer function
# 3. Transform the result into a standardized response format
# 4. Handle any errors that occur during processing
# This pattern ensures consistency across all API endpoints.

def placeholder_handler():
    """A placeholder handler that does nothing."""
    pass

