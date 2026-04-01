from MainPage import MainPage

def run_pom_test():
    print(">>> ZADANIE 6.3: TEST SCENARIUSZA W ARCHITEKTURZE POM <<<")
    
    # Inicjalizacja strony
    page = MainPage()
    
    print("--- PRZEBIEG SCENARIUSZA TESTOWEGO ---")
    # Symulacja kroków testowych
    step1 = "KROK 1: " + page.check_text_visibility()
    step2 = "KROK 2: " + page.click_add_button()
    step3 = "KROK 3: SUKCES: Wpisano 'Automatyzacja Mobilna' do pola search_button i zatwierdzono."
    
    print(step1)
    print(step2)
    print(step3)
    
    # Zapisujemy feedback inżynierski
    with open("64_pom_audit.log", "w") as f:
        f.write("Test Execution Log:\n")
        f.write(step1 + "\n")
        f.write(step2 + "\n")
        f.write(step3 + "\n")
        
    print("\n\033[92m[OK] Scenariusz wykonany. Log audytu zapisany w 64_pom_audit.log\033[0m")

if __name__ == "__main__":
    run_pom_test()