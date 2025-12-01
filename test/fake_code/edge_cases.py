"""Edge cases for duplicate detection testing."""


# =============================================================================
# VERY SHORT DUPLICATES (may be below threshold)
# =============================================================================

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b


# =============================================================================
# WHITESPACE VARIATIONS (should match after normalization)
# =============================================================================

def spaced_out_function(   x,    y,     z   ):
    """Function with extra whitespace."""
    result    =    x   +   y   +   z
    return     result


def compact_function(x,y,z):
    """Function with minimal whitespace."""
    result=x+y+z
    return result


# The normalized versions should be similar:
# def spaced_out_function(x, y, z):
#     result = x + y + z
#     return result


# =============================================================================
# TRIPLE DUPLICATE (same code 3 times with minor variations)
# =============================================================================

def log_event_info(event_name, event_data, timestamp):
    """Log an info-level event."""
    formatted = f"[INFO] {timestamp}: {event_name}"
    print(formatted)
    for key, value in event_data.items():
        print(f"  {key}: {value}")
    return formatted


def log_event_warning(event_name, event_data, timestamp):
    """Log a warning-level event."""
    formatted = f"[WARN] {timestamp}: {event_name}"
    print(formatted)
    for key, value in event_data.items():
        print(f"  {key}: {value}")
    return formatted


def log_event_error(event_name, event_data, timestamp):
    """Log an error-level event."""
    formatted = f"[ERROR] {timestamp}: {event_name}"
    print(formatted)
    for key, value in event_data.items():
        print(f"  {key}: {value}")
    return formatted


# =============================================================================
# UNICODE AND SPECIAL CHARACTERS
# =============================================================================

def greet_user_english(name):
    """Greet the user in English."""
    message = f"Hello, {name}! Welcome to our application."
    print(message)
    return message


def greet_user_spanish(nombre):
    """Greet the user in Spanish."""
    message = f"¡Hola, {nombre}! Bienvenido a nuestra aplicación."
    print(message)
    return message


def greet_user_japanese(namae):
    """Greet the user in Japanese."""
    message = f"こんにちは、{namae}さん！アプリへようこそ。"
    print(message)
    return message


# =============================================================================
# NESTED DUPLICATES (duplicate inside a duplicate)
# =============================================================================

def outer_process_a(data):
    """Outer processing function A."""
    # Pre-processing
    cleaned = [x.strip() for x in data if x]
    
    # Inner duplicate block
    result = []
    for item in cleaned:
        if item.startswith("#"):
            continue
        if not item:
            continue
        result.append(item.lower())
    
    return result


def outer_process_b(data):
    """Outer processing function B."""
    # Pre-processing (slightly different)
    cleaned = [x.strip() for x in data if x is not None]
    
    # Inner duplicate block (same as above)
    result = []
    for item in cleaned:
        if item.startswith("#"):
            continue
        if not item:
            continue
        result.append(item.lower())
    
    return result


# =============================================================================
# COMPLETELY UNIQUE (control group - no matches expected)
# =============================================================================

class BinarySearchTree:
    """A completely unique implementation that shouldn't match anything."""
    
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = {"value": value, "left": None, "right": None}
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if value < node["value"]:
            if node["left"] is None:
                node["left"] = {"value": value, "left": None, "right": None}
            else:
                self._insert_recursive(node["left"], value)
        else:
            if node["right"] is None:
                node["right"] = {"value": value, "left": None, "right": None}
            else:
                self._insert_recursive(node["right"], value)
    
    def search(self, value):
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        if node is None:
            return False
        if value == node["value"]:
            return True
        if value < node["value"]:
            return self._search_recursive(node["left"], value)
        return self._search_recursive(node["right"], value)

