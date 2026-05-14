"""
Génère le CV PDF (A4) avec photo et contenu à jour.
Usage : python scripts/generate_cv_pdf.py
"""

from __future__ import annotations

import os
import shutil
import sys
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

ROOT = Path(__file__).resolve().parents[1]
OUT_PDF = ROOT / "public" / "CV_Fidella_Maeva_Ketemepi_professionnel.pdf"
PHOTO_DST = ROOT / "public" / "cv-photo.png"
PHOTO_SRC_CANDIDATES = [
    Path(
        r"C:\Users\HP ELITEBOOK G5\.cursor\projects\c-Users-HP-ELITEBOOK-G5-OneDrive-Desktop-Porfolio\assets\c__Users_HP_ELITEBOOK_G5_AppData_Roaming_Cursor_User_workspaceStorage_8e42555df083737d19dd88fcc6a60f87_images_Capture_d__cran_2026-05-14_142225-02a1ab76-399f-4c37-ace4-3cd2691bed70.png"
    ),
]


def find_windows_font() -> tuple[str, str]:
    windir = Path(os.environ.get("WINDIR", r"C:\Windows"))
    fonts = windir / "Fonts"
    reg = fonts / "arial.ttf"
    bold = fonts / "arialbd.ttf"
    if reg.is_file() and bold.is_file():
        return str(reg), str(bold)
    raise FileNotFoundError("Polices Arial introuvables (arial.ttf / arialbd.ttf).")


def ensure_photo() -> Path:
    if PHOTO_DST.is_file():
        return PHOTO_DST
    for src in PHOTO_SRC_CANDIDATES:
        if src.is_file():
            PHOTO_DST.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, PHOTO_DST)
            return PHOTO_DST
    raise FileNotFoundError("Photo introuvable. Placez cv-photo.png dans public/.")


def esc(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def build_story(styles: dict[str, ParagraphStyle], photo_path: Path) -> list:
    story: list = []

    img = Image(str(photo_path))
    img.drawWidth = 3.2 * cm
    img.drawHeight = 3.2 * cm

    title_block = Paragraph(
        "<b><font size=16>KETEMEPI Fidella Maeva</font></b><br/>"
        "<font size=10>Lomé, Togo<br/>"
        "Téléphone : à compléter<br/>"
        "E-mail : à compléter</font>",
        styles["header"],
    )

    header_tbl = Table(
        [[img, title_block]],
        colWidths=[3.5 * cm, 12.5 * cm],
    )
    header_tbl.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    story.append(header_tbl)
    story.append(Spacer(1, 0.35 * cm))

    story.append(Paragraph("<b>Profil</b>", styles["h2"]))
    story.append(
        Paragraph(
            esc(
                "Personne dynamique, communicative et persuasive, avec un fort intérêt "
                "pour la relation client et pour les projets numériques. En formation en "
                "génie informatique, j’associe aisance relationnelle, sens de l’écoute et "
                "pratique du développement web, de l’analyse de données et des bases de données."
            ),
            styles["body"],
        )
    )
    story.append(Spacer(1, 0.25 * cm))

    story.append(Paragraph("<b>Compétences clés</b>", styles["h2"]))
    story.append(Paragraph("<b>Relation client &amp; communication</b>", styles["h3"]))
    for line in [
        "Aisance dans la communication et l’expression orale",
        "Capacité à convaincre et argumenter",
        "Sens de l’écoute et compréhension des besoins clients",
        "Bonne interaction avec différents profils de clients",
        "Attitude professionnelle et sens du service",
    ]:
        story.append(Paragraph(f"• {esc(line)}", styles["bullet"]))
    story.append(Spacer(1, 0.15 * cm))

    story.append(Paragraph("<b>Informatique &amp; développement</b>", styles["h3"]))
    for line in [
        "Front-end : React 19, React Router, Vite, TypeScript, Tailwind CSS 4",
        "Back-end : Node.js, Express, API REST, authentification JWT (bcryptjs), upload Multer",
        "Bases de données : SQLite (Node better-sqlite3 ; Python)",
        "Python / data : Pandas, Matplotlib, Seaborn ; exports CSV ; contrôles qualité",
        "Outils : Flask (formulaires / saisie), Jupyter Notebook, pipeline d’analyse",
        "PHP : écosystème Laravel (routage, Eloquent, migrations, files d’attente — documentation officielle)",
        "Déploiement et outils : Git, GitHub, GitHub Pages, GitHub Actions (build statique)",
        "Projet full-stack documenté : plateforme d’échange de compétences (SkillSwap)",
        "Projet data : analyse des ventes (SQLite, KPI, visualisations, dashboard web)",
        "Cadrage fonctionnel : application de gestion d’analyses médicales (ALPHA_LAB)",
    ]:
        story.append(Paragraph(f"• {esc(line)}", styles["bullet"]))

    story.append(Spacer(1, 0.25 * cm))
    story.append(Paragraph("<b>Qualités personnelles</b>", styles["h2"]))
    for line in [
        "Dynamisme",
        "Sens du contact",
        "Persévérance",
        "Adaptabilité",
        "Motivation et envie d’apprendre",
    ]:
        story.append(Paragraph(f"• {esc(line)}", styles["bullet"]))

    story.append(Spacer(1, 0.25 * cm))
    story.append(Paragraph("<b>Formation</b>", styles["h2"]))
    story.append(
        Paragraph(
            esc("Études en génie informatique (formation en cours)."),
            styles["body"],
        )
    )

    story.append(Spacer(1, 0.25 * cm))
    story.append(Paragraph("<b>Projets &amp; réalisations techniques</b>", styles["h2"]))
    story.append(
        Paragraph(
            "<b>SkillSwap</b> — plateforme d’échange de compétences : authentification, "
            "profils enrichis, messagerie, feed communautaire, recherche et filtres ; "
            "stack React 19, Vite, Express, SQLite.",
            styles["body"],
        )
    )
    story.append(
        Paragraph(
            "<b>Analyse des ventes</b> — TP complet : schéma SQLite, données simulées, "
            "Pandas, KPI, graphiques Matplotlib/Seaborn, exports CSV, dashboard HTML, "
            "interface Flask optionnelle.",
            styles["body"],
        )
    )
    story.append(
        Paragraph(
            "<b>ALPHA_LAB</b> — cadrage d’une application de gestion des analyses "
            "médicales (biochimie, hématologie, compte rendu) pour laboratoire.",
            styles["body"],
        )
    )
    story.append(
        Paragraph(
            "<b>Portfolio</b> — site vitrine React/Vite/TypeScript, hébergé sur GitHub Pages.",
            styles["body"],
        )
    )

    story.append(Spacer(1, 0.25 * cm))
    story.append(Paragraph("<b>Langues</b>", styles["h2"]))
    story.append(
        Paragraph(
            "Français : courant<br/>Anglais : niveau basique (en amélioration)",
            styles["body"],
        )
    )

    return story


def main() -> None:
    reg, bold = find_windows_font()
    pdfmetrics.registerFont(TTFont("CVArial", reg))
    pdfmetrics.registerFont(TTFont("CVArial-Bold", bold))

    base = getSampleStyleSheet()
    styles = {
        "header": ParagraphStyle(
            name="header",
            parent=base["Normal"],
            fontName="CVArial",
            fontSize=10,
            leading=13,
            alignment=TA_LEFT,
        ),
        "h2": ParagraphStyle(
            name="h2",
            parent=base["Heading2"],
            fontName="CVArial-Bold",
            fontSize=11,
            leading=14,
            textColor=colors.HexColor("#0f766e"),
            spaceBefore=6,
            spaceAfter=4,
        ),
        "h3": ParagraphStyle(
            name="h3",
            parent=base["Normal"],
            fontName="CVArial-Bold",
            fontSize=10,
            leading=13,
            spaceBefore=4,
            spaceAfter=2,
        ),
        "body": ParagraphStyle(
            name="body",
            parent=base["Normal"],
            fontName="CVArial",
            fontSize=9.5,
            leading=13,
            alignment=TA_JUSTIFY,
        ),
        "bullet": ParagraphStyle(
            name="bullet",
            parent=base["Normal"],
            fontName="CVArial",
            fontSize=9.5,
            leading=12.5,
            leftIndent=12,
            bulletIndent=0,
            alignment=TA_LEFT,
        ),
    }

    photo = ensure_photo()
    OUT_PDF.parent.mkdir(parents=True, exist_ok=True)

    doc = SimpleDocTemplate(
        str(OUT_PDF),
        pagesize=A4,
        leftMargin=1.8 * cm,
        rightMargin=1.8 * cm,
        topMargin=1.5 * cm,
        bottomMargin=1.5 * cm,
        title="CV — KETEMEPI Fidella Maeva",
        author="KETEMEPI Fidella Maeva",
    )
    doc.build(build_story(styles, photo))
    print(f"PDF généré : {OUT_PDF}")

    cursor_pdf = Path(
        r"c:\Users\HP ELITEBOOK G5\AppData\Roaming\Cursor\User\workspaceStorage\8e42555df083737d19dd88fcc6a60f87\pdfs\ddae6625-eca6-4e04-8395-709de5817e76\CV_Fidella_Maeva_Ketemepi_professionnel.pdf"
    )
    try:
        if cursor_pdf.parent.is_dir():
            shutil.copy2(OUT_PDF, cursor_pdf)
            print(f"Copie vers dossier Cursor : {cursor_pdf}")
    except OSError as e:
        print(f"Copie Cursor non effectuée ({e}). Le PDF reste dans public/.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Erreur:", e, file=sys.stderr)
        sys.exit(1)
