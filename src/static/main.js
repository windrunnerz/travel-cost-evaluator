import { evaluateKosten, fetchHistory } from "./api.js";
import { getInputNumber, getInputInt, setResultText, renderHistory } from "./dom.js";


const form = document.getElementById("kostenForm");
const historyButton = document.getElementById("historyButton");


form.addEventListener("submit", async function(e) {
    e.preventDefault();

    const strecke = getInputNumber("strecke");
    const verbrauch = getInputNumber("verbrauch");
    const kosten = getInputNumber("kosten");
    const mitfahrer = getInputInt("mitfahrer");

    const data = {
        strecke_km: strecke,
        verbrauch_l_pro_100km: verbrauch,
        kosten_pro_liter: kosten,
        mitfahrer_anzahl: mitfahrer
    };

    const result = await evaluateKosten(data);

    setResultText(`Gesamtkosten: ${result.gesamtkosten} €, Kosten pro Person ${result.kosten_pro_person} €`);

});


historyButton.addEventListener("click", async function() {
    try {
        const history = await fetchHistory();
        renderHistory(history);
    } catch (error) {
        console.error();        
    }
});