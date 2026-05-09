# 📱 Mobile App Testing Framework (Appium & Python)

**Autor:** Patryk Dawczak (Nr indeksu: 95086)
**Projekt:** Zaawansowane testowanie aplikacji mobilnych w architekturze Page Object Model.

## 🚀 O Projekcie
Repozytorium stanowi kompletny framework testowy (End-to-End) zbudowany od zera. Projekt integruje analizę statyczną, testy API, automatyzację UI (Appium) oraz raportowanie (Allure) z wykorzystaniem środowiska wirtualnego Docker.

## 🛠 Wykorzystane technologie
* **Język:** Python 3
* **Frameworki:** Appium, Pytest, Requests
* **Raportowanie:** Allure Framework
* **Infrastruktura:** Docker (konteneryzacja serwera Appium)
* **Bezpieczeństwo:** MobSF (koncepcje analizy statycznej APK)

## 📂 Struktura Projektu (Bloki 1-10)
* **Blok 1 & 2:** Podstawy ADB oraz inżynieria wsteczna (dekompilacja APK za pomocą Apktool).
* **Blok 3:** Wdrożenie serwera Appium przy użyciu `docker-compose`.
* **Blok 4 & 5:** Ekstrakcja selektorów, analiza Indeksu Dominacji Klas (CDI) oraz Mapowanie UI (Dictionary).
* **Blok 6:** Implementacja architektury **Page Object Model (POM)**.
* **Blok 7:** Symulacja gestów (Swipe, Long Press) oraz testy przerwań (Incoming Call, Battery Warning).
* **Blok 8:** Audyt bezpieczeństwa (DevSecOps), poszukiwanie Hardcoded Secrets oraz analiza podatności (CVE).
* **Blok 9:** Testy backendu przez REST API (CRUD, walidacja JSON Schema, obsługa błędów).
* **Blok 10:** Konfiguracja potoku CI/CD, raportowanie Allure oraz budowa profesjonalnego repozytorium.

---
*Projekt zrealizowany w ramach laboratorium Testowania Aplikacji Mobilnych.*