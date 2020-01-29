# coding=utf-8

"""
author    = mdimai666 <mdimai666@gmail.com>
copyright = "2020"
license   = "MIT"
"""

from __future__ import absolute_import
from webassets.filter import Filter
from webassets_libsass import LibSass



__all__ = ('DLibSass',)

class DLibSass(Filter):
    """
    Convert SASS/SCSS to CSS.

    This uses a python extension module `libsass <http://dahlia.kr/libsass-python>`_
    which is binding C/C++ implementation of a Sass compiler `Libsass <https://github.com/hcatlin/libsass>`_

    """

    name = 'dlibsass'
    options = {
        'style': 'LIBSASS_STYLE',
        'includes': 'LIBSASS_INCLUDES',
        'images': 'LIBSASS_IMAGES',
    }


    def setup(self):
        super(DLibSass, self).setup()

        import sass
        self.sass = sass


    def input(self, _in, out, **kwargs):
        source_path = kwargs['source_path']
        print(type(source_path))
        print(source_path)

        out.write(
            self.sass.compile(
                filename=source_path,
                output_style='compressed',
                # include_paths=(self.includes if self.includes else []),
                # image_path=(self.images if self.images else '')
                # --dima--
                source_comments=True,
                source_map_contents=True,
                source_map_embed=True,
            )
        )
