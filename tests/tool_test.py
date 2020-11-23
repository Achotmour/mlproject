# -*- coding: UTF-8 -*-

# Import from standard library
import os
import mlproject
# Import from our lib
from mlproject.tools import haversine
import pytest

def test_haversine():
    a = haversine(0,0,0,0)
    assert a == 0
    assert type(haversine(10,10,20,20)) == float
