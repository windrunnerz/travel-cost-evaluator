const form = document.getElementById("kostenForm");

form.addEventListener("submit", async function(e) {
    e.preventDefault();

    const strecke = parseFloat(document.getElementById("strecke").value);
    const verbrauch = parseFloat(document.getElementById("verbrauch").value);
    const kosten = parseFloat(document.getElementById("kosten").value);
    const mitfahrer = parseInt(document.getElementById("mitfahrer").value);

    const data = {
        strecke_km: strecke,
        verbrauch_l_pro_100km: verbrauch,
        kosten_pro_liter: kosten,
        mitfahrer_anzahl: mitfahrer
    };

    const response = await fetch("/api/evaluate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    const result = await response.json();

    document.getElementById("ergebnis").innerText =
        `Gesamtkosten: ${result.gesamtkosten} €, Kosten pro Person ${result.kosten_pro_person} €`;
});