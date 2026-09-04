#!/usr/bin/env python3
"""Regenerates PHRASE_BANK.md.

The BJCP style guide reuses a lot of boilerplate sentences across styles
(e.g. "Honey varieties may be declared."). Different translators working on
different pages can end up phrasing the same English sentence differently in
PT-BR. This script finds those repeated English sentences and, where a page
containing that sentence has already been translated, pulls out the PT-BR
wording that was used for it as a "canonical" suggestion.

Source of the original (pre-translation) English text: commit a1f9111, the
initial commit that split the English PDF into this .tex tree, before any
translation happened. Every page in ORDERED_FILES existed in English in that
commit. Do not change GENESIS_COMMIT unless that commit is rewritten/lost.

Usage:
    python3 scripts/generate-phrase-bank.py > PHRASE_BANK.md

Re-run this after translating or revising a page, so newly-established
wording feeds back into the bank for the next translator to match.
"""
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

GENESIS_COMMIT = "a1f9111"
MIN_OCCURRENCES = 2
MIN_SENTENCE_LEN = 20

# (path, short code used in the "Páginas" column, friendly name)
ORDERED_FILES = [
    ("introduction-to-the-2026-mead-guidelines/header.tex", "Intro 2026", "Introdução às Diretrizes de Estilos de Hidromel 2026"),
    ("introduction-to-mead-styles/header.tex", "Preâmbulo", "Introdução aos Estilos de Hidromel (preâmbulo)"),
    ("introduction-to-mead-styles/aroma-and-flavor.tex", "Preâmbulo/Aroma", "Preâmbulo — Aroma e Sabor"),
    ("introduction-to-mead-styles/appearance.tex", "Preâmbulo/Aparência", "Preâmbulo — Aparência"),
    ("introduction-to-mead-styles/mouthfeel.tex", "Preâmbulo/Boca", "Preâmbulo — Sensação na Boca"),
    ("introduction-to-mead-styles/overall-impression.tex", "Preâmbulo/Impressão", "Preâmbulo — Impressão Geral"),
    ("introduction-to-mead-styles/ingredients.tex", "Preâmbulo/Ingredientes", "Preâmbulo — Ingredientes"),
    ("introduction-to-mead-styles/entry-instructions.tex", "Preâmbulo/Inscrição", "Preâmbulo — Instruções para Inscrição"),
    ("m1-traditional-mead/header.tex", "M1", "M1. Traditional Mead (preâmbulo)"),
    ("m1-traditional-mead/m1-a-dry-mead.tex", "M1A", "M1A. Dry Mead"),
    ("m1-traditional-mead/m1-b-semi-sweet-mead.tex", "M1B", "M1B. Semi-Sweet Mead"),
    ("m1-traditional-mead/m1-c-sweet-mead.tex", "M1C", "M1C. Sweet Mead"),
    ("m2-melomel/header.tex", "M2", "M2. Melomel (preâmbulo)"),
    ("m2-melomel/m2-a-cyser.tex", "M2A", "M2A. Cyser"),
    ("m2-melomel/m2-b-pyment.tex", "M2B", "M2B. Pyment"),
    ("m2-melomel/m2-c-berry-mead.tex", "M2C", "M2C. Berry Mead"),
    ("m2-melomel/m2-d-stone-fruit-mead.tex", "M2D", "M2D. Stone Fruit Mead"),
    ("m2-melomel/m2-e-other-fruit-mead.tex", "M2E", "M2E. Other Fruit Mead"),
    ("m3-spiced-mead/header.tex", "M3", "M3. Spiced Mead (preâmbulo)"),
    ("m3-spiced-mead/m3-a-metheglin.tex", "M3A", "M3A. Metheglin"),
    ("m3-spiced-mead/m3-b-vegetable-mead.tex", "M3B", "M3B. Vegetable Mead"),
    ("m3-spiced-mead/m3-c-fruit-and-spice-mead.tex", "M3C", "M3C. Fruit and Spice Mead"),
    ("m4-specialty-mead/header.tex", "M4", "M4. Specialty Mead (preâmbulo)"),
    ("m4-specialty-mead/m4-a-braggot.tex", "M4A", "M4A. Braggot"),
    ("m4-specialty-mead/m4-b-bochet.tex", "M4B", "M4B. Bochet"),
    ("m4-specialty-mead/m4-c-polish-mead.tex", "M4C", "M4C. Polish Mead"),
    ("m4-specialty-mead/m4-d-wood-aged-mead.tex", "M4D", "M4D. Wood-Aged Mead"),
    ("m4-specialty-mead/m4-e-barrel-aged-mead.tex", "M4E", "M4E. Barrel-Aged Mead"),
    ("m4-specialty-mead/m4-f-experimental-mead.tex", "M4F", "M4F. Experimental Mead"),
]
CODE_BY_PATH = {path: code for path, code, _ in ORDERED_FILES}


def get_original(path):
    return subprocess.run(
        ["git", "show", f"{GENESIS_COMMIT}:{path}"],
        capture_output=True, text=True, check=True,
    ).stdout


def get_current(path):
    return Path(path).read_text(encoding="utf-8")


def clean_latex(s):
    # Isolate \textbf{Label}: field labels onto their own line first, so a
    # label never glues onto the sentence that follows it (that would make
    # "Entrants must specify..." fail to match its other occurrences, since
    # not every field label is the same across styles).
    s = re.sub(r"\\textbf\{([^}]*)\}:", r"\n\1:\n", s)
    s = re.sub(r"\\textbf\{([^}]*)\}", r"\1", s)
    s = re.sub(r"\\textit\{([^}]*)\}", r"\1", s)
    s = re.sub(r"\\[a-zA-Z]+\*?", " ", s)
    s = s.replace("{", " ").replace("}", " ")
    s = s.replace("\\%", "%")
    s = re.sub(r"[ \t]+", " ", s)
    return s


def split_sentences(s):
    chunks = re.split(r"\n+", s)
    out = []
    for chunk in chunks:
        chunk = chunk.strip()
        if not chunk:
            continue
        protected = re.sub(
            r"\b(e\.g|i\.e|etc|vs|Mr|Mrs|No)\.",
            lambda m: m.group(0).replace(".", "<DOT>"),
            chunk,
        )
        parts = re.split(r"(?<=[.!?])\s+(?=[A-ZÁÀÂÃÉÍÓÔÕÚÇ(])", protected)
        parts = [p.replace("<DOT>", ".").strip() for p in parts]
        out.extend(parts)
    # drop fragments that are just a bare label (e.g. "Entry Instructions:")
    return [
        p for p in out
        if len(p) > MIN_SENTENCE_LEN
        and not re.fullmatch(r"[A-ZÁÀÂÃÉÍÓÔÕÚÇa-záàâãéíóôõúç ,]+:?", p)
    ]


def norm_key(sent):
    key = re.sub(r"[-\u2013\u2014]+", "-", sent)
    key = re.sub(r"[\u2018\u2019]", "'", key)
    key = re.sub(r"[\u201c\u201d]", '"', key)
    return re.sub(r"\s+", " ", key).strip().lower()


def get_labeled_blocks(raw_tex):
    """Splits a page on \\textbf{Label}: boundaries, pairing each label with
    the text that follows it up to the next label."""
    parts = re.split(r"(\\textbf\{[^}]*\}:)", raw_tex)
    return [(parts[i], parts[i + 1]) for i in range(1, len(parts) - 1, 2)]


def build_repeated_sentence_index():
    locations = defaultdict(list)
    for path, _, _ in ORDERED_FILES:
        for sent in split_sentences(clean_latex(get_original(path))):
            locations[norm_key(sent)].append((path, sent))
    return {k: v for k, v in locations.items() if len(v) >= MIN_OCCURRENCES}


def build_pt_alignment():
    """Best-effort EN->PT sentence alignment for already-translated pages.

    Aligns by \\textbf{Label}: block, then by sentence position within the
    block. Skips any block where the EN/PT sentence counts don't match,
    since that means the translation merged/split sentences and positional
    alignment would silently pair the wrong sentences.
    """
    alignment = {}
    for path, _, _ in ORDERED_FILES:
        orig_blocks = get_labeled_blocks(get_original(path))
        curr_blocks = get_labeled_blocks(get_current(path))
        if len(orig_blocks) != len(curr_blocks):
            continue  # page not translated yet, or its block structure changed
        for (_, obody), (_, cbody) in zip(orig_blocks, curr_blocks):
            o_sents = split_sentences(clean_latex(obody))
            c_sents = split_sentences(clean_latex(cbody))
            if len(o_sents) != len(c_sents) or not o_sents:
                continue
            for o, c in zip(o_sents, c_sents):
                key = norm_key(o)
                if key == norm_key(c):
                    continue  # page (or this block) not translated yet
                alignment[key] = c
    return alignment


def render_markdown(repeated, alignment):
    items = sorted(repeated.items(), key=lambda kv: -len(kv[1]))
    matched = sum(1 for k in repeated if k in alignment)

    lines = []
    lines.append("# Banco de frases repetidas")
    lines.append("")
    lines.append(
        "O guia original em inglês repete muitas frases padronizadas entre "
        "estilos (ex.: \"Honey varieties may be declared.\"). Esta lista "
        "existe pra garantir que, ainda que traduzidas por pessoas "
        "diferentes, essas frases fiquem com a mesma redação em PT-BR."
    )
    lines.append("")
    lines.append(
        f"Gerado por [`scripts/generate-phrase-bank.py`](scripts/generate-phrase-bank.py) "
        f"a partir do texto original em inglês (commit `{GENESIS_COMMIT}`, antes de "
        f"qualquer tradução). Considera frases com {MIN_OCCURRENCES}+ ocorrências "
        f"idênticas (comparação exata, após normalizar espaços/aspas/travessão e "
        f"remover marcação LaTeX) — variações de redação da mesma ideia não são "
        f"detectadas automaticamente."
    )
    lines.append("")
    lines.append(
        f"**{len(items)} frases repetidas** encontradas, cobrindo "
        f"{sum(len(v) for v in repeated.values())} ocorrências no total. "
        f"**{matched}/{len(items)}** já têm uma tradução canônica sugerida, extraída "
        f"das páginas já traduzidas."
    )
    lines.append("")
    lines.append("## Como usar")
    lines.append("")
    lines.append(
        "- Traduzindo ou revisando uma página: se uma frase dela aparece nesta "
        "lista **com** tradução canônica preenchida, use essa mesma redação."
    )
    lines.append(
        "- Se aparece na lista **sem** tradução canônica (coluna vazia), essa é a "
        "primeira vez que a frase está sendo traduzida — escolha a redação e, "
        "depois, rode o script de novo pra ela entrar como canônica pras próximas "
        "ocorrências."
    )
    lines.append(
        "- Depois de traduzir/revisar uma página, regenere este arquivo: "
        "`python3 scripts/generate-phrase-bank.py > PHRASE_BANK.md`."
    )
    lines.append("")
    lines.append("| Ocorrências | Frase original (EN) | Tradução canônica (PT-BR) | Páginas |")
    lines.append("| --- | --- | --- | --- |")
    for k, locs in items:
        en_example = locs[0][1].replace("|", "\\|")
        pt = alignment.get(k, "").replace("|", "\\|")
        pages = sorted({CODE_BY_PATH[p] for p, _ in locs}, key=lambda c: (len(c), c))
        pages_str = ", ".join(pages)
        pt_cell = pt if pt else "_(a definir)_"
        lines.append(f"| {len(locs)}x | {en_example} | {pt_cell} | {pages_str} |")
    lines.append("")
    return "\n".join(lines)


def main():
    repeated = build_repeated_sentence_index()
    alignment = build_pt_alignment()
    sys.stdout.write(render_markdown(repeated, alignment))


if __name__ == "__main__":
    main()
