// Modul für DOM-Interaktionen: liest Formwerte aus und setzt Inhalte in die Oberfläche.

import { buildOutputText, historyFieldMapping } from "./utils.js";

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
        const liContent = buildOutputText(entry, historyFieldMapping);
        html += `<li>${liContent}</li>`;
    });

    html += "</ul>";
    document.getElementById("historyOutput").innerHTML = html;
}

export function toggleElementVisibility(id, show = true) {
    if (show === true) {
        document.getElementById(id).classList.remove("hidden");
    } else {
        document.getElementById(id).classList.add("hidden");
    }
}

export function showFieldsForType(selected) {
    toggleElementVisibility("defaultFields");
    toggleElementVisibility("berechnenButton");

    toggleElementVisibility("autoFields", false);
    toggleElementVisibility("fahrradFields", false);
    toggleElementVisibility("ticketFields", false);

    if (selected === "auto") {
        toggleElementVisibility("autoFields");
    }
    else if (selected === "fahrrad") {
        toggleElementVisibility("fahrradFields");
    }
    else if (selected === "bus" || selected === "zug") {
        toggleElementVisibility("ticketFields");
    }
}
