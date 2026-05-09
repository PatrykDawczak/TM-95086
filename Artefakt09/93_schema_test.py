import requests
from jsonschema import validate

def test_schema():
    print(">>> ZADANIE 9.3: WALIDACJA STRUKTURY JSON (KONTRAKT) <<<")
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url).json()
    
    # Określamy strukture: userId i id MUSZĄ być liczbami, a title i body tekstami
    expected_schema = {
        "type": "object",
        "properties": {
            "userId": {"type": "number"},
            "id": {"type": "number"},
            "title": {"type": "string"},
            "body": {"type": "string"}
        },
        "required": ["userId", "id", "title"]
    }
    
    try:
        validate(instance=response, schema=expected_schema)
        print("[SUCCESS] Kontrakt zachowany. Struktura JSON jest poprawna.")
        print(f"[DEBUG] Zweryfikowano pola dla obiektu ID: {response.get('id')}")
    except Exception as e:
        print(f"[FAIL] Kontrakt złamany! Błąd struktury: {e}")

if __name__ == "__main__":
    test_schema()