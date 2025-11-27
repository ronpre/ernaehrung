#!/usr/bin/env python3
"""Erzeugt einen wochenplan fuer leber- und blutfreundliche Ernaehrung."""

from __future__ import annotations

import random
import sys
from datetime import date
from pathlib import Path

MEALS = [
    {
        "name": "Ofenlachs mit Zitronen-Quinoa und geduenstetem Brokkoli",
        "prep_time": "25 Minuten",
        "ingredients": [
            "2 Lachsfilets (je ca. 120 g)",
            "120 g Quinoa",
            "1 Bio-Zitrone",
            "250 g Brokkoli",
            "1 EL Olivenoel",
            "Frischer Dill, Salz, Pfeffer",
        ],
        "instructions": (
            "Backofen auf 180 C vorheizen. Lachs mit Zitrone, Dill, Salz und Pfeffer in"
            " eine ofenfeste Form legen und 12 bis 14 Minuten garen. Quinoa nach Packungs-"
            "anweisung mit etwas Zitronenabrieb und -saft kochen. Brokkoli 5 Minuten"
            " daempfen und alles zusammen servieren."
        ),
        "benefit": (
            "Lachs liefert Omega-3-Fettsaeuren, die die Leberfettwerte senken und"
            " Entzuendungen reduzieren. Quinoa stabilisiert den Blutzucker und Brokkoli"
            " enthaelt Leber-schuetzende Bitterstoffe."
        ),
        "tm_instructions": (
            "Quinoa im Gareinsatz mit 350 ml Wasser 15 Min/100C/Stufe 1 garen, Brokkoli"
            " im Varoma 5 Min/Varoma/Stufe 1 daempfen und Lachs im Varoma-Einlegeboden"
            " 12 Min/Varoma/Stufe 1 mit Zitronenscheiben garen; alles im Mixtopf"
            " 5 Sek/Stufe 2 mit Dill vermengen."
        ),
    },
    {
        "name": "Huehnchen-Gemuese-Pfanne mit Kurkuma und Naturreis",
        "prep_time": "30 Minuten",
        "ingredients": [
            "200 g Haehnchenbrust",
            "150 g Naturreis",
            "1 rote Paprika",
            "1 Zucchini",
            "1 Zwiebel",
            "1 TL Kurkuma, 1 TL Paprikapulver",
            "1 EL Raps- oder Olivenoel",
            "Petersilie, Salz, Pfeffer",
        ],
        "instructions": (
            "Reis nach Packungsanweisung garen. Huehnchen in Streifen schneiden und in"
            " Oel mit Kurkuma und Paprika 5 Minuten anbraten. Zwiebel, Paprika und"
            " Zucchini zugeben und weitere 7 Minuten garen. Mit Reis servieren und mit"
            " Petersilie bestreuen."
        ),
        "benefit": (
            "Mageres Eiweiss und Kurkuma unterstuetzen die Leberentgiftung, das Gemuese"
            " liefert Antioxidantien und Ballaststoffe fuer stabile Blutwerte."
        ),
        "tm_instructions": (
            "Zwiebel, Paprika und Zucchini 5 Sek/Stufe 5 zerkleinern, Oel zufuegen und"
            " 5 Min/120C/Linkslauf/Stufe 1 anduensten; Huehnchenwuerfel im Varoma"
            " 15 Min/Varoma/Stufe 1 garen und anschliessend mit dem Gemuese"
            " vermengen; Naturreis im Gareinsatz 30 Min/100C/Stufe 1 kochen."
        ),
    },
    {
        "name": "Quinoa-Bowl mit Spinat, gebackenem Gemuese und Tahin-Dressing",
        "prep_time": "35 Minuten",
        "ingredients": [
            "200 g gekochte Quinoa",
            "1 Sueskartoffel",
            "1 rote Paprika",
            "2 Haende Babyspinat",
            "2 EL Tahin",
            "Saft von 0,5 Zitrone",
            "1 TL Ahornsirup",
            "1 EL mildes Olivenoel",
            "Salz, Pfeffer, Kreuzkuemmel",
        ],
        "instructions": (
            "Sueskartoffel und Paprika wuerfeln, mit 1 TL Oel und Kreuzkuemmel 20"
            " Minuten bei 200 C backen. Quinoa vorbereiten. Tahin mit Zitronensaft,"
            " Ahornsirup, Wasser und Salz zu einem Dressing verruehren. Bowl mit"
            " Spinat, Quinoa, Gemuese und Dressing anrichten."
        ),
        "benefit": (
            "Quinoa liefert pflanzliches Eiweiss und Magnesium fuer stabile Blutwerte,"
            " Sueskartoffel und Paprika bringen Carotinoide und Spinat liefert Folat."
        ),
        "tm_instructions": (
            "Quinoa im Gareinsatz mit 400 ml Wasser 20 Min/100C/Stufe 1 garen;"
            " Sueskartoffel und Paprika im Varoma 20 Min/Varoma/Stufe 1 daempfen;"
            " Dressing aus Tahin, Zitronensaft, Ahornsirup und Wasser 10 Sek/Stufe 4"
            " ruehren und alles im Mixtopf 5 Sek/Linkslauf/Stufe 2 mischen."
        ),
    },
    {
        "name": "Miso-Kabeljau mit Sesam-Spitzkohl und Vollkornnudeln",
        "prep_time": "28 Minuten",
        "ingredients": [
            "2 Kabeljaufilets",
            "2 EL helle Misopaste",
            "1 TL Sesamoel",
            "200 g Vollkornnudeln",
            "1 kleiner Spitzkohl",
            "1 Karotte",
            "Frischer Ingwer, Sesamsamen, Limette",
        ],
        "instructions": (
            "Kabeljau mit Misopaste, Sesamoel und Ingwer einstreichen und 12 Minuten"
            " bei 180 C backen. Nudeln kochen. Spitzkohl und Karotte fein schneiden,"
            " in einer Pfanne kurz sautieren und mit Limettensaft sowie Sesam abschmecken."
            " Alles zusammen anrichten."
        ),
        "benefit": (
            "Magerer Fisch und Miso liefern leicht verdauliches Eiweiss und Probiotika"
            " fuer die Leber. Spitzkohl enthaelt Schwefelverbindungen, die die"
            " Entgiftung unterstuetzen."
        ),
        "tm_instructions": (
            "Spitzkohl und Karotte 4 Sek/Stufe 4 zerkleinern, mit Sesamoel 5 Min/120C/"
            "Linkslauf/Stufe 1 sautieren; Nudeln im Mixtopf mit 1200 ml Wasser"
            " 10 Min/100C/Linkslauf/Stufe 1 kochen; Kabeljau im Varoma-Einlegeboden"
            " mit Misopaste 12 Min/Varoma/Stufe 1 garen und alles zusammenrichten."
        ),
    },
    {
        "name": "Tofu-Gado-Gado mit gruenen Bohnen und Erdnuss-Limetten-Sauce",
        "prep_time": "30 Minuten",
        "ingredients": [
            "200 g fester Tofu",
            "200 g gruene Bohnen",
            "1 kleine Salatgurke",
            "1 gelbe Paprika",
            "2 hart gekochte Eier (optional)",
            "2 EL Erdnussmus ohne Zucker",
            "1 Limette",
            "1 TL Sojasauce (natriumarm)",
            "1 TL Honig oder Ahornsirup",
        ],
        "instructions": (
            "Tofu wuerfeln und in einer Pfanne ohne Fett goldbraun anbraten. Bohnen 5"
            " Minuten blanchieren. Gemuese in Streifen schneiden. Erdnussmus mit"
            " Limettensaft, Sojasauce, Honig und etwas Wasser verruehren. Alles als"
            " Bowl servieren und mit Sauce betraeufeln."
        ),
        "benefit": (
            "Tofu liefert pflanzliches Eiweiss ohne viel Fett, Bohnen und Gemuese"
            " bringen Ballaststoffe und Kalium fuer ausgeglichene Blutwerte."
        ),
        "tm_instructions": (
            "Gemuese im Mixtopf 4 Sek/Stufe 4 zerkleinern; Bohnen 5 Min/Varoma/Stufe 1"
            " daempfen; Tofuwuerfel in Varoma-Einlegeboden 12 Min/Varoma/Stufe 1"
            " garen; Sauce aus Erdnussmus, Limettensaft, Sojasauce und Honig"
            " 15 Sek/Stufe 3 ruehren und alle Komponenten im Mixtopf 5 Sek/"
            "Linkslauf/Stufe 2 mischen."
        ),
    },
    {
        "name": "Sesam-Lachs-Poke mit Vollkornreis und Edamame",
        "prep_time": "20 Minuten",
        "ingredients": [
            "150 g Sushi-Lachs",
            "200 g gegarter Vollkornreis",
            "100 g Edamame",
            "1 Avocado",
            "1 kleine Mango",
            "2 EL Sojasauce (natriumarm)",
            "1 TL Sesamoel",
            "Sesamsamen, Koriander",
        ],
        "instructions": (
            "Reis vorbereiten. Lachs wuerfeln und kurz in Sojasauce und Sesamoel"
            " marinieren. Edamame blanchieren. Avocado und Mango wuerfeln. Alles"
            " zusammen in eine Schuessel geben und mit Sesam bestreuen."
        ),
        "benefit": (
            "Roh verarbeiteter Lachs liefert Omega-3-Fettsaeuren, Edamame und Vollkornreis"
            " stabilisieren den Blutzucker, Obst bringt Antioxidantien."
        ),
        "tm_instructions": (
            "Vollkornreis im Gareinsatz mit 900 ml Wasser 35 Min/100C/Stufe 1 garen;"
            " Edamame im Varoma 8 Min/Varoma/Stufe 1 daempfen; Marinade aus Sojasauce"
            " und Sesamoel 5 Sek/Stufe 2 ruehren, Lachs in Stuecken unterheben und"
            " mit vorbereitetem Obst im Mixtopf 5 Sek/Linkslauf/Stufe 1 vermengen."
        ),
    },
    {
        "name": "Mediterrane Kichererbsenpfanne mit Mangold und Tomaten",
        "prep_time": "22 Minuten",
        "ingredients": [
            "1 Dose Kichererbsen (abgespuelt)",
            "1 Bund Mangold",
            "200 g Kirschtomaten",
            "1 rote Zwiebel",
            "2 Knoblauchzehen",
            "1 EL Olivenoel",
            "1 TL geraucherte Paprika",
            "Frische Petersilie, Zitrone",
        ],
        "instructions": (
            "Zwiebel und Knoblauch hacken, in Oel anschwitzen. Kichererbsen zugeben und"
            " 5 Minuten braten. Mangoldstreifen und Tomaten zufuegen, weitere 5 Minuten"
            " garen. Mit Zitrone und Petersilie abschmecken."
        ),
        "benefit": (
            "Kichererbsen liefern Ballaststoffe und pflanzliches Eiweiss, Mangold und"
            " Tomaten bringen Folat, Kalium und Lycopin fuer gesunde Blutwerte."
        ),
        "tm_instructions": (
            "Zwiebel und Knoblauch 5 Sek/Stufe 5 zerkleinern, Olivenoel zugeben und"
            " 3 Min/120C/Stufe 1 anschwitzen; Kichererbsen, Mangoldstreifen und"
            " Tomaten zufuegen und 10 Min/100C/Linkslauf/Stufe 1 koecheln, zum Schluss"
            " mit Petersilie und Zitrone 5 Sek/Linkslauf/Stufe 2 vermengen."
        ),
    },
    {
        "name": "Spinat-Feta-Omelett mit Vollkornbrot",
        "prep_time": "12 Minuten",
        "ingredients": [
            "2 Eier",
            "1 Handvoll Babyspinat",
            "30 g Feta",
            "1 TL Olivenoel",
            "1 Scheibe Vollkornbrot",
            "Pfeffer, Muskat",
        ],
        "instructions": (
            "Eier verquirlen, Spinat hacken und mit Feta vermengen. In einer Pfanne mit"
            " Oel 3 Minuten stocken lassen, zusammenklappen und mit getoastetem"
            " Vollkornbrot servieren."
        ),
        "benefit": (
            "Eier liefern hochwertiges Protein fuer stabile Blutwerte, Spinat und Feta"
            " steuern Folat und Kalzium bei und die Zubereitung schont die Leber."
        ),
        "tm_instructions": (
            "Spinat und Feta 4 Sek/Stufe 4 hacken, Eier und Gewuerze zugeben und"
            " 8 Sek/Stufe 3 verruehren; Masse in eine geölte Varoma-Form geben und"
            " 15 Min/Varoma/Stufe 1 stocken lassen, Brot im Varoma-Einlegeboden"
            " in den letzten 3 Minuten mitwaermen."
        ),
    },
    {
        "name": "Quark-Beeren-Bowl mit Chiasamen",
        "prep_time": "10 Minuten",
        "ingredients": [
            "200 g Magerquark",
            "Handvoll Beerenmix",
            "1 EL Chiasamen",
            "1 TL Leinsamen",
            "1 TL Honig",
            "Etwas Zitronenabrieb",
        ],
        "instructions": (
            "Quark mit Honig und Zitronenabrieb glatt ruehren, Beeren und Samen"
            " unterheben und sofort servieren."
        ),
        "benefit": (
            "Quark liefert Eiweiss ohne viel Fett, Beeren bringen Antioxidantien und"
            " Chiasamen unterstuetzen die Verdauung sowie den Cholesterinspiegel."
        ),
        "tm_instructions": (
            "Chia- und Leinsamen 5 Sek/Stufe 8 mahlen, Quark mit Honig und Zitronenabrieb"
            " 20 Sek/Stufe 3 cremig ruehren und Beeren 5 Sek/Linkslauf/Stufe 2"
            " unterheben."
        ),
    },
    {
        "name": "Gruener Power-Salat mit Avocado und Grapefruit",
        "prep_time": "15 Minuten",
        "ingredients": [
            "2 Haende Babyspinat",
            "1 Avocado",
            "1 rosa Grapefruit",
            "2 EL gekochte Kichererbsen",
            "1 TL Olivenoel",
            "1 TL Limettensaft",
            "1 EL gehackte Walnuesse",
        ],
        "instructions": (
            "Spinat und Grapefruit in Stuecke zupfen, Avocado wuerfeln. Mit Kichererbsen"
            " und Walnuessen mischen. Oel mit Limettensaft verruehren und darueber geben."
        ),
        "benefit": (
            "Spinat, Grapefruit und Walnuesse liefern Folat, Vitamin C und Omega-3-Fette"
            " fuer starke Leber- und Blutwerte, Avocado spendet gesunde Fette."
        ),
        "is_salad": True,
        "tm_instructions": (
            "Walnuesse 3 Sek/Stufe 5 hacken, Dressing aus Olivenoel und Limettensaft"
            " 5 Sek/Stufe 4 ruehren, Spinat und Grapefruit 3 Sek/Linkslauf/Stufe 2"
            " vermengen und Avocado mit dem Spatel unterheben."
        ),
    },
    {
        "name": "Fenchel-Orangen-Salat mit Edamame",
        "prep_time": "18 Minuten",
        "ingredients": [
            "1 Fenchelknolle",
            "1 Orange",
            "100 g gegarte Edamame",
            "1 Handvoll Rucola",
            "1 TL Olivenoel",
            "1 TL Zitronensaft",
            "1 TL Senf",
            "Pfeffer, Salz",
        ],
        "instructions": (
            "Fenchel fein hobeln, Orange filetieren und mit Rucola sowie Edamame"
            " vermengen. Olivenoel, Zitronensaft, Senf, Salz und Pfeffer zu einem"
            " Dressing ruehren und unterheben."
        ),
        "benefit": (
            "Fenchel beruhigt die Verdauung, Orangen liefern Vitamin C und Edamame"
            " spenden pflanzliches Eiweiss fuer stabile Blutwerte."
        ),
        "is_salad": True,
        "tm_instructions": (
            "Fenchel 3 Sek/Stufe 5 hobeln, Edamame im Varoma 6 Min/Varoma/Stufe 1"
            " waermen, Dressing aus Olivenoel, Zitronensaft und Senf 6 Sek/Stufe 4"
            " ruehren und alles 4 Sek/Linkslauf/Stufe 2 mischen; Orangenfilets"
            " zuletzt mit dem Spatel unterheben."
        ),
    },
    {
        "name": "Bohnen-Chili mit Paprika und Mais",
        "prep_time": "35 Minuten",
        "ingredients": [
            "1 Dose Kidneybohnen (abgespuelt)",
            "1 Dose schwarze Bohnen (abgespuelt)",
            "2 Dosen stueckige Tomaten",
            "1 rote Paprika",
            "1 gelbe Paprika",
            "1 Dose Mais (ungesuesst)",
            "1 Zwiebel",
            "2 Knoblauchzehen",
            "1 TL Kreuzkuemmel, 1 TL Paprikapulver",
            "1 EL Olivenoel",
        ],
        "instructions": (
            "Zwiebel und Knoblauch in Oel anschwitzen, Paprika zugeben und 5 Minuten"
            " braten. Bohnen, Tomaten, Gewuerze und 200 ml Wasser zufuegen, 20 Minuten"
            " koecheln lassen. Mais einruhren und abschmecken. Ergibt etwa 5 Portionen,"
            " die sich nach dem Abkuehlen portionsweise einfrieren lassen."
        ),
        "benefit": (
            "Kidney- und schwarze Bohnen liefern pflanzliches Eiweiss und Ballaststoffe,"
            " Paprika und Tomaten bringen Vitamin C sowie Antioxidantien und das Gericht"
            " bleibt fettarm."
        ),
        "freezer_friendly": True,
        "freezer_note": "Nach dem Abkuehlen in 5 Behaelter fuellen und bis zu 3 Monate einfrieren. Zum Essen ueber Nacht auftauen und kurz aufwaermen.",
        "tm_instructions": (
            "Zwiebel und Knoblauch 5 Sek/Stufe 5 zerkleinern, Olivenoel zugeben und"
            " 3 Min/120C/Stufe 1 anschwitzen; Paprika zugeben und 5 Min/120C/"
            "Linkslauf/Stufe 1 garen, Bohnen, Tomaten, Gewuerze und 200 ml Wasser"
            " zufuegen und 20 Min/100C/Linkslauf/Stufe 1 koecheln, zum Schluss Mais"
            " 1 Min/Linkslauf/Stufe 1 unterziehen."
        ),
    },
    {
        "name": "Haehnchen-Gemuese-Eintopf mit Suesskartoffel",
        "prep_time": "45 Minuten",
        "ingredients": [
            "400 g Haehnchenbrust",
            "2 Sueskartoffeln",
            "2 Karotten",
            "2 Stangen Sellerie",
            "1 Zwiebel",
            "1 Liter natriumreduzierte Gemuese- oder Knochenbruehe",
            "1 TL Thymian, 1 Lorbeerblatt",
            "1 EL Raps- oder Olivenoel",
        ],
        "instructions": (
            "Haehnchen wuerfeln und in Oel 5 Minuten anbraten. Gemuese wuerfeln,"
            " hinzugeben und weitere 5 Minuten garen. Mit Bruehe auffuellen,"
            " Gewuerze zugeben und 25 Minuten koecheln. Ergibt 5 Portionen zum"
            " Einfrieren. Vor dem Portionieren Lorbeer entfernen."
        ),
        "benefit": (
            "Mageres Haehnchen und Gemuesebruehe liefern leicht verdauliches Eiweiss"
            " und Elektrolyte, Gemuese bringt Beta-Carotin und Kalium fuer Leber und Blut."
        ),
        "freezer_friendly": True,
        "freezer_note": "In 5 luftdichte Behaelter geben, einfrieren und bei Bedarf schonend aufwaermen.",
        "tm_instructions": (
            "Zwiebel, Sellerie und Karotten 5 Sek/Stufe 5 zerkleinern, Oel zufuegen"
            " und 4 Min/120C/Stufe 1 anschwitzen; Haehnchenwuerfel einfuellen und"
            " 20 Min/100C/Linkslauf/Stufe 1 mit Bruehe, Gewuerzen und Sueskartoffel"
            " garen; Lorbeer entnehmen und Portionsweise abfuellen."
        ),
    },
    {
        "name": "Gemuese-Lasagne mit Vollkornplatten und Ricotta",
        "prep_time": "50 Minuten",
        "ingredients": [
            "12 Vollkorn-Lasagneplatten",
            "300 g TK-Spinat",
            "200 g Champignons",
            "1 Zucchini",
            "1 Aubergine",
            "500 ml passierte Tomaten",
            "250 g Ricotta",
            "1 EL Olivenoel",
            "Basilikum, Oregano, Salz, Pfeffer",
        ],
        "instructions": (
            "Gemuese wuerfeln und in Oel 5 Minuten anbraten, Spinat zugeben. Mit"
            " Tomaten und Gewuerzen 10 Minuten koecheln lassen. In eine Auflaufform"
            " schichten: Sauce, Platten, Ricotta. Drei Lagen bilden, mit Sauce"
            " abschliessen und 25 Minuten bei 190 C backen. In 5 Portionen schneiden"
            " und einfrieren."
        ),
        "benefit": (
            "Viel Gemuese liefert Antioxidantien und Kalium, Vollkornplatten stabilisieren"
            " den Blutzucker und Ricotta spendet leicht verdauliches Eiweiss."
        ),
        "freezer_friendly": True,
        "freezer_note": "Portionen luftdicht verpacken und einfrieren, zum Verzehr ueber Nacht im Kuehlschrank auftauen und im Ofen erwaermen.",
        "tm_instructions": (
            "Champignons, Zucchini und Aubergine 5 Sek/Stufe 5 zerkleinern, Olivenoel"
            " zugeben und 10 Min/120C/Linkslauf/Stufe 1 garen; Spinat zufuegen und"
            " weitere 2 Min/100C/Linkslauf/Stufe 1 zusammenfallen lassen; Ricotta mit"
            " etwas Sauce 5 Sek/Stufe 3 glattruehren und Lasagne wie beschrieben"
            " schichten, anschliessend im Ofen backen."
        ),
    },
]

SNACKS = [
    {
        "timing": "Vormittag",
        "idea": "Handvoll Walnuesse und eine Birne",
        "reason": "Walnuesse bieten Omega-3-Fettsaeuren, die Leberfett reduzieren."
    },
    {
        "timing": "Vormittag",
        "idea": "Naturjoghurt mit Heidelbeeren und Leinsamen",
        "reason": "Leinsamen liefern Ballaststoffe fuer stabile Blutzuckerwerte."
    },
    {
        "timing": "Nachmittag",
        "idea": "Gemuese-Sticks (Karotte, Sellerie) mit Hummus",
        "reason": "Hummus liefert pflanzliches Eiweiss und Ballaststoffe fuer die Leber."
    },
    {
        "timing": "Nachmittag",
        "idea": "Apfel mit Mandelmus",
        "reason": "Kombination aus Fruchtzucker und gesunden Fetten haelt satt ohne die Leber zu belasten."
    },
    {
        "timing": "Abend",
        "idea": "Beerenmix mit etwas Kefir",
        "reason": "Fermentierte Milchprodukte unterstuetzen die Darmflora und damit die Leber."
    },
]

BEVERAGE_TIPS = [
    "Mindestens 1,5 Liter stilles Wasser oder ungesuessten Tee ueber den Tag verteilt trinken.",
    "Morgens ein Glas lauwarmes Wasser mit Zitronensaft fuer die Leberaktivierung trinken.",
    "Gruener Tee am Nachmittag liefert Antioxidantien fuer gute Blutwerte.",
]

GENERAL_HINTS = [
    "Alle Gerichte lassen sich gut vorbereiten und halten im Kuehlschrank bis zu 2 Tage frisch.",
    "Bei Bedarf Vollkornbeilagen vorkochen und portioniert einfrieren, um Zeit zu sparen.",
    "Gewuerze wie Kurkuma, Kreuzkuemmel und Ingwer regelmaessig einsetzen, sie foerdern die Lebergesundheit.",
    "Fertige Portionen in BPA-freie Behaelter fuellen, datieren und optimalerweise innerhalb von 3 Monaten verbrauchen.",
]

OUTPUT_DIR = Path(__file__).resolve().parent / "wochenplaene"


def extract_meal_names_from_text(content: str) -> list[str]:
    """Liest Rezeptnamen aus einer Plan-Textdatei aus."""
    names: list[str] = []
    for line in content.splitlines():
        stripped = line.strip()
        if stripped.startswith("Gericht "):
            try:
                _, tail = stripped.split(":", 1)
            except ValueError:
                continue
            names.append(tail.strip())
    return names


def load_previous_meal_names(today: date) -> set[str]:
    """Ermittelt die Gerichte der letzten erzeugten Kalenderwoche."""
    iso_year, iso_week, _ = today.isocalendar()
    plan_files = sorted(OUTPUT_DIR.glob("wochenplan_*.txt"), reverse=True)
    for path in plan_files:
        stem = path.stem
        if not stem.startswith("wochenplan_"):
            continue
        date_str = stem.replace("wochenplan_", "")
        try:
            plan_date = date.fromisoformat(date_str)
        except ValueError:
            continue
        plan_year, plan_week, _ = plan_date.isocalendar()
        if (plan_year, plan_week) == (iso_year, iso_week):
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except OSError:
            continue
        names = extract_meal_names_from_text(content)
        if names:
            return set(names)
    return set()


def is_quick_meal(meal: dict[str, str]) -> bool:
    """Prueft, ob das Gericht spaetestens in 15 Minuten zubereitet ist."""
    time_str = meal.get("prep_time", "")
    try:
        minutes = int(time_str.split()[0])
    except (ValueError, IndexError):
        return False
    return minutes <= 15


def is_freezer_friendly(meal: dict[str, str]) -> bool:
    """Prueft, ob das Gericht fuer Batch-Cooking und Einfrieren markiert ist."""
    return bool(meal.get("freezer_friendly"))


def is_salad_meal(meal: dict[str, str]) -> bool:
    """Prueft, ob das Gericht als Salat markiert ist."""
    return bool(meal.get("is_salad"))


def select_plan(
    forbidden_meals: set[str] | None = None,
    attempts: int = 50,
) -> tuple[list[dict[str, str]], list[dict[str, str]], str]:
    """Waehlt zufaellige Hauptgerichte, Snacks und ein Getraenk."""
    forbidden_meals = forbidden_meals or set()

    def pick_once() -> tuple[list[dict[str, str]], list[dict[str, str]], str]:
        quick_options = [meal for meal in MEALS if is_quick_meal(meal)]
        freezer_options = [meal for meal in MEALS if is_freezer_friendly(meal)]
        salad_options = [meal for meal in MEALS if is_salad_meal(meal)]

        if not quick_options:
            raise RuntimeError("Keine schnellen Gerichte mit maximal 15 Minuten gefunden.")
        if not freezer_options:
            raise RuntimeError("Keine Gerichte zum Einfrieren markiert.")
        if not salad_options:
            raise RuntimeError("Keine Salate hinterlegt.")

        quick_meal = random.choice(quick_options)
        selected: list[dict[str, str]] = [quick_meal]

        freezer_candidates = [meal for meal in freezer_options if meal not in selected]
        freezer_meal = random.choice(freezer_candidates) if freezer_candidates else random.choice(freezer_options)
        if freezer_meal not in selected:
            selected.append(freezer_meal)

        salad_candidates = [meal for meal in salad_options if meal not in selected]
        salad_meal = random.choice(salad_candidates) if salad_candidates else random.choice(salad_options)
        if salad_meal not in selected:
            selected.append(salad_meal)

        remaining_pool = [meal for meal in MEALS if meal not in selected]
        needed = max(0, 3 - len(selected))
        if needed > 0:
            selected.extend(random.sample(remaining_pool, needed))

        meals = selected[:3]
        random.shuffle(meals)
        snacks = random.sample(SNACKS, 2)
        beverage_tip = random.choice(BEVERAGE_TIPS)
        return meals, snacks, beverage_tip

    best_choice: tuple[list[dict[str, str]], list[dict[str, str]], str] | None = None
    best_overlap: int | None = None

    for _ in range(attempts):
        meals, snacks, beverage_tip = pick_once()
        if not forbidden_meals:
            return meals, snacks, beverage_tip
        overlap = len({meal["name"] for meal in meals} & forbidden_meals)
        if overlap == 0:
            return meals, snacks, beverage_tip
        if best_choice is None or best_overlap is None or overlap < best_overlap:
            best_choice = (meals, snacks, beverage_tip)
            best_overlap = overlap

    if best_choice is not None:
        return best_choice

    return pick_once()


def build_text(today: date, meals: list[dict[str, str]], snacks: list[dict[str, str]], beverage_tip: str) -> str:
    """Erstellt den Textinhalt fuer den Wochenplan."""
    lines: list[str] = []
    lines.append("Woechentliche Ernaehrung (leberwertfreundlich)")
    lines.append("")

    for idx, meal in enumerate(meals, start=1):
        lines.append(f"Gericht {idx}: {meal['name']}")
        lines.append(f"Zubereitungszeit: {meal['prep_time']}")
        lines.append("Zutaten:")
        for ingredient in meal["ingredients"]:
            lines.append(f"- {ingredient}")
        lines.append(f"Zubereitung: {meal['instructions']}")
        lines.append(f"Naehrwertfokus: {meal['benefit']}")
        if meal.get("freezer_friendly"):
            note = meal.get(
                "freezer_note",
                "Nach dem Abkuehlen portionsweise einfrieren und bei Bedarf aufwaermen.",
            )
            lines.append(f"Batch-Tipp: {note}")
        tm_hint = meal.get("tm_instructions")
        if tm_hint:
            lines.append(f"Thermomix: {tm_hint}")
        lines.append("")

    lines.append("Zwischenmahlzeiten-Empfehlung:")
    for snack in snacks:
        lines.append(f"- {snack['timing']}: {snack['idea']} ({snack['reason']})")
    lines.append("")

    lines.append("Getraenke-Tipp:")
    lines.append(f"- {beverage_tip}")
    lines.append("")

    lines.append("Allgemeine Hinweise:")
    for hint in GENERAL_HINTS:
        lines.append(f"- {hint}")

    return "\n".join(lines)


def build_html(today: date, meals: list[dict[str, str]], snacks: list[dict[str, str]], beverage_tip: str) -> str:
    """Erstellt eine HTML-Version des Wochenplans."""
    meal_sections = []
    for idx, meal in enumerate(meals, start=1):
        ingredients = "".join(f"<li>{ingredient}</li>" for ingredient in meal["ingredients"])
        section = (
            f"<section>"
            f"<h2>Gericht {idx}: {meal['name']}</h2>"
            f"<p><strong>Zubereitungszeit:</strong> {meal['prep_time']}</p>"
            f"<h3>Zutaten</h3>"
            f"<ul>{ingredients}</ul>"
            f"<p><strong>Zubereitung:</strong> {meal['instructions']}</p>"
            f"<p><strong>Naehrwertfokus:</strong> {meal['benefit']}</p>"
        )
        if meal.get("freezer_friendly"):
            note = meal.get(
                "freezer_note",
                "Nach dem Abkuehlen portionsweise einfrieren und bei Bedarf aufwaermen.",
            )
            section += f"<p><strong>Batch-Tipp:</strong> {note}</p>"
        tm_hint = meal.get("tm_instructions")
        if tm_hint:
            section += f"<p><strong>Thermomix:</strong> {tm_hint}</p>"
        section += "</section>"
        meal_sections.append(section)

    snack_items = "".join(
        f"<li><strong>{snack['timing']}:</strong> {snack['idea']} ({snack['reason']})</li>"
        for snack in snacks
    )
    hint_items = "".join(f"<li>{hint}</li>" for hint in GENERAL_HINTS)

    html = f"""
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="utf-8" />
        <title>Woechentliche Ernaehrung (leberwertfreundlich)</title>
  <style>
    body {{ font-family: Arial, sans-serif; line-height: 1.5; margin: 2rem; }}
    h1 {{ color: #1f4d3a; }}
    section {{ border-bottom: 1px solid #d0d7de; padding-bottom: 1rem; margin-bottom: 1.5rem; }}
    ul {{ margin: 0.5rem 0 1rem 1.5rem; }}
  </style>
</head>
<body>
    <h1>Woechentliche Ernaehrung (leberwertfreundlich)</h1>
  {''.join(meal_sections)}
  <section>
    <h2>Zwischenmahlzeiten-Empfehlung</h2>
    <ul>{snack_items}</ul>
  </section>
  <section>
    <h2>Getraenke-Tipp</h2>
    <p>{beverage_tip}</p>
  </section>
  <section>
    <h2>Allgemeine Hinweise</h2>
    <ul>{hint_items}</ul>
  </section>
</body>
</html>
"""
    return "".join(line.rstrip() for line in html.splitlines(True))


def build_index_html(plan_files: list[Path]) -> str:
    """Erstellt eine Liste mit allen vorhandenen Wochenplaenen."""
    entries: dict[tuple[int, int], tuple[date, str, str]] = {}
    for path in plan_files:
        stem = path.stem
        if not stem.startswith("wochenplan_"):
            continue
        date_str = stem.replace("wochenplan_", "")
        try:
            plan_date = date.fromisoformat(date_str)
        except ValueError:
            continue
        iso_year, iso_week, _ = plan_date.isocalendar()
        href = f"kw{iso_week:02d}.html"
        if not (OUTPUT_DIR / href).exists():
            continue
        label = f"KW {iso_week:02d} ({iso_year})"
        key = (iso_year, iso_week)
        existing = entries.get(key)
        if existing is None or plan_date > existing[0]:
            entries[key] = (plan_date, href, label)

    if not entries:
        body = "<p>Noch keine Wochenplaene verfuegbar.</p>"
    else:
        ordered = sorted(entries.values(), key=lambda item: item[0], reverse=True)
        items = "".join(
            f"<li><a href='{href}'>{label}</a></li>"
            for _, href, label in ordered
        )
        body = f"<ul>{items}</ul>"

    html = f"""
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="utf-8" />
  <title>Ernaehrungsplaene</title>
  <style>
    body {{ font-family: Arial, sans-serif; line-height: 1.5; margin: 2rem; }}
    h1 {{ color: #1f4d3a; }}
    ul {{ margin-left: 1.5rem; }}
  </style>
</head>
<body>
  <h1>Alle Wochenplaene</h1>
  <p>Hier finden sich alle automatisch erzeugten Ernaehrungsplaene.</p>
  {body}
</body>
</html>
"""
    return "".join(line.rstrip() for line in html.splitlines(True))


def ensure_friday(force: bool) -> None:
    """Bricht ab, falls heute kein Freitag ist und kein Force-Flag gesetzt wurde."""
    today = date.today()
    if today.weekday() != 4 and not force:
        raise SystemExit(
            "Heute ist kein Freitag. Nutze die Option --force, um trotzdem einen Plan zu erstellen."
        )


def build_output_paths(today: date) -> tuple[Path, Path, Path, Path, int, int]:
    """Gibt Pfade fuer Text/HTML und KW-Aliasse zurueck und legt Ordner an."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    base_name = f"wochenplan_{today.isoformat()}"
    iso_year, iso_week, _ = today.isocalendar()
    alias_name = f"kw{iso_week:02d}"
    return (
        OUTPUT_DIR / f"{base_name}.txt",
        OUTPUT_DIR / f"{base_name}.html",
        OUTPUT_DIR / f"{alias_name}.txt",
        OUTPUT_DIR / f"{alias_name}.html",
        iso_week,
        iso_year,
    )


def main() -> None:
    """Erzeugt bei Bedarf eine neue Plan-Datei."""
    force = "--force" in sys.argv
    ensure_friday(force)

    today = date.today()
    paths = build_output_paths(today)
    text_path, html_path, kw_text_path, kw_html_path, iso_week, iso_year = paths
    if (text_path.exists() or html_path.exists() or kw_text_path.exists() or kw_html_path.exists()) and not force:
        raise SystemExit(
            "Es existiert bereits eine Datei fuer heute. Nutze --force, um sie zu ueberschreiben."
        )

    forbidden_meals = load_previous_meal_names(today)
    meals, snacks, beverage_tip = select_plan(forbidden_meals)
    content = build_text(today, meals, snacks, beverage_tip)
    html_content = build_html(today, meals, snacks, beverage_tip)

    text_path.write_text(content, encoding="utf-8")
    html_path.write_text(html_content, encoding="utf-8")
    kw_text_path.write_text(content, encoding="utf-8")
    kw_html_path.write_text(html_content, encoding="utf-8")

    html_plans = sorted(OUTPUT_DIR.glob("wochenplan_*.html"), reverse=True)
    index_content = build_index_html(html_plans)
    (OUTPUT_DIR / "index.html").write_text(index_content, encoding="utf-8")

    print(
        "Wochenplaene gespeichert unter"
        f" {text_path.name}, {html_path.name} sowie Alias kw{iso_week:02d}.html (KW {iso_week:02d}/{iso_year})"
    )


if __name__ == "__main__":
    main()
