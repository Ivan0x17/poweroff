# poweroff
l'obbiettivo di questo programma è spegnere windows tutti i giorni a una specifica ora

1. primo avvio il programma ti chiede che ora vuoi spegnerlo
2. salva l'ora in un file json e rimane in background fino all'ora X

ho usato la libreria pyinstaller per compilarlo per windows:

compila lo script python è lo trasforma in bin in base al so installato (linux/windows/macos)
pyinstaller --onefile main.py
