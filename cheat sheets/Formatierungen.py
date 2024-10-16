# Formatierungsspezifikatoren in Python: Verschiedene Beispiele

zahl = 1234567.89123
text = "Hallo"
anteil = 0.25
hex_zahl = 255

# 1. Tausendertrennzeichen
print(f"{zahl:,}")  # Ausgabe: 1,234,567.89123 (Komma als Tausendertrennzeichen)

# 2. Anzahl der Nachkommastellen
print(f"{zahl:.2f}")  # Ausgabe: 1234567.89 (2 Dezimalstellen)
print(f"{zahl:.3g}")  # Ausgabe: 1.23e+06 (3 signifikante Stellen in wissenschaftlicher Notation)

# 3. Vorzeichen angeben
positive_zahl = 42
negative_zahl = -42
print(f"{positive_zahl:+}")  # Ausgabe: +42 (Vorzeichen für positive Zahl)
print(f"{negative_zahl:-}")  # Ausgabe: -42 (Vorzeichen nur für negative Zahl)
print(f"{positive_zahl: }")  # Ausgabe:  42 (Leerzeichen für positive Zahl)

# 4. Ausrichtung und Breite
print(f"{text:<10}")  # Ausgabe: 'Hallo     ' (linksbündig, Breite 10)
print(f"{text:>10}")  # Ausgabe: '     Hallo' (rechtsbündig, Breite 10)
print(f"{text:^10}")  # Ausgabe: '  Hallo   ' (zentriert, Breite 10)

# 5. Auffüllen mit Zeichen
print(f"{positive_zahl:05}")  # Ausgabe: 00042 (Auffüllen mit Nullen, Breite 5)

# 6. Hexadezimal-, Oktal- und Binärdarstellung
print(f"{hex_zahl:x}")  # Ausgabe: ff (hexadezimal, kleine Buchstaben)
print(f"{hex_zahl:X}")  # Ausgabe: FF (hexadezimal, große Buchstaben)
print(f"{hex_zahl:o}")  # Ausgabe: 377 (oktal)
print(f"{hex_zahl:b}")  # Ausgabe: 11111111 (binär)

# 7. Wissenschaftliche Notation
print(f"{zahl:e}")  # Ausgabe: 1.234568e+06 (wissenschaftliche Notation, kleine Buchstaben)
print(f"{zahl:E}")  # Ausgabe: 1.234568E+06 (wissenschaftliche Notation, große Buchstaben)

# 8. Prozentsatz
print(f"{anteil:.2%}")  # Ausgabe: 25.00% (Prozentdarstellung mit 2 Dezimalstellen)

# Weitere kombinierte Beispiele
print(f"{zahl:,.2f}")  # Ausgabe: 1,234,567.89 (Komma als Tausendertrennzeichen, 2 Dezimalstellen)
print(f"{zahl:10.2f}")  # Ausgabe: ' 1234567.89' (rechte Ausrichtung, insgesamt 10 Stellen)
print(f"{zahl:<10.2f}")  # Ausgabe: '1234567.89 ' (linke Ausrichtung, insgesamt 10 Stellen)
print(f"{zahl:010.2f}")  # Ausgabe: '01234567.89' (Auffüllen mit Nullen, insgesamt 10 Stellen)