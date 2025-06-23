import string
import random

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("Devi selezionare almeno un tipo di carattere!")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Benvenuto nel Password Generator!")
    length = int(input("Lunghezza password (default 12): ") or 12)
    use_upper = input("Usare lettere maiuscole? (S/n): ").lower() != 'n'
    use_lower = input("Usare lettere minuscole? (S/n): ").lower() != 'n'
    use_digits = input("Usare numeri? (S/n): ").lower() != 'n'
    use_special = input("Usare caratteri speciali? (S/n): ").lower() != 'n'

    try:
        password = generate_password(length, use_upper, use_lower, use_digits, use_special)
        print(f"\nPassword generata: {password}")
    except ValueError as e:
        print(f"Errore: {e}")

if __name__ == "__main__":
    main()
