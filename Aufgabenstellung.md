Superdiesel

Die Superdiesel GmbH bekommt eine neue Software zur Mitarbeiter Verwaltung. Diese besteht aus einem Flask backend und einem Web Frontend (HTML/CSS/JS). Teile der Software wurden schon fertiggestellt.
Die fertige Software soll die aktuellen Mitarbeiter als Liste auf der Startseite anzeigen lassen. Dabei sollen nur Anrede, Vorname und Nachname angezeigt werden. Die Mitarbeiter sollen nach Nachname aufsteigend sortiert dargestellt werden.

Das Formular zum Anlegen eines neuen Mitarbeiters soll alle Menüs dynamisch aus der Datenbank laden. Die Eingabe einer PLZ und das Drücken des entsprechenden Buttons ist nötig um die dazugehörigen Orte aus der Datenbank zu laden. Die Filterung soll im Backend stattfinden. Es soll jedoch nur eine Anfrage an das Backend geschickt werden, falls die PLZ genau 5 Stellen hat. Ansonsten soll eine entsprechende Meldung ausgegeben werden. (z. B. mittels a l e r t).
Beispiel für eine korrekte PLZ:

PLZ: 91058 -> Bruck, Eltersdorf, Erlangen, Königsmühle, Tennenlohe Kreis Erlangen

Treten Fehler bei der Kommunikation mit dem Backend auf sollen die Fehler mit einer eindeutigen Fehlermeldung im dafür vorgesehenen Feld entsprechend angezeigt werden.

Im Backend müssen alle nötigen Endpunkte für die korrekte Funktionsweise implementiert werden. Dabei müssen alle Eingaben sinnvoll validiert werden und entsprechende Fehlermeldungen zurückgegeben werden. Die Telefonnummer soll mit Hilfe von RegEx auf Plausibilität  überprüft werden. Dabei soll folgendes gelten:

Telefonnummern sollen immer mit Vorwahl, auch mit der Ländervorwahl für Deutschland angegeben werden.
Konnte der Mitarbeiter erfolgreich angelegt werden, soll die entsprechende ID des neuen Mitarbeiters in der Meldung enthalten sein.

Senden Sie auch eine entsprechende Fehlermeldung falls die Datenbank nicht verfügbar ist. (Sie können dies testen, indem Sie die Datenbank umbenennen.)

Konnte das Formular erfolgreich übermittelt und der neue Mitarbeiter angelegt werden soll eine Erfolgsmeldung ausgegeben und alle Felder des Formulars automatisch geleert werden.
Hinweis: Alle benötigten SQL-Statements und die Datenbankstruktur sind vorgegeben. Es dürfen keine Änderungen an der Datenbank vorgenommen werden.

Hilfestellung: Pfadparameter in Flask können mit <parameter> definiert werden. In diesem Fall könnte der Endpunkt für die PLZ-Abfrage wie folgt aussehen: /api/ort/<plz>
