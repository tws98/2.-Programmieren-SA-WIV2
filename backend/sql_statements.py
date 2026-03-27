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

SELECT_ORT_BY_PLZ = """
    SELECT 
        ID_Ort,
        PLZ,
        Ort
    FROM ort
    WHERE PLZ = ?
"""

SELECT_ANREDE = """
    SELECT 
        ID_Anrede,
        Anrede
    FROM anrede
"""

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