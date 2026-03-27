# Selektiert alle Mitarbeiter mit allen Daten
SELECT_MITARBEITER = """
    SELECT 
        ID_Mitarbeiter,
        Anrede,
        Vorname,
        Name,
        Strasse,
        Hausnr,
        ID_Ort,
        Telefon
    FROM mitarbeiter
"""

# Selektiert alle Orte zu einer bestimmten PLZ
SELECT_ORT_BY_PLZ = """
    SELECT 
        ID_Ort,
        PLZ,
        Ort
    FROM ort
    WHERE PLZ = ?
"""

# Selektiert alle Anreden
SELECT_ANREDE = """
    SELECT 
        ID_Anrede,
        Anrede
    FROM anrede
"""

# Fügt einen neuen Mitarbeiter ein (ID_Mitarbeiter wird automatisch vergeben)
INSERT_MITARBEITER = """
    INSERT INTO mitarbeiter (
        Anrede,
        Vorname,
        Name,
        Strasse,
        Hausnr,
        ID_Ort,
        Telefon
    ) VALUES (?, ?, ?, ?, ?, ?, ?)
"""