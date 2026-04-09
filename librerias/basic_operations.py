import numpy as np
import cmath

def complex_sum(num_1: complex, num_2: complex) -> complex:
    '''Esta funcion realiza la suma de numeros complejos'''
    
    sum_result = num_1 + num_2
    return sum_result

def complex_sub(num_1: complex, num_2: complex) -> complex:
    '''Esta funcion realiza la resta de numeros complejos'''
    
    sub_result = num_1 - num_2
    return sub_result

def complex_mult(num_1: complex, num_2: complex) -> complex:
    '''Esta funcion realiza la multiplicacion de numeros complejos'''
    # -------------------------------------------------------------------------
    # Esta parte representa la parte matematica de operaciones de numeros
    # complejos, pero ya numpy maneja la multiplicacion de complejos.
    
    #real_part_1 = num_1.real
    #imag_part_1 = num_1.imag
    #real_part_2 = num_2.real
    #imag_part_2 = num_2.imag
    
    #real_result = (real_part_1 * real_part_2) - (imag_part_1 * imag_part_2)
    #imag_result = (real_part_1 * imag_part_2) + (real_part_2 * imag_part_1)
    #mult_result = real_result + imag_result * 1j
    # -------------------------------------------------------------------------
    
    mult_result = num_1 * num_2
    return mult_result

def complex_div(num_1: complex, num_2: complex) -> complex:
    '''Esta funcion realiza la division de numeros complejos'''
    
    # -------------------------------------------------------------------------
    # Esta parte representa la parte matematica de operaciones de numeros
    # complejos, pero ya numpy maneja la division de complejos.
    
    #numerador = num_1 * complex_conj(num_2)
    #denominador = num_2 * complex_conj(num_2)
    
    #div_result = numerador / denominador
    # -------------------------------------------------------------------------
    
    div_result = num_1 / num_2
    return div_result

def complex_conj(num_1: complex) -> complex:
    '''Esta funcion realiza el conjuhado de un numero complejo'''
    
    conj_result = np.conj(num_1)
    return conj_result

def rect_to_polar(num_1: complex) -> tuple[float, float]:
    '''Esta funcion hace la conversion de coordenadas rectangulares
    a coordenadas polares'''
    
    return cmath.polar(num_1)

def polar_to_rect(magnitud: float, fase: float) -> complex:
    '''Esta funcion hace la conversion de coordenadas polares a 
    coordenadas rectangulares'''
    
    return cmath.rect(magnitud, fase)
    

if __name__ == "__main__":
    
    # ===== Prueba de suma ===== 
    complex_1 = 1 + 2j
    complex_2 = 2 - 3j
    suma = complex_sum(complex_1, complex_2)
    print("SUMA: ")
    print(f"{suma} \n")
    
    # ===== Prueba de resta ===== 
    complex_3 = 1 + 2j
    complex_4 = 2 - 3j
    resta = complex_sub(complex_3, complex_4)
    print("RESTA: ")
    print(f"{resta} \n")
    
    # ===== Prueba de multiplicacion ===== 
    complex_5 = 3 - 1j
    complex_6 = 1 + 4j
    multiplicacion = complex_mult(complex_5, complex_6)
    print("MULTIPLICACION: ")
    print(f"{multiplicacion} \n")
    
    # ===== Prueba de division ===== 
    complex_7 = 7 - 3j
    complex_8 = 0 + 2j
    division = complex_div(complex_7, complex_8)
    print("DIVISION: ")
    print(f"{division} \n")
    
    # ===== Prueba de conjugado ===== 
    complex_9 = 3 + 2j
    conjugado = complex_conj(complex_9)
    print("CONJUGADO: ")
    print(f"{conjugado} \n")
    
    # ===== Prueba de conversion rectangular a polar ===== 
    complex_10 = -1 - 1j
    magnitud, fase = rect_to_polar(complex_10)
    print("RECTANGULAR A POLAR: ")
    print(f"Magnitud: {magnitud: .2f}")
    print(f"Fase: {fase: .2f} \n")
    
    # ===== Prueba de conversion polar a rectangular ===== 
    magnitud = 10
    fase = (2*(cmath.pi)) / 3
    complejo = polar_to_rect(magnitud, fase)
    print("POLAR A RECTANGULAR: ")
    print(f"Numero complejo: {complejo: .2f} \n")   