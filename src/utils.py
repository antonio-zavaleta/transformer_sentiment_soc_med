def log_message(message):
    print(f"[LOG] {message}")

def save_to_file(data, filename):
    with open(filename, 'w') as f:
        f.write(data)

def load_from_file(filename):
    with open(filename, 'r') as f:
        return f.read()

def validate_data(data):
    if not data:
        raise ValueError("Data cannot be empty.")
    return True