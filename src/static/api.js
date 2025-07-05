// Modul für Server-Kommunikation: kapselt alle Fetch-Requests und API-Aufrufe

async function evaluateKosten(data) {
    const response = await fetch("/api/evaluate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    });

    if (!response.ok) {
        throw new Error(`Server-Fehler: ${response.status}`);
    }

    return await response.json(); 
};


async function fetchHistory() {
    const response = await fetch("/api/history");

    if (!response.ok) {
        throw new Error(`Server-Fehler: ${response.status}`);
    }

    return await response.json();
}

export { evaluateKosten, fetchHistory };