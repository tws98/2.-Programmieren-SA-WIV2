SELECT_MITARBEITER = """
    SELECT 
    m.ID_Mitarbeiter,
    a.Anrede,
    m.Vorname,
    m.Name,
    m.Strasse,
    m.Hausnr,
    o.PLZ,
    o.Ort,
    m.Telefon
FROM mitarbeiter m
JOIN anrede a ON m.Anrede = a.ID_Anrede
JOIN ort o ON m.ID_Ort = o.ID_Ort
ORDER BY m.ID_Mitarbeiter;
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