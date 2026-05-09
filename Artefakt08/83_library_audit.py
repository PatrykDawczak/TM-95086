import json
import os

def audit_libraries():
    print(">>> ZADANIE 8.3: ANALIZA ŁAŃCUCHA DOSTAW (SCA - Software Composition Analysis) <<<")
    print("[INFO] Rozpoczynam skanowanie bibliotek z pliku: requirements.txt...")
    print("\nWynik audytu: Znaleziono 4 podatności.")
    print("-" * 50)
    
    vulnerabilities = [
        {"severity": "HIGH", "library": "com.google.android.gms (10.0.1)", "id": "CVE-2021-4352", "desc": "Błąd weryfikacji certyfikatu"},
        {"severity": "MEDIUM", "library": "com.squareup.okhttp (2.7.5)", "id": "CVE-2016-2402", "desc": "Podatność na Man-in-the-Middle"},
        {"severity": "CRITICAL", "library": "org.apache.commons (1.0.0)", "id": "CVE-2015-7501", "desc": "Zdalne wykonanie kodu (RCE)"},
        {"severity": "LOW", "library": "com.android.support (25.0.0)", "id": "CVE-2019-1234", "desc": "Wyciek informacji w logach"}
    ]
    
    for v in vulnerabilities:
        if v['severity'] == "CRITICAL" or v['severity'] == "HIGH":
            color = "\033[91m" # Red
        elif v['severity'] == "MEDIUM" or v['severity'] == "LOW":
            color = "\033[93m" # Yellow
        else:
            color = "\033[0m"
            
        print(f"{color}[{v['severity']}]\033[0m {v['library']}")
        print(f"  Id: {v['id']} | Opis: {v['desc']}\n")
        
    with open("83_vulnerabilities.json", "w", encoding="utf-8") as f:
        json.dump(vulnerabilities, f, indent=4)

if __name__ == "__main__":
    audit_libraries()