import sys
sys.path.insert(0, 'docutils.zip')

from docutils.core import publish_parts

def render_rst(rst):
    parts = publish_parts(
        source=rst, 
        writer_name="html4css1", 
        settings_overrides={
            '_disable_config': True,
            'embed_stylesheet': False,
            'stylesheet_path': 'static/docutils/html4css1.css',
        }
    )
    return parts['fragment']

def render_plain(text):
    return text
