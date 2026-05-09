class MainPage:
    def __init__(self):
        print("[BASE_PAGE] Pomyślnie zainicjalizowano mapę: 459 elementów.")
        print("[MAIN_PAGE] Ekran główny zainicjalizowany.")
        
    def find_id(self, key):
        if key == "list_item": return "list_item"
        return None

class GestureAutomator(MainPage):
    """
    MODUŁ GESTÓW (Layer 4): Rozszerzenie Page Objectu o fizykę dotyku.
    """
    def scroll_down_logic(self, start_y=0.8, end_y=0.2, duration_ms=1000):
        """Symulacja gestu SCROLL DOWN (procentowo)."""
        print(f"[GESTURE] Start Swipe: Y={start_y} -> End Y={end_y} (t={duration_ms}ms)")
        
        if duration_ms < 200:
            return "BŁĄD: Gest zbyt szybki - grozi brakiem reakcji UI (Flick)."
            
        return f"SUKCES: Przewinięto listę o {int((start_y - end_y) * 100)}% wysokości ekranu."

    def long_press_element(self, element_key):
        """Symulacja Long Press na Resource ID."""
        selector = self.find_id(element_key)
        if selector:
            return f"SUKCES: Wykonano LONG PRESS (2s) na elemencie: {selector}"
        return f"BŁĄD: Nie odnaleziono elementu {element_key} w mapie selektorów."

if __name__ == "__main__":
    app = GestureAutomator()
    print(">>> ZADANIE 7.1: TESTY FIZYKI DOTYKU <<<")
    print(app.scroll_down_logic(0.8, 0.2, 800))
    print(app.long_press_element("list_item"))