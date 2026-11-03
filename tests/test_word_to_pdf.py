from pathlib import Path
from pdfjin_word_to_pdf.core import convert_word_to_pdf


def test_import():
    assert callable(convert_word_to_pdf)
