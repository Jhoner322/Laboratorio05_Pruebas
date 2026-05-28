class PagoService:

    def calcular_total(self, monto):
        impuesto = monto * 0.18
        return monto + impuesto

    def validar_pago(self, monto):
        if monto < 10:
            return False
        return True