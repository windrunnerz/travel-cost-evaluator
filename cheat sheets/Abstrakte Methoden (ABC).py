# Vorteil von abc gegenüber Kommentar

# 1. Erzwingung der Implementierung

#   - Durch Verwendung von abc und Definition von abstrakten Methoden, erzwingt
#   Python, dass alle Unterklassen diese Methoden implementieren. Das bedeutet, dass jede Unterklasse die definierten
#   abstrakten Methoden bereitstellen muss, bevor sie instanziiert werden kann.

from abc import ABC, abstractmethod

class Transportmittel(ABC):
    @abstractmethod
    def berechne_kosten(self):
        pass

# Bei Verwendung von @abstractmethod und ABC wird Python eine Fehlermeldung ausgeben, wenn eine Unterklasse
# berechne_kosten() nicht implementiert. Dies hilft, sicherzustellen, dass der Code korrekt ist und alle Unterklassen
# die benötigten Methoden haben.

# 2. Frühe Fehlererkennung
#   - Mit abstrakten Klassen und Methoden kannst du potenzielle Fehler frühzeitig erkennen. Wenn eine Unterklasse die
#   abstrakte Methode nicht implementiert, wird dies direkt beim Erstellen der Klasse bemerkt und führt zu einem Fehler.
#   Dadurch kann vermieden werden, dass zur Laufzeit unerwartete Fehler auftreten, weil eine erwartete Methode fehlt.

# Ohne ABC:
class Transportmittel:
    # Kommentar: Diese Klasse soll als abstrakte Klasse verwendet werden.
    def berechne_kosten(self):
        pass  # Wird als Platzhalter verwendet

# Wenn du nur einen Kommentar hinzufügst, dass eine Methode implementiert werden soll, könnte es passieren, dass du oder
# ein anderer Entwickler dies vergisst, und zur Laufzeit wird nur die Platzhalter-Methode (pass) aufgerufen, was
# möglicherweise zu ungewolltem Verhalten führt.

# 3. Klarere Intentionen im Code
#   - Die Verwendung von ABC macht deine Absicht klarer. Es signalisiert anderen Entwicklern explizit, dass
#   Transportmittel eine abstrakte Klasse ist, die nicht instanziiert werden sollte, und dass die Unterklassen bestimmte
#   Methoden haben müssen.
#   - Kommentare können diese Intention ebenfalls vermitteln, aber sie sind nicht bindend. Sie dienen lediglich als
#   Hinweise und bieten keine Garantie, dass sie umgesetzt werden.

# 4. Bessere Unterstützung durch Werkzeuge
#   - Viele Entwicklungswerkzeuge und IDEs können mit abstrakten Klassen besser umgehen, indem sie Hinweise und
#   Warnungen geben, wenn eine Unterklasse nicht alle abstrakten Methoden implementiert.
#   - Mit Kommentaren erhalten Entwickler weniger Unterstützung durch Tools, da diese Kommentare nicht interpretieren
#   können, ob eine Methode wirklich als Pflicht implementiert werden muss.

# 5. Explizite Abstraktion
#   - Durch die Verwendung von ABC und @abstractmethod zeigst du klar, dass deine Klasse eine Abstraktion ist. Die
#   Klasse Transportmittel selbst kann nicht direkt instanziiert werden, was sinnvoll ist, da sie eine allgemeine
#   Struktur für alle Unterklassen bietet, aber keine konkrete Implementierung.
#   - Wenn du nur mit einem Kommentar arbeitest, bleibt diese Klasse instanziierbar, obwohl sie möglicherweise keine
#   sinnvolle Implementierung für sich allein hat.

# Zusammenfassung
#   - Die Verwendung von ABC und @abstractmethod stellt sicher, dass jede Unterklasse bestimmte Methoden implementiert.
#   Das macht den Code robuster, konsistenter und weniger fehleranfällig.
#   - Kommentare allein haben keine Bindungskraft; sie sind eher Empfehlungen, die leicht übersehen werden können,
#   während abstrakte Klassen und Methoden durch den Python-Interpreter erzwingend sind.
# Durch die Verwendung von abstrakten Klassen und Methoden kannst du sicherstellen, dass dein Code konsistent ist und
# alle Unterklassen die erforderlichen Methoden bieten, was zu einer besseren Wartbarkeit und Qualität führt.

# Wichtige Punkte:
# 1. Erbe von ABC:
#   - Eine Klasse wird zur abstrakten Klasse, indem sie von ABC (Abstract Base Class) erbt. Dies zeigt an, dass die
#   Klasse möglicherweise abstrakte Methoden enthält.
# 2. Verwendung von @abstractmethod:
#   - Der Dekorator @abstractmethod markiert eine Methode als abstrakt, sodass jede Unterklasse gezwungen ist, diese
#   Methode zu implementieren.
# 3. Nicht instanziierbar:
#   - Eine abstrakte Klasse kann nicht direkt instanziiert werden. Das bedeutet, du kannst nicht einfach ein Objekt der
#   abstrakten Klasse Transportmittel erstellen. Stattdessen musst du eine Unterklasse verwenden, die die abstrakten
#   Methoden implementiert.
#
# Warum werden abstrakte Methoden verwendet?
#   - Vorlagen und Schnittstellen: Sie bieten eine Art Vorlage für alle Unterklassen. Dadurch kann sichergestellt
#   werden, dass alle Unterklassen bestimmte Methoden besitzen, die eine konsistente Schnittstelle bieten.
#   - Vermeidung von Implementierungsdetails: In der Oberklasse werden keine Details der Methode spezifiziert. Die
#   Details überlässt man den spezifischen Unterklassen, was zu einer flexibleren und besser strukturierten Codebasis
#   führt.

