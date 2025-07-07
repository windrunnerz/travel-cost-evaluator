import { evaluateKosten, fetchHistory } from "./api.js";
import { getInputNumber, getInputInt, setResultText, renderHistory } from "./dom.js";
import { showError, clearError, validateNumber, notEmpty } from "./utils.js";


const kostenForm = document.getElementById("kostenForm");
const historyButton = document.getElementById("historyButton");


kostenForm.addEventListener("submit", async function(e) {
    e.preventDefault();

    const strecke = getInputNumber("strecke");
    const reisezeit = getInputNumber("reisezeit");
    const verbrauch = getInputNumber("verbrauch");
    const spritkosten = getInputNumber("spritkosten");
    const mitfahrer = getInputInt("mitfahrer");
    const fahrzeugTyp = document.getElementById("fahrzeugTyp").value;

    clearError();

    const numericValidations = [
        {value: strecke, min: 1, message: "Bitte eine gültige Strecke (größer 0) eingeben.", errorID: "streckeError"},
        {value: reisezeit, min: 1, message: "Bitte eine gültige Reiszeit (größer 0) eingeben.", errorID: "reisezeitError"},
        {value: verbrauch, min: 0, message: "Bitte einen gültigen Verbrauch eingeben.", errorID: "verbrauchError"},
        {value: spritkosten, min: 0, message: "Bitte gültige Spritkosten eingeben.", errorID: "spritkostenError"},
        {value: mitfahrer, min: 1, message: "Bitte mindestens einen Mitfahrer eingeben.", errorID: "mitfahrerError"}
    ];

    if (!notEmpty(fahrzeugTyp)) {
        showError("fahrzeugTypError", "Bitte Fahrzeug auswählen.");
        return;
    }

    for (const validation of numericValidations) {

        if (!validateNumber(validation.value, validation.min)) {
            showError(validation.errorID, validation.message);
            return;
        }
    }

    const data = {
        strecke_km: strecke,
        reisezeit: reisezeit,
        verbrauch_l_pro_100km: verbrauch,
        spritkosten_pro_liter: spritkosten,
        mitfahrer_anzahl: mitfahrer,
        fahrzeug_typ: fahrzeugTyp
    };

    try {
        const result = await evaluateKosten(data);
        setResultText(`Gesamtkosten: ${result.gesamtkosten} €, Kosten pro Person ${result.kosten_pro_person} €`);
    } catch (error) {
        showError("globalError", error.message);
    }
});


historyButton.addEventListener("click", async function() {
    try {
        const history = await fetchHistory();
        renderHistory(history);
    } catch (error) {
        console.error();        
    }
});