Google Calendar Viewer
Aplikacja w Flask, która pozwala na wyświetlanie nadchodzących wydarzeń z kalendarza Google (lub innego kalendarza ICS) za pomocą pliku .ics.

💡 Opis
Ta aplikacja pozwala użytkownikowi na podanie linku do swojego kalendarza Google (lub innego kalendarza ICS) i wyświetlanie nadchodzących wydarzeń. Wydarzenia są pobierane z pliku .ics i wyświetlane w prostym interfejsie opartym na Flask i Bootstrap.

🚀 Uruchomienie
1. Klonowanie repozytorium
bash
git clone https://github.com/TwójUsername/GoogleCalendarAlert.git
cd GoogleCalendarAlert
2. Instalacja wymaganych pakietów
Upewnij się, że masz zainstalowanego Pythona (minimum 3.7) i pip.

Zainstaluj wymagane biblioteki:
bash
pip install -r requirements.txt

Jeśli nie masz jeszcze pliku requirements.txt, to uruchom poniższe polecenie, aby go wygenerować:
bash
pip freeze > requirements.txt

3. Uruchomienie aplikacji
Uruchom aplikację Flask:

bash
python app.py
Aplikacja będzie dostępna pod adresem http://localhost:5002.

💻 Funkcjonalności
Podanie własnego linku ICS: Użytkownicy mogą podać link do swojego kalendarza .ics, aby wyświetlić nadchodzące wydarzenia.
Wyświetlanie wydarzeń: Aplikacja wyświetla wydarzenia z nadchodzącego tygodnia w prostym, estetycznym interfejsie.
Bootstrap: Aplikacja wykorzystuje bibliotekę Bootstrap, aby szybko stworzyć responsywny i atrakcyjny wygląd.

🔧 Technologie
Flask - Web framework do Pythona
Requests - Biblioteka do wykonywania żądań HTTP
ICS - Biblioteka do parsowania plików ICS
Bootstrap - Framework CSS do responsywnych stron
