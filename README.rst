The Daftish Documentation Theme
===============================

This is a theme for `Sphinx-generated documentation <http://sphinx-doc.org/>`_
based on the `Daft <http://daft-pgm.org>`_ website. It's licensed under the
`Creative Commons Attribution 3.0 License
<http://creativecommons.org/licenses/by/3.0/deed.en_US>`_.

Usage
-----

First, ``cd`` into your Sphinx-generated docs directory and clone the
``daftish`` repository:

::

    git clone https://github.com/dfm/daftish.git _themes

Add these lines to your Sphinx ``conf.py`` script:

::

    html_theme = "daftish"
    html_theme_path = ["_themes"]
    html_theme_options = {
            "tagline": "Beautiful.",
            "github": "https://github.com/dfm/daftish",
            "license_name": "CC Attribution 3.0 License",
            "license_link": "http://creativecommons.org/licenses/by/3.0/deed.en_US",
            # "google_analytics": "UA-XXXXXXXX-1",
        }
    html_sidebars = {
                "**": ["relations.html", "searchbox.html"]
            }
