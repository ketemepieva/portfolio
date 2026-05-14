"""
Génère un CV PDF (A4) structuré et visuellement soigné.
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
from reportlab.platypus import (
    Image,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

ROOT = Path(__file__).resolve().parents[1]
OUT_PDF = ROOT / "public" / "CV_Fidella_Maeva_Ketemepi_professionnel.pdf"
PHOTO_DST = ROOT / "public" / "cv-photo.png"
PHOTO_SRC_CANDIDATES = [
    Path(
        r"C:\Users\HP ELITEBOOK G5\.cursor\projects\c-Users-HP-ELITEBOOK-G5-OneDrive-Desktop-Porfolio\assets\c__Users_HP_ELITEBOOK_G5_AppData_Roaming_Cursor_User_workspaceStorage_8e42555df083737d19dd88fcc6a60f87_images_Capture_d__cran_2026-05-14_142225-02a1ab76-399f-4c37-ace4-3cd2691bed70.png"
    ),
]

COL_TEAL = colors.HexColor("#0f766e")
COL_TEAL_DARK = colors.HexColor("#134e4a")
COL_MINT = colors.HexColor("#99f6e4")
COL_CARD = colors.HexColor("#f8fafc")
COL_BORDER = colors.HexColor("#e2e8f0")
COL_TEXT = colors.HexColor("#1e293b")
COL_MUTED = colors.HexColor("#64748b")
COL_WHITE = colors.white

PAGE_W, PAGE_H = A4
MARGIN_X = 1.35 * cm
MARGIN_Y = 1.15 * cm
CONTENT_W = PAGE_W - 2 * MARGIN_X


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
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def vstack_table(flows: list, col_w: float, pad: float = 8) -> Table:
    """Une colonne : une ligne par flowable."""
    rows = [[f] for f in flows]
    t = Table(rows, colWidths=[col_w])
    t.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), pad),
                ("RIGHTPADDING", (0, 0), (-1, -1), pad),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ]
        )
    )
    return t


def accent_bar_section(
    title: str,
    flows: list,
    styles: dict,
    total_width: float,
    bar_w: float = 0.38 * cm,
) -> Table:
    """Bloc : barre verticale teal + zone contenu (carte)."""
    inner_w = total_width - bar_w
    inner = vstack_table(
        [
            Paragraph(
                f"<b><font size=11 color='#0f766e'>{esc(title)}</font></b>",
                styles["section_head"],
            ),
            Spacer(1, 0.1 * cm),
        ]
        + flows,
        inner_w,
        pad=10,
    )
    spacer_cell = Paragraph("<font size=1> </font>", styles["tiny"])
    tbl = Table([[spacer_cell, inner]], colWidths=[bar_w, inner_w])
    tbl.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (0, 0), COL_TEAL),
                ("BACKGROUND", (1, 0), (1, 0), COL_CARD),
                ("BOX", (0, 0), (-1, -1), 0.75, COL_BORDER),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    return tbl


def project_card(title: str, desc: str, tags: str, styles: dict, w: float) -> Table:
    inner = vstack_table(
        [
            Paragraph(
                f'<b><font size="10" color="#0f766e">{esc(title)}</font></b>',
                styles["proj_title"],
            ),
            Spacer(1, 0.08 * cm),
            Paragraph(esc(desc), styles["body"]),
            Spacer(1, 0.15 * cm),
            Paragraph(
                f'<font size="7.5" color="#64748b"><i>{esc(tags)}</i></font>',
                styles["tagline"],
            ),
        ],
        w - 16,
        pad=0,
    )
    wrap = Table([[inner]], colWidths=[w])
    wrap.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#ffffff")),
                ("BOX", (0, 0), (-1, -1), 0.6, COL_BORDER),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                ("TOPPADDING", (0, 0), (-1, -1), 10),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
                ("ROWBACKGROUNDS", (0, 0), (-1, -1), [colors.HexColor("#ffffff")]),
            ]
        )
    )
    return wrap


def build_styles() -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    return {
        "hero_name": ParagraphStyle(
            name="hero_name",
            parent=base["Normal"],
            fontName="CVArial-Bold",
            fontSize=20,
            leading=24,
            textColor=COL_WHITE,
            spaceAfter=4,
        ),
        "hero_tag": ParagraphStyle(
            name="hero_tag",
            parent=base["Normal"],
            fontName="CVArial",
            fontSize=11,
            leading=14,
            textColor=COL_MINT,
            spaceAfter=8,
        ),
        "hero_contact": ParagraphStyle(
            name="hero_contact",
            parent=base["Normal"],
            fontName="CVArial",
            fontSize=9,
            leading=12,
            textColor=COL_WHITE,
        ),
        "section_head": ParagraphStyle(
            name="section_head",
            parent=base["Normal"],
            fontName="CVArial-Bold",
            fontSize=11,
            leading=14,
            textColor=COL_TEAL,
        ),
        "side_kicker": ParagraphStyle(
            name="side_kicker",
            parent=base["Normal"],
            fontName="CVArial-Bold",
            fontSize=8,
            leading=11,
            textColor=COL_WHITE,
            alignment=TA_LEFT,
        ),
        "side_body": ParagraphStyle(
            name="side_body",
            parent=base["Normal"],
            fontName="CVArial",
            fontSize=8.5,
            leading=11.5,
            textColor=colors.HexColor("#e2e8f0"),
        ),
        "body": ParagraphStyle(
            name="body",
            parent=base["Normal"],
            fontName="CVArial",
            fontSize=9.5,
            leading=13.5,
            textColor=COL_TEXT,
            alignment=TA_JUSTIFY,
        ),
        "body_left": ParagraphStyle(
            name="body_left",
            parent=base["Normal"],
            fontName="CVArial",
            fontSize=9.5,
            leading=13.5,
            textColor=COL_TEXT,
            alignment=TA_LEFT,
        ),
        "proj_title": ParagraphStyle(
            name="proj_title",
            parent=base["Normal"],
            fontName="CVArial-Bold",
            fontSize=10,
            leading=12,
            alignment=TA_LEFT,
        ),
        "tagline": ParagraphStyle(
            name="tagline",
            parent=base["Normal"],
            fontName="CVArial",
            fontSize=7.5,
            leading=10,
            alignment=TA_LEFT,
        ),
        "tiny": ParagraphStyle(
            name="tiny",
            parent=base["Normal"],
            fontName="CVArial",
            fontSize=7,
            leading=9,
            textColor=COL_MUTED,
        ),
    }


def build_story(styles: dict[str, ParagraphStyle], photo_path: Path) -> list:
    story: list = []
    W = CONTENT_W

    img = Image(str(photo_path))
    img.drawWidth = 2.85 * cm
    img.drawHeight = 2.85 * cm

    hero_left = vstack_table(
        [
            Paragraph("KETEMEPI Fidella Maeva", styles["hero_name"]),
            Paragraph(
                "Génie informatique · Développement web &amp; data",
                styles["hero_tag"],
            ),
            Paragraph(
                "Lomé, Togo<br/>"
                "Tél. : <b>à compléter</b> · E-mail : <b>à compléter</b>",
                styles["hero_contact"],
            ),
        ],
        W * 0.62,
        pad=14,
    )

    photo_cell = Table(
        [[img]],
        colWidths=[W * 0.38 - 0.2 * cm],
    )
    photo_cell.setStyle(
        TableStyle(
            [
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#ecfdf5")),
                ("TOPPADDING", (0, 0), (-1, -1), 12),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
            ]
        )
    )

    hero = Table([[hero_left, photo_cell]], colWidths=[W * 0.62, W * 0.38])
    hero.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (0, -1), COL_TEAL_DARK),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LINEAFTER", (0, 0), (0, -1), 0, colors.white),
                ("BOX", (0, 0), (-1, -1), 0, COL_BORDER),
            ]
        )
    )
    story.append(hero)
    story.append(Spacer(1, 0.35 * cm))

    # Bandeau synthétique (évite un tableau 2 colonnes trop haut pour une page)
    rw = W / 3.0
    lang_cell = vstack_table(
        [
            Paragraph("<b><font size=8 color='white'>LANGUES</font></b>", styles["side_kicker"]),
            Paragraph(
                "Français : courant<br/>Anglais : basique<br/><i>(progression)</i>",
                styles["side_body"],
            ),
        ],
        rw - 10,
        pad=8,
    )
    soft_txt = (
        "<b><font size=8 color='white'>RELATION CLIENT</font></b><br/><br/>"
        "Communication · Convaincre · Écoute · Multi-profils · Service"
    )
    soft_cell = vstack_table(
        [Paragraph(soft_txt, styles["side_body"])],
        rw - 10,
        pad=8,
    )
    qual_txt = (
        "<b><font size=8 color='white'>QUALITÉS</font></b><br/><br/>"
        "Dynamisme · Contact · Persévérance · Adaptabilité · Curiosité tech."
    )
    qual_cell = vstack_table([Paragraph(qual_txt, styles["side_body"])], rw - 10, pad=8)
    ribbon = Table([[lang_cell, soft_cell, qual_cell]], colWidths=[rw, rw, rw])
    ribbon.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), COL_TEAL),
                ("BOX", (0, 0), (-1, -1), 0.75, COL_BORDER),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LINEAFTER", (0, 0), (1, -1), 0.35, colors.HexColor("#5eead4")),
            ]
        )
    )
    story.append(ribbon)
    story.append(Spacer(1, 0.4 * cm))

    main_w = W

    story.append(
        accent_bar_section(
            "Profil",
            [
                Paragraph(
                    esc(
                        "Profil orienté relation client et projets numériques. En formation en "
                        "génie informatique, je relie aisance communicationnelle, sens du service "
                        "et pratique concrète du développement web, de l’analyse de données et des "
                        "bases SQL — avec une approche structurée et rigoureuse."
                    ),
                    styles["body"],
                ),
            ],
            styles,
            main_w,
        )
    )
    story.append(Spacer(1, 0.3 * cm))

    story.append(
        accent_bar_section(
            "Formation",
            [
                Paragraph(
                    esc(
                        "<b>Génie informatique</b> — formation en cours. "
                        "Projets personnels et académiques : applications web full-stack, "
                        "data science appliquée, sensibilisation aux bonnes pratiques (versioning, déploiement)."
                    ),
                    styles["body"],
                ),
            ],
            styles,
            main_w,
        )
    )
    story.append(Spacer(1, 0.3 * cm))

    tech_pills = [
        "React 19",
        "TypeScript",
        "Vite",
        "Node.js",
        "Express",
        "SQLite",
        "JWT",
        "Python",
        "Pandas",
        "Flask",
        "Git",
        "GitHub Actions",
        "Laravel",
    ]
    chips_txt = "  <font color='#94a3b8'>·</font>  ".join(
        [f"<b><font color='#0f766e'>{esc(p)}</font></b>" for p in tech_pills]
    )
    chips_para = Paragraph(f'<font size="8">{chips_txt}</font>', styles["body_left"])

    story.append(
        accent_bar_section(
            "Stack technique (aperçu)",
            [
                Paragraph(
                    "<b>Front</b> : React 19, React Router, Vite, Tailwind CSS 4 · "
                    "<b>Back</b> : Express, JWT, bcryptjs, Multer · "
                    "<b>Data</b> : Pandas, Matplotlib, Seaborn, exports CSV · "
                    "<b>PHP</b> : écosystème Laravel (doc officielle).",
                    styles["body"],
                ),
                Spacer(1, 0.2 * cm),
                chips_para,
            ],
            styles,
            main_w,
        )
    )
    story.append(Spacer(1, 0.3 * cm))

    story.append(
        Paragraph(
            "<b><font color='#0f766e'>Projets sélectionnés</font></b> — réalisations et cadrages récents.",
            styles["body_left"],
        )
    )
    story.append(Spacer(1, 0.18 * cm))

    projects = [
        (
            "SkillSwap",
            "Plateforme d’échange de compétences : authentification, profils enrichis, "
            "messagerie, notifications, feed communautaire, recherche et filtres avancés.",
            "React 19 · Vite · Express · SQLite · JWT",
        ),
        (
            "Analyse des ventes",
            "TP complet : schéma SQLite, données simulées, Pandas, KPI, graphiques "
            "Matplotlib/Seaborn, exports CSV, dashboard HTML, saisie Flask optionnelle.",
            "Python · SQLite · Pandas · Flask · Jupyter",
        ),
        (
            "ALPHA_LAB",
            "Cadrage fonctionnel d’une application de gestion des analyses médicales "
            "(biochimie, hématologie, compte rendu) pour laboratoire.",
            "Analyse métier · UX documentaire",
        ),
        (
            "Portfolio professionnel",
            "Site vitrine du parcours technique, hébergé sur GitHub Pages avec pipeline de build.",
            "React · TypeScript · Vite · GitHub Actions",
        ),
    ]
    for title, desc, tags in projects:
        story.append(project_card(title, desc, tags, styles, main_w))
        story.append(Spacer(1, 0.18 * cm))

    return story


def main() -> None:
    reg, bold = find_windows_font()
    pdfmetrics.registerFont(TTFont("CVArial", reg))
    pdfmetrics.registerFont(TTFont("CVArial-Bold", bold))

    styles = build_styles()
    photo = ensure_photo()
    OUT_PDF.parent.mkdir(parents=True, exist_ok=True)

    doc = SimpleDocTemplate(
        str(OUT_PDF),
        pagesize=A4,
        leftMargin=MARGIN_X,
        rightMargin=MARGIN_X,
        topMargin=MARGIN_Y,
        bottomMargin=MARGIN_Y,
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
        print(f"Copie Cursor non effectuée ({e}).")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Erreur:", e, file=sys.stderr)
        sys.exit(1)
