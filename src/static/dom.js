// Modul für DOM-Interaktionen: liest Formwerte aus und setzt Inhalte in die Oberfläche.

export function getInputNumber(id) {
    return parseFloat(document.getElementById(id).value);
}

export function getInputInt(id) {
    return parseInt(document.getElementById(id).value);
}

export function setResultText(text) {
    document.getElementById("ergebnis").innerText = text;
}

export function renderHistory(historyArray) {
    let html = "<h3>Historie</h3><ul>";
    historyArray.forEach(entry => {
        html += 
            `<li>
            Strecke: ${entry.strecke} km, 
            Verbrauch: ${entry.verbrauch} l/100km, 
            Geamtkosten: ${entry.gesamtkosten} €, 
            Kosten/Person: ${entry.kosten_pro_person} €
            </li>`;
    });
    html += "</ul>";
    
    document.getElementById("historyOutput").innerHTML = html;
}

export function showFieldsForType(selected) {
    document.getElementById("defaultFields").classList.remove("hidden");
    document.querySelector('button[type="submit"]').classList.remove("hidden");

    document.getElementById("autoFields").classList.add("hidden");
    document.getElementById("fahrradFields").classList.add("hidden");
    document.getElementById("ticketFields").classList.add("hidden");

    if (selected === "auto") {
        document.getElementById("autoFields").classList.remove("hidden");
    }
    else if (selected === "fahrrad") {
        document.getElementById("fahrradFields").classList.remove("hidden");
    }
    else if (selected === "bus" || selected === "zug") {
        document.getElementById("ticketFields").classList.remove("hidden");
    }
}

