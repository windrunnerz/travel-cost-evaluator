import { evaluateKosten, fetchHistory } from "./api.js";
import { getInputNumber, getInputInt, setResultText, renderHistory, showFieldsForType } from "./dom.js";
import { showError, clearError, validateNumber, notEmpty } from "./utils.js";


const kostenForm = document.getElementById("kostenForm");
const historyButton = document.getElementById("historyButton");
const fahrzeugTypSelect = document.getElementById("fahrzeugTyp");


kostenForm.addEventListener("submit", async function(e) {
    e.preventDefault();

    const selected = fahrzeugTypSelect.value;

    const mitfahrer = getInputInt("mitfahrer");
    const strecke = getInputNumber("strecke");
    const reisezeit = getInputNumber("reisezeit");

    const verbrauch = getInputNumber("verbrauch");
    const spritkosten = getInputNumber("spritkosten");

    const koerperGewicht = getInputNumber("koerperGewicht");
    const skillLevel = parseInt(document.getElementById("skillLevel").value);

    const ticketPreis = getInputNumber("ticketPreis"); 

    clearError();

    const numericValidations = [
        {value: mitfahrer, min: 1, message: "Bitte mindestens einen Mitfahrer eingeben.", errorID: "mitfahrerError"},
        {value: strecke, min: 1, message: "Bitte eine gültige Strecke (größer 0) eingeben.", errorID: "streckeError"},
        {value: reisezeit, min: 1, message: "Bitte eine gültige Reiszeit (größer 0) eingeben.", errorID: "reisezeitError"},
    ];

    if (selected === "auto") {
        numericValidations.push(
            {value: verbrauch, min: 0, message: "Bitte einen gültigen Verbrauch eingeben.", errorID: "verbrauchError"},
            {value: spritkosten, min: 0, message: "Bitte gültige Spritkosten eingeben.", errorID: "spritkostenError"}
        );
    } else if (selected === "fahrrad") {
        numericValidations.push(
            {value: koerperGewicht, min: 20, message: "Bitte Körpergewicht ab 20kg eingeben.", errorID: "koerperGewichtError"},
            {value: skillLevel, min: 1, message: "Bitte Skill Level auswählen.", errorID: "skillLevelError"}
        );
    }else if (selected === "bus" || selected === "zug") {
        numericValidations.push(
            {value: ticketPreis, min: 1, message: "Bitte Ticketpreis eingeben.", errorID: "ticketPreisError"}
        );
    }


    if (!notEmpty(selected)) {
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
        fahrzeug_typ: selected,
        mitfahrer_anzahl: mitfahrer,
        strecke_km: strecke,
        reisezeit: reisezeit
    };
        
    if (selected === "auto") {
        data.verbrauch_l_pro_100km = verbrauch;
        data.spritkosten_pro_liter = spritkosten;
    } else if (selected ==="fahrrad") {
        data.koerpergewicht = koerperGewicht;
        data.skill_level = skillLevel;
    } else if (selected === "bus" || selected === "zug") {
        data.ticket_preis = ticketPreis;
    }

    try {
        const result = await evaluateKosten(data);
        setResultText(`Gesamtkosten: ${result.gesamtkosten} €, Kosten pro Person ${result.kosten_pro_person} €`);
        
        document.getElementById("historyButton").classList.remove("hidden");
    } catch (error) {
        showError("globalError", error.message);
    }
});

fahrzeugTypSelect.addEventListener("change", async function () {
    const selected = fahrzeugTypSelect.value;
    showFieldsForType(selected);
});


historyButton.addEventListener("click", async function() {
    try {
        const history = await fetchHistory();
        renderHistory(history);
    } catch (error) {
        console.error();        
    }
});