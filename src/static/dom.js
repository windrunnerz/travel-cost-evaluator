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
    console.log("showFieldsForType called with:", selected);

    toggleElementVisibility("defaultFields", true);
    toggleElementVisibility("berechnenButton", true);

    toggleElementVisibility("autoFields", false);
    toggleElementVisibility("fahrradFields", false);
    toggleElementVisibility("ticketFields", false);

    if (selected === "auto") {
        toggleElementVisibility("autoFields", true);
    }
    else if (selected === "fahrrad") {
        toggleElementVisibility("fahrradFields", true);
    }
    else if (selected === "bus" || selected === "zug") {
        toggleElementVisibility("ticketFields", true);
    }
}

export function showError(errorID, message) {
    document.getElementById(errorID).innerText = message;
}

export function clearError() {
    const errorSpans = document.querySelectorAll(".error-text");

    errorSpans.forEach(span => {
        span.textContent = "";
    });
}

export function clearInputs(containerID) {
    const container = document.getElementById(containerID);
    const inputFields = container.querySelectorAll("input");

    inputFields.forEach(field => {
        field.value = field.defaultValue;
    });
}