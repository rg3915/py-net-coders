class Veiculo(object):

    def __init__(self, porta=0, roda=2):
        super(Veiculo, self).__init__()
        self.porta = porta
        self.roda = roda


class VeiculoMotorizado(Veiculo):

    def __init__(self, porta=0, roda=2, ligado=False):
        super(VeiculoMotorizado, self).__init__(porta, roda)
        Veiculo.__init__(self)
        self.ligado = ligado

    def ligar_motor(self):
        self.ligado = True


if __name__ == '__main__':
    bicicleta = Veiculo()
    print('Bicicleta:')
    print('Porta:', bicicleta.porta)
    print('Roda:', bicicleta.roda)

    triciclo = Veiculo()
    print('Triciclo:')
    triciclo.roda = 3
    print('Porta:', triciclo.porta)
    print('Roda:', triciclo.roda)

    moto = VeiculoMotorizado()
    print('Moto:')
    print('Porta:', moto.porta)
    print('Roda:', moto.roda)
    print('Motor:', moto.ligado)

    moto.ligar_motor()
    print('Motor:', moto.ligado)

    carro = VeiculoMotorizado()
    carro.porta = 4
    carro.roda = 4
    carro.ligar_motor()
    print('Carro:')
    print('Porta:', carro.porta)
    print('Roda:', carro.roda)
    print('Motor:', carro.ligado)
