import sys
from pathlib import Path
from typing import Union


def convert_word_to_pdf(input_docx: Union[str, Path], output_pdf: Union[str, Path]) -> Path:
    in_p = Path(input_docx).resolve()
    out_p = Path(output_pdf).resolve()
    out_p.parent.mkdir(parents=True, exist_ok=True)

    try:
        from docx2pdf import convert
        convert(str(in_p), str(out_p))
    except Exception:
        # Fallback to soffice / libreoffice if docx2pdf encounters non-Word OS
        import subprocess
        subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", str(out_p.parent), str(in_p)], check=True)
    return out_p
