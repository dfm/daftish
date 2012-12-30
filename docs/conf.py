# -*- coding: utf-8 -*-

source_suffix = ".rst"
master_doc = "index"

project = u"Daftish"
copyright = u"2012, Dan Foreman-Mackey"
version = "0.0.1"

exclude_patterns = ["_build"]
pygments_style = "sphinx"
html_theme = "daftish"
html_theme_options = {
        "tagline": "Beautiful Sphinx-generated documentation.",
        "github": "https://github.com/dfm/daftish",
        "license_name": "CC Attribution 3.0 License",
        "license_link":
                    "http://creativecommons.org/licenses/by/3.0/deed.en_US",
        "google_analytics": "UA-22909046-1",
    }
html_theme_path = ["_themes"]
html_sidebars = {
            "**": ["relations.html", "searchbox.html"]
        }
html_static_path = ["_static"]
html_show_sourcelink = False
