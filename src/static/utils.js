// Hilfsfunktionen für Frontend

export function validateNumber(value, min = 0) {
    return !isNaN(value) && value >= min;
}

export function notEmpty(value) {
    return value !== undefined && value !== null && value !== ""; // !!value
}

export function buildOutputText(obj, fieldMapping) {
    let output = "";

    for (const key in fieldMapping) {
        if (obj[key] !== undefined) {
            const { label, unit } = fieldMapping[key];
            output += `${label}: ${obj[key]}${unit}, `;
        }
    }

    if (output.endsWith(", ")) {
        output.slice(0, -2);
    }

    return output;
}

export const resultFieldMapping = {
    fahrzeugTyp: { label: "Fahrzeug", unit: "" },
    gesamtkosten: { label: "Gesamtkosten", unit: " €" },
    kostenProPerson: { label: "Kosten/Person", unit: " €" },
    reisezeit: { label: "Reisezeit", unit: " h" },
    kalorienverbrauch: { label: "Kalorienverbrauch", unit: " kcal" },
    anzahlDoener: { label: "Anzahl Döner", unit: "" },
    
};

export const historyFieldMapping = {
    fahrzeugTyp: { label: "Fahrzeug", unit: "" },
    strecke: { label: "Strecke", unit: " km" },
    verbrauch: { label: "Verbrauch", unit: " l/100km" },
    gesamtkosten: { label: "Gesamtkosten", unit: " €" },
    kostenProPerson: { label: "Kosten/Person", unit: " €" },
    koepergewicht: { label: "Körpergewicht", unit: " kg" },
    skillLevel: { label: "Skill-Level", unit: "" },
    ticketPreis: { label: "Tickepreis", unit: " €" },
};