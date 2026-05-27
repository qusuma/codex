import json
from pathlib import Path
import textwrap

ROOT = Path(__file__).resolve().parent
CONTENT = ROOT / "content"
ASSETS = ROOT / "assets" / "generated_images"
OUTPUT = ROOT / "output"

PAGE_W, PAGE_H = 612, 792  # letter points


def esc(text: str) -> str:
    return text.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')


def wrap_lines(text, width=68):
    return textwrap.wrap(text, width=width) or [""]


def parse_md_pages(md: str):
    pages, current, lines = {}, None, []
    for line in md.splitlines():
        if line.startswith("## Page "):
            if current is not None:
                pages[current] = lines
            current = int(line.split()[2].replace(":", ""))
            lines = []
        elif current is not None:
            lines.append(line.rstrip())
    if current is not None:
        pages[current] = lines
    return pages


def load_data():
    outline = json.loads((CONTENT / "page_outline.json").read_text())
    text_md = (CONTENT / "page_text.md").read_text()
    prompts = (CONTENT / "illustration_prompts.md").read_text()
    return outline, parse_md_pages(text_md), prompts


def watercolor_shapes(seed_shift=0):
    # pastel circles/ellipses as faux watercolor in PDF operators
    colors = [
        (0.84, 0.73, 0.76), (0.78, 0.70, 0.85), (0.72, 0.57, 0.65),
        (0.88, 0.80, 0.70), (0.66, 0.76, 0.67), (0.70, 0.80, 0.86),
    ]
    cmds = []
    for i, (r, g, b) in enumerate(colors):
        x = 70 + ((i * 87 + seed_shift * 33) % 470)
        y = 120 + ((i * 121 + seed_shift * 41) % 560)
        rad = 60 + ((i * 29 + seed_shift * 17) % 90)
        cmds.append(f"{r:.3f} {g:.3f} {b:.3f} rg")
        cmds.append(f"{x} {y} {rad} 0 360 arc f")
    return "\n".join(cmds)


def page_content(page_num, title, lines):
    parts = [
        "q",
        "0.96 0.93 0.87 rg 0 0 612 792 re f",  # paper
        watercolor_shapes(page_num),
        "Q",
        "0.45 0.36 0.31 RG 2 w 20 20 572 752 re S",
        "BT /F2 26 Tf 50 740 Td (" + esc(title) + ") Tj ET",
    ]
    y = 700
    for raw in lines:
        if not raw.strip():
            y -= 10
            continue
        line = raw.strip()
        if line.startswith("### "):
            txt = line[4:]
            parts.append(f"BT /F2 18 Tf 50 {y} Td ({esc(txt)}) Tj ET")
            y -= 28
        elif line.startswith("- "):
            for wrapped in wrap_lines("• " + line[2:], 72):
                parts.append(f"BT /F1 12 Tf 60 {y} Td ({esc(wrapped)}) Tj ET")
                y -= 18
        elif line.startswith("> "):
            parts.append(f"0.92 0.86 0.78 rg 45 {y-8} 522 28 re f")
            note = "Memory line: " + line[2:]
            for wrapped in wrap_lines(note, 70):
                parts.append(f"BT /F1 11 Tf 55 {y} Td ({esc(wrapped)}) Tj ET")
                y -= 16
            y -= 4
        else:
            for wrapped in wrap_lines(line, 72):
                parts.append(f"BT /F1 12 Tf 50 {y} Td ({esc(wrapped)}) Tj ET")
                y -= 18
    parts.append(f"BT /F2 12 Tf 560 30 Td ({page_num}) Tj ET")
    return "\n".join(parts)


def build_pdf(pages):
    objects = []

    def add_obj(data: bytes):
        objects.append(data)
        return len(objects)

    font1 = add_obj(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
    font2 = add_obj(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>")

    page_ids = []
    content_ids = []
    for p in pages:
        stream = p.encode("latin-1", "replace")
        cid = add_obj(f"<< /Length {len(stream)} >>\nstream\n".encode() + stream + b"\nendstream")
        content_ids.append(cid)
        pid = add_obj(b"TEMP")
        page_ids.append(pid)

    kids = " ".join(f"{pid} 0 R" for pid in page_ids)
    pages_id = add_obj(f"<< /Type /Pages /Count {len(page_ids)} /Kids [{kids}] >>".encode())

    for i, pid in enumerate(page_ids):
        page_dict = (
            f"<< /Type /Page /Parent {pages_id} 0 R /MediaBox [0 0 {PAGE_W} {PAGE_H}] "
            f"/Resources << /Font << /F1 {font1} 0 R /F2 {font2} 0 R >> >> /Contents {content_ids[i]} 0 R >>"
        )
        objects[pid - 1] = page_dict.encode()

    catalog_id = add_obj(f"<< /Type /Catalog /Pages {pages_id} 0 R >>".encode())

    out = b"%PDF-1.4\n"
    offsets = [0]
    for i, obj in enumerate(objects, start=1):
        offsets.append(len(out))
        out += f"{i} 0 obj\n".encode() + obj + b"\nendobj\n"
    xref_pos = len(out)
    out += f"xref\n0 {len(objects)+1}\n".encode()
    out += b"0000000000 65535 f \n"
    for i in range(1, len(objects)+1):
        out += f"{offsets[i]:010d} 00000 n \n".encode()
    out += f"trailer\n<< /Size {len(objects)+1} /Root {catalog_id} 0 R >>\nstartxref\n{xref_pos}\n%%EOF\n".encode()
    return out


def main():
    ASSETS.mkdir(parents=True, exist_ok=True)
    OUTPUT.mkdir(parents=True, exist_ok=True)
    outline, page_text, _ = load_data()

    page_streams = []
    for p in outline["pages"]:
        n, title = p["page"], p["title"]
        lines = page_text.get(n, [])
        page_streams.append(page_content(n, title, lines))
        (ASSETS / f"page_{n:02d}_art.txt").write_text(f"Decorative watercolor vector instructions for page {n}.\n")

    pdf_bytes = build_pdf(page_streams)
    out_path = OUTPUT / "story_of_ghrelin_and_leptin.pdf"
    out_path.write_bytes(pdf_bytes)
    print(f"Created: {out_path}")


if __name__ == "__main__":
    main()
