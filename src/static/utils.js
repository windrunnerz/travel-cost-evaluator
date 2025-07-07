// Hilfsfunktionen für Frontend

function validateNumber(value, min = 0) {
    return !isNaN(value) && value >= min;
}

function notEmpty(value) {
    return value !== undefined && value !== null && value !== ""; // !!value
}

function showError(errorID, message) {
    document.getElementById(errorID).innerText = message;
}

function clearError() {
    showError("streckeError", "");
    showError("verbrauchError", "");
    showError("spritkostenError", "");
    showError("mitfahrerError", "");
    showError("fahrzeugTypError", "");
    showError("globalError", "");
}


export { validateNumber, showError, clearError, notEmpty };