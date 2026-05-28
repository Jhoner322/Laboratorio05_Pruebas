from pagos import PagoService

def test_calculo_total():

    servicio = PagoService()

    resultado = servicio.calcular_total(100)

    assert resultado == 118


def test_pago_minimo():

    servicio = PagoService()

    resultado = servicio.validar_pago(5)

    assert resultado is False