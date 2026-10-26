
from app.estacionamento.tarifas import calcular_tarifa_base


def test_moto_uma_hora():
    assert calcular_tarifa_base(1, "moto") == 5.0


def test_moto_tres_horas():
    assert calcular_tarifa_base(3, "moto") == 11.0


def test_carro_uma_hora():
    assert calcular_tarifa_base(1, "carro") == 10.0


def test_carro_quatro_horas():
    assert calcular_tarifa_base(4, "carro") == 28.0


def test_tipo_veiculo_invalido():
    assert calcular_tarifa_base(2, "caminhao") == -1.0


def test_horas_menor_ou_igual_a_zero():
    assert calcular_tarifa_base(0, "carro") == 0.0
    assert calcular_tarifa_base(-1, "moto") == 0.0
