from AutoDeportivo import AutoDeportivo
from Auto import Auto

if __name__ == '__main__':
    auto = AutoDeportivo('Ferrari', 'F40', 'Rojo', 320)
    
    auto.acelerar()
    auto.turbo()
    auto.frenar()
    
    auto.turbo()
    
    auto.arrancar()
    auto.acelerar()
    auto.acelerar()
    auto.frenar()
    auto.arrancar()
    auto.turbo()
    
    
    auto2 = Auto('Honda', 'CR-V', 'Negro')
    auto2.arrancar()
    