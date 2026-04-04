"""
Pelican plugin to combine CSS files into a single stylesheet.
"""
import os
from pelican import signals


def combine_css(pelican):
    """Combine CSS files into a single stylesheet."""
    theme_dir = pelican.settings.get('THEME')
    output_dir = pelican.settings.get('OUTPUT_PATH')
    siteurl = pelican.settings.get('SITEURL', '')

    if not theme_dir or not output_dir:
        return

    # Paths to CSS files
    css_files = []

    # Bootstrap CSS
    bootstrap_theme = pelican.settings.get('BOOTSTRAP_THEME')
    if bootstrap_theme:
        css_files.append(os.path.join(theme_dir, 'static/css', f'bootstrap.{bootstrap_theme}.min.css'))
    else:
        css_files.append(os.path.join(theme_dir, 'static/css', 'bootstrap.min.css'))

    # Font Awesome
    css_files.append(os.path.join(theme_dir, 'static/css', 'font-awesome.min.css'))

    # Pygments
    pygments_style = pelican.settings.get('PYGMENTS_STYLE', 'native')
    css_files.append(os.path.join(theme_dir, 'static/css/pygments', f'{pygments_style}.css'))

    # Optional CSS files
    if pelican.settings.get('DOCUTIL_CSS'):
        css_files.append(os.path.join(theme_dir, 'static/css', 'html4css1.css'))

    if pelican.settings.get('TYPOGRIFY'):
        css_files.append(os.path.join(theme_dir, 'static/css', 'typogrify.css'))

    # Theme style.css
    css_files.append(os.path.join(theme_dir, 'static/css', 'style.css'))

    # Read and combine CSS
    combined_css = ""
    for css_file in css_files:
        if os.path.exists(css_file):
            with open(css_file, 'r') as f:
                combined_css += f"/* {os.path.basename(css_file)} */\n"
                combined_css += f.read()
                combined_css += "\n\n"

    # Write combined CSS
    output_css_dir = os.path.join(output_dir, 'theme/css')
    os.makedirs(output_css_dir, exist_ok=True)

    combined_file = os.path.join(output_css_dir, 'combined.css')
    with open(combined_file, 'w') as f:
        f.write(combined_css)

    print(f"Combined CSS written to {combined_file}")


def register():
    """Register the plugin with Pelican."""
    signals.finalized.connect(combine_css)
