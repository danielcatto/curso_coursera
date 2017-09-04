
from exercicio.formulaBhaskara import delta


def test_delta():
    assert delta(10, 30, 25) < 0

def test_delta():
    assert delta(10, 30, 25) >0

def test_delta():
    assert delta(16, 4, 9) < 0
