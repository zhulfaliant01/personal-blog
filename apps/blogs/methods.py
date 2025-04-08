import markdown

def render_markdown(is_markdown, content):
    if is_markdown:
        return markdown.markdown(content)
    else:
        return content