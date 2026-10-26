
from app.estacionamento.convenio import calcular_desconto_convenio


def test_desconto_mercado():
    assert calcular_desconto_convenio(50.0, "MERCADO") == 10.0


def test_desconto_farmacia():
    assert calcular_desconto_convenio(40.0, "FARMACIA") == 4.0


def test_loja_nao_parceira():
    assert calcular_desconto_convenio(50.0, "PADARIA") == 0.0


def test_codigo_vazio():
    assert calcular_desconto_convenio(50.0, "") == 0.0


def test_valor_bruto_menor_ou_igual_a_zero():
    assert calcular_desconto_convenio(0.0, "MERCADO") == 0.0
    assert calcular_desconto_convenio(-10.0, "FARMACIA") == 0.0
