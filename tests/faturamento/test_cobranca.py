import pytest

from app.faturamento.cobranca import processar_cobranca


@pytest.mark.parametrize(
    "valor_base, plano, dias_atraso, esperado",
    [
        (0, "BASICO", 0, -1.0),
        (-100, "BASICO", 0, -1.0),
        (100, "BASICO", -1, -1.0),

        (100, "INVALIDO", 0, -2.0),
        (100, "", 0, -2.0),

        (100, "BASICO", 0, 100.0),
        (100, "PREMIUM", 0, 90.0),
        (100, "EMPRESARIAL", 0, 80.0),

        (100, "basico", 0, 100.0),
        (100, "premium", 0, 90.0),
        (100, " EMPRESARIAL ", 0, 80.0),

        (100, "BASICO", 1, 105.50),
        (100, "BASICO", 30, 120.00),

        (100, "BASICO", 31, 156.00),
    ],
)
def test_processar_cobranca(
    valor_base, plano, dias_atraso, esperado
):
    resultado = processar_cobranca(
        valor_base,
        plano,
        dias_atraso
    ) 

    assert resultado == esperado


import time
from app.faturamento.cobranca import processar_cobranca

def test_desempenho_processar_cobranca():
    inicio = time.perf_counter()

    resultado = processar_cobranca(100,"PREMIUM",10)

    fim = time.perf_counter()

    tempo_decorrido = fim - inicio

    assert resultado == 99.50
    assert tempo_decorrido < 0.1  

    