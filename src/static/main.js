import { evaluateKosten } from "./api";
import { getInputNumber, getInputInt, setResultText } from "./dom";


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
    const response = await fetch("/api/history");
    const history = await response.json();

    let html = "<h3>Historie</h3><ul>";
    history.forEach(entry => {
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
})