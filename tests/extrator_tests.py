import pytest
from skopelib.extractor import SkopeExtractor

def test_class_create():
    e = SkopeExtractor()
    assert isinstance(e, SkopeExtractor)
