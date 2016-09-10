class Veiculo(object):

    def __init__(self):
        self.porta = 0
        self.roda = 2


class VeiculoMotorizado(Veiculo):

    def __init__(self):
        Veiculo.__init__(self)
        self.ligado = False

    def ligar_motor(self):
        self.ligado = True


if __name__ == '__main__':
    bicicleta = Veiculo()
    print('Bicicleta')
    print('Porta:', bicicleta.porta)
    print('Roda:', bicicleta.roda)

    triciclo = Veiculo()
    print('Triciclo')
    triciclo.roda = 3
    print('Porta:', triciclo.porta)
    print('Roda:', triciclo.roda)

    moto = VeiculoMotorizado()
    print('Moto')
    print('Porta:', moto.porta)
    print('Roda:', moto.roda)
    print('Motor:', moto.ligado)

    moto.ligar_motor()
    print('Motor:', moto.ligado)

    carro = VeiculoMotorizado()
    carro.porta = 4
    carro.roda = 4
    carro.ligar_motor()
    print('Carro')
    print('Porta:', carro.porta)
    print('Roda:', carro.roda)
    print('Motor:', carro.ligado)
