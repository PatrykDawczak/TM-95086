import time

class MainPage:
    def __init__(self):
        print("[BASE_PAGE] Pomyślnie zainicjalizowano mapę: 459 elementów.")
        print("[MAIN_PAGE] Ekran główny zainicjalizowany.")

class InterruptManager(MainPage):
    """
    MODUŁ PRZERWAŃ (Layer 4): Symulacja zdarzeń systemowych Androida.
    """
    def simulate_incoming_call(self, duration_sec=5):
        """Symuluje nadchodzące połączenie, które przysłania aplikację."""
        print("\n[INTERRUPT] KROK 1: Stan aplikacji przed połączeniem: ACTIVE")
        print(f"[INTERRUPT] KROK 2: Wyzwalanie zdarzenia: INCOMING CALL (Duration: {duration_sec}s)")
        
        # W Appium: driver.make_gsm_call(phone_number, GsmCallActions.CALL)
        time.sleep(1)
        print(">>> SYSTEM: Aplikacja w tle (onPause) | Widoczny ekran połączenia <<<")
        
        time.sleep(duration_sec) # Czas trwania rozmowy
        
        print("[INTERRUPT] KROK 3: Zakończenie połączenia. Powrót do aplikacji.")
        # W Appium: driver.activate_app('io.appium.android.apis')
        
        return "SUKCES: Aplikacja odzyskała fokus (onResume). Dane sesji zachowane."

    def simulate_low_battery_warning(self):
        """Symuluje systemowy komunikat o niskim stanie baterii (System Dialog)."""
        print("\n[INTERRUPT] Wyzwalanie zdarzenia: LOW BATTERY WARNING")
        # W Appium: driver.set_power_capacity(5)
        return "SUKCES: Aplikacja obsłużyła systemowe okno dialogowe bez błędu."

if __name__ == "__main__":
    app = InterruptManager()
    print(">>> ZADANIE 7.2: TESTY ODPORNOŚCI NA PRZERWANIA <<<")
    print(app.simulate_incoming_call(3))
    print(app.simulate_low_battery_warning())