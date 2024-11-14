# Rekrutacja

Jak to działa? - Aplikacja wczytuje artykuł z pliku tekstowego, przekształca go na sformatowany kod HTML za pomocą sprecyzowanego promptu do OpenAI i zapisuje w folderze z kodem głównym pod nazwą artykul.html

Jak uruchomić? - Żeby główny kod main.py działał poprawnie - należy wkleić swój klucz do API OpenAI w miejscu: (openai.api_key = "TUTAJ").
Do uruchomienia aplikacji potrzebujesz jeszcze pliku tekstowego do odczytu, zapisanego w tym samym miejscu co main.py (lub podania innej ścieżki pliku w miejscu: article_path = "///")- w moim przypadku jest to plik Oxido.txt zapisany bezpośrednio w folderze z kodem głównym.
W rezultacie, po krótkiej chwili od startu aplikacji, powinien pojawić się w Twoim folderze plik o nazwie artykul.html z przekonwertowanym plikiem tekstowym ;)
