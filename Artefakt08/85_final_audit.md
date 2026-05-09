# 📊 RAPORT Z AUDYTU BEZPIECZEŃSTWA: APIDEMOS
**Data:** 09-05-2026
**Audytor:** Patryk Dawczak (95086)
**Projekt:** Testowanie Aplikacji Mobilnych - Blok 8

## 📊 1. OCENA KOŃCOWA (SECURITY SCORE)
**WYNIK:** 0/100
**STATUS:** 🔴 REJECTED

## 🛡️ 2. KLUCZOWE OBSZARY RYZYKA

### A. Konfiguracja Systemowa (Zadanie 8.1)
**Problem:** W pliku AndroidManifest.xml pozostawiono aktywną flagę `debuggable="true"`.
**Wpływ:** Pozwala napastnikowi na podłączenie debuggera i manipulowanie pamięcią aplikacji w czasie rzeczywistym.

### B. Wycieki Danych (Zadanie 8.2)
**Problem:** Zidentyfikowano twardo zakodowane potencjalne hasła (`password`) oraz ścieżki e-mail w strings.xml.
**Wpływ:** Ułatwia to dostęp do kont testowych lub produkcyjnych oraz ujawnia wewnętrzną infrastrukturę atakującemu.

### C. Biblioteki Zewnętrzne (Zadanie 8.3)
**Problem:** Znaleziono krytyczną podatność (CVE-2015-7501) w bibliotece `org.apache.commons (1.0.0)`.
**Wpływ:** Umożliwia Zdalne Wykonanie Kodu (RCE) na urządzeniu ofiary.

## 📄 3. MAPA DROGOWA NAPRAWCZA (REMEDIATION)
1. **[PRIORYTET 1]:** Aktualizacja biblioteki `org.apache.commons` do najnowszej bezpiecznej wersji lub jej usunięcie.
2. **[PRIORYTET 1]:** Bezwzględna zmiana flagi `debuggable` na `false` we wszystkich buildach produkcyjnych.
3. **[PRIORYTET 2]:** Przeniesienie wszystkich twardo zakodowanych poświadczeń do bezpiecznego zarządzania kluczami (np. Android Keystore).

## 🏁 WNIOSKI KOŃCOWE
Aplikacja w obecnym stanie posiada krytyczne luki w łańcuchu dostaw oraz błędną konfigurację budowania. Wypuszczenie jej na rynek grozi natychmiastowym przejęciem danych. Kod wstrzymany (No-Go).