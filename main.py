from carro_inteligente import CarroInteligente
from carro_esportivo import CarroEsportivo
from carro_corrida import CarroCorrida

def teste_drive (carro):
    print(f'\nTestando {carro.__class__.__name__}: ')
    carro.acelera()
    carro.exibe_velocidade()

if __name__ == '__main__':
    # Testando CarroInteligente
    carro_inteligente = CarroInteligente (10)
    print ('Carro Inteligente: ')
    carro_inteligente.acelera()
    carro_inteligente.exibe_velocidade()
    carro_inteligente.estacionar()
    

    #Testando carro esportivo
    carro_esportivo = CarroEsportivo (50)
    print('Carro esportivo: ')
    carro_esportivo.turbo()
    carro_esportivo.exibe_velocidade()
    carro_esportivo.freia()
    carro_esportivo.exibe_velocidade()

    carro_corrida = CarroCorrida(100)
    teste_drive(carro_corrida)

