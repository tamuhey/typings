"""
This type stub file was generated by pyright.
"""

from __future__ import unicode_literals
from ..tokenizer_exceptions import BASE_EXCEPTIONS
from ..norm_exceptions import BASE_NORMS
from ...language import Language
from ...attrs import LANG, NORM
from ...util import add_lookups, update_exc

class MultiLanguageDefaults(Language.Defaults):
    lex_attr_getters = ...
    tokenizer_exceptions = ...

class MultiLanguage(Language):
    """Language class to be used for models that support multiple languages.
    This module allows models to specify their language ID as 'xx'.
    """

    lang = ...
    Defaults = ...

__all__ = ["MultiLanguage"]