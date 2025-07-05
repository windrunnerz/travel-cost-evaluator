// Modul für DOM-Interaktionen: liest Formwerte aus und setzt Inhalte in die Oberfläche.

function getInputNumber(id) {
    return parseFloat(document.getElementById(id).value);
}

function getInputInt(id) {
    return parseInt(document.getElementById(id).value);
}

function setResultText(text) {
    document.getElementById("ergebnis").innerText = text;
}

function renderHistory(historyArray) {
    let html = "<h3>Historie</h3><ul>";
    historyArray.forEach(entry => {
        html += 
            `<li>
            Strecke: ${entry.strecke} km, 
            Verbrauch: ${entry.verbrauch} l/100km, 
            Kosten: ${entry.gesamtkosten} €, 
            Kosten/Person: ${entry.kosten_pro_person} €
            </li>`;
    });
    html += "</ul>";
    
    document.getElementById("historyOutput").innerHTML = html;
}


export { getInputNumber, getInputInt, setResultText, renderHistory };