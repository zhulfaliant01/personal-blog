import markdown
from django.utils.html import escape
import re

def render_plaintext(content):
    paragraphs = re.split(r'\n\s*\n', escape(content))
    return ''.join(f'<p>{p.strip()}</p>' for p in paragraphs)

def render_markdown(is_markdown, content):
    if is_markdown:
        html = markdown.markdown(content, extensions=["extra", "fenced_code", "codehilite", "tables"])
        #print(is_markdown, html)
        return html
    else:
        html = render_plaintext(content)
        #print(is_markdown, html)
        return html
