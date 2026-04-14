from pathlib import Path
from weasyprint import HTML
import sys

if len(sys.argv) != 3:
    print('uso: python3 gerar_pdf_relatorio.py <input.html> <output.pdf>')
    sys.exit(1)

src = Path(sys.argv[1]).resolve()
out = Path(sys.argv[2]).resolve()
out.parent.mkdir(parents=True, exist_ok=True)
HTML(filename=str(src)).write_pdf(str(out))
print(out)
