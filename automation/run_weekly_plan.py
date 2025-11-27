#!/usr/bin/env python3
"""Fuehrt die Wochenplan-Generierung und anschliessende HTML-Aktualisierung aus."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

AUTOMATION_DIR = Path(__file__).resolve().parent
GENERATOR_SCRIPT = AUTOMATION_DIR / "generate_wochenplan.py"
UPDATE_SCRIPT = AUTOMATION_DIR / "wochenplaene" / "scripts" / "update_weekly_plan.py"
TARGET_DIR = AUTOMATION_DIR / "wochenplaene"
DOCS_ROOT = AUTOMATION_DIR.parent / "docs"
DOCS_TARGET = DOCS_ROOT / "automation" / "wochenplaene"


def run_step(arguments: list[str]) -> None:
    """Startet einen einzelnen Schritt und gibt Fehler direkt weiter."""
    subprocess.run(arguments, check=True)


def mirror_to_docs() -> None:
    """Kopiert aktuelle Ausgabe nach docs/, damit GitHub Pages sie veroeffentlicht."""
    DOCS_ROOT.mkdir(parents=True, exist_ok=True)
    if DOCS_TARGET.exists():
        shutil.rmtree(DOCS_TARGET)
    DOCS_TARGET.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(
        TARGET_DIR,
        DOCS_TARGET,
        ignore=shutil.ignore_patterns("logs", "*.log", "*.err"),
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Erzeugt und aktualisiert Wochenplaene")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Ueberschreibt bestehende Plaene (nur fuer manuelle Tests noetig)",
    )
    parser.add_argument(
        "--date",
        metavar="YYYY-MM-DD",
        help="Datum, fuer das der Plan generiert werden soll",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    python = sys.executable

    print("[weekly-plan] starte generierung ...", flush=True)
    generator_call = [python, str(GENERATOR_SCRIPT)]
    if args.force:
        generator_call.append("--force")
    if args.date:
        generator_call.extend(["--date", args.date])
    run_step(generator_call)

    print("[weekly-plan] aktualisiere HTML-Index ...", flush=True)
    run_step([python, str(UPDATE_SCRIPT), str(TARGET_DIR)])

    print("[weekly-plan] spiegele Dateien nach docs/...", flush=True)
    mirror_to_docs()

    print("[weekly-plan] abgeschlossen.", flush=True)


if __name__ == "__main__":
    main()
