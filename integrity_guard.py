import hashlib

def calculate_fingerprint(filename):
    """This function creates a unique digital fingerprint (Hash) for a file."""
    try:

        sha256_hash = hashlib.sha256()
        with open(filename, "rb") as f:
            
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None

print("--- Ethio-Safe File Integrity Guard ---")
file_to_check = input("Enter the name of the file to protect (e.g., test.txt):
initial_hash = calculate_fingerprint(file_to_check)

if initial_hash:
    print(f"\n[SUCCESS] Original Fingerprint: {initial_hash}")
    print("\nNow, go change one single letter in that file and save it.")
    input("Press Enter once you have changed the file...")

    new_hash = calculate_fingerprint(file_to_check)
    
    print(f"[CHECKING] New Fingerprint: {new_hash}")

    if initial_hash == new_hash:
        print("\n SAFE: The file has NOT been changed.")
     else:
        print("\n ALERT: The file has been TAMPERED with or modified!")
     else:
    print("Error: File not found. Please create a simple 'test.txt' file first.")