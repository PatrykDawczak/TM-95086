import requests

def test_api_errors():
    print(">>> ZADANIE 9.4: TESTY NEGATYWNE (OBSŁUGA BŁĘDÓW) <<<")
    
    # 1. TEST: Zasób nie istnieje (404)
    url_404 = "https://jsonplaceholder.typicode.com/posts/999999"
    print(f"[INFO] Próba pobrania nieistniejącego zasobu: {url_404}")
    
    response = requests.get(url_404)
    
    if response.status_code == 404:
        print("[SUCCESS] API poprawnie zwróciło kod 404 Not Found.")
    else:
        print(f"[FAIL] Oczekiwano 404, a otrzymano: {response.status_code}")
        
    # 2. TEST: Błędne zapytanie (Celowe wysłanie błędnego typu danych)
    url_post = "https://jsonplaceholder.typicode.com/posts"
    print(f"[INFO] Próba wysłania błędnego body (nie-JSON) do: {url_post}")
    
    bad_data = "To nie jest JSON, to zwykły tekst"
    response_bad = requests.post(url_post, data=bad_data)
    
    print(f"[DEBUG] Status dla błędnych danych: {response_bad.status_code}")

if __name__ == "__main__":
    test_api_errors()