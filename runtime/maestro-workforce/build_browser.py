"""Build the standalone deployment browser from the maintained browser sources."""
from pathlib import Path
import sys

root = Path(__file__).resolve().parent
source = root.parent.parent / "apps" / "maestro-browser-mvp"
html = (source / "index.html").read_text()
html = html.replace('<link rel="stylesheet" href="styles.css">', '<style>' + (source / "styles.css").read_text() + '</style>')
html = html.replace('<script src="app.js" defer></script>', '<script>' + (source / "app.js").read_text() + '</script>')
target = root / "public" / "index.html"
if "--check" in sys.argv:
    assert target.read_text() == html, "Standalone browser is stale; run build_browser.py"
else:
    target.write_text(html)
