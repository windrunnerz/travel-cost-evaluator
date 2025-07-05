import { evaluateKosten, fetchHistory } from "./api.js";
import { getInputNumber, getInputInt, setResultText, renderHistory } from "./dom.js";
import { showError, clearError, validateNumber } from "./utils.js";


const form = document.getElementById("kostenForm");
const historyButton = document.getElementById("historyButton");


form.addEventListener("submit", async function(e) {
    e.preventDefault();

    const strecke = getInputNumber("strecke");
    const verbrauch = getInputNumber("verbrauch");
    const spritkosten = getInputNumber("spritkosten");
    const mitfahrer = getInputInt("mitfahrer");

    clearError();

    const validations = [
        {value: strecke, min: 1, message: "Bitte eine gültige Strecke (größer 0) eingeben.", errorID: "streckeError"},
        {value: verbrauch, min: 0, message: "Bitte einen gültigen Verbrauch eingeben.", errorID: "verbrauchError"},
        {value: spritkosten, min: 0, message: "Bitte gültige Spritkosten eingeben.", errorID: "spritkostenError"},
        {value: mitfahrer, min: 1, message: "Bitte mindestens einen Mitfahrer eingeben.", errorID: "mitfahrerError"}
    ];

    for (const v of validations) {
        if (!validateNumber(v.value, v.min)) {
            showError(v.errorID, v.message);
            return;
        }
    }

    const data = {
        strecke_km: strecke,
        verbrauch_l_pro_100km: verbrauch,
        kosten_pro_liter: spritkosten,
        mitfahrer_anzahl: mitfahrer
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