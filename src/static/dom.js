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

export { getInputNumber, getInputInt, setResultText };