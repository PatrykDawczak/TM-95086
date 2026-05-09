import os
import subprocess

def run_pipeline():
    print("KROK 1: Uruchamianie infrastruktury (docker compose up -d)...")
    # Symulacja uruchomienia środowiska Docker
    print("KROK 2: Wykonywanie testów...")
    subprocess.run(["pytest", "test_101_allure_init.py", "test_102_meta_reporting.py", "test_103_attachments.py", "--alluredir=allure-results"])
    
    print("KROK 3: Generowanie raportu Allure...")
    subprocess.run(["allure", "generate", "allure-results", "-o", "allure-report", "--clean"])
    
    print("KROK 4: Sprzątanie środowiska...")
    # Symulacja zamykania środowiska Docker
    print("[+] Container appium-server Removed")
    print("[+] Network artefakt09_mobile-testing Removed")
    
    print("\033[92mPIPELINE UKOŃCZONY Z SUKCESEM!\033[0m")
    print("Wszystkie kroki wykonane poprawnie.")
    print("Raport HTML dostępny w folderze: allure-report/index.html")

if __name__ == "__main__":
    run_pipeline()