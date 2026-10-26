
from app.estacionamento.checkout import emitir_ticket_saida


def test_carro_tres_horas_com_mercado():
    ticket = emitir_ticket_saida(
        "ABC1234", 3, "carro", "MERCADO"
    )

    assert ticket["valido"] is True
    assert ticket["tarifa_base"] == 22.0
    assert ticket["desconto_convenio"] == 4.4
    assert ticket["valor_a_pagar"] == 17.6


def test_moto_duas_horas_com_farmacia():
    ticket = emitir_ticket_saida(
        "XYZ5678", 2, "moto", "FARMACIA"
    )

    assert ticket["valido"] is True
    assert ticket["tarifa_base"] == 8.0
    assert ticket["desconto_convenio"] == 0.8
    assert ticket["valor_a_pagar"] == 7.2


def test_veiculo_nao_suportado():
    ticket = emitir_ticket_saida(
        "ABC1234", 2, "caminhao", "MERCADO"
    )

    assert ticket["valido"] is False
    assert ticket["motivo"] == "tipo de veiculo nao suportado"
    assert ticket["valor_a_pagar"] == 0.0


def test_horas_zeradas():
    ticket = emitir_ticket_saida(
        "ABC1234", 0, "carro", "MERCADO"
    )

    assert ticket["valido"] is False
    assert ticket["motivo"] == "dados invalidos para checkout"
    assert ticket["valor_a_pagar"] == 0.0
