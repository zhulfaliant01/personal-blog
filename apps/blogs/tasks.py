from huey.contrib.djhuey import task

from .methods import render_markdown


@task()
def task_render_markdown(is_markdown, content):
    return render_markdown(is_markdown, content)
