import numpy as np
import cmath

# ===== VECTORES =====
def vector_sum(vec_1, vec_2):
    sum_result = vec_1 + vec_2
    return sum_result

def vector_sub(vec_1, vec_2):
    sub_result = vec_1 - vec_2
    return sub_result

def escalar_x_vector(num, vec):
    mult_result = num * vec
    return mult_result

def vector_inv(vec_1):
    inv_result = -vec_1
    return inv_result

def vector_transpose(vec_1):
    trans_result = vec_1.T
    return trans_result

def vector_conj(vec_1):
    conj_result = np.conjugate(vec_1)
    return conj_result

def vector_adj(vec_1):
    adj_result = vec_1.T.conj()
    return adj_result

def vector_mag(vec):
    prod_int = prod_int_vec(vec, vec)
    mag_result = np.sqrt(prod_int)
    return mag_result

# ===== MATRICES =====
def matriz_sum(mtz_1, mtz_2):
    sum_result = mtz_1 + mtz_2
    return sum_result

def matriz_sub(mtz_1, mtz_2):
    sub_result = mtz_1 - mtz_2
    return sub_result

def matriz_mult(mtz_1, mtz_2):
    mult_result = np.dot(mtz_1, mtz_2)
    return mult_result

def escalar_x_matriz(num, mtz):
    mult_result = num * mtz
    return mult_result

def matriz_inv(mtz_1):
    inv_result = -mtz_1
    return inv_result

def matriz_transpose(mtz_1):
    trans_result = mtz_1.T
    return trans_result

def matriz_conj(mtz_1):
    conj_result = np.conjugate(mtz_1)
    return conj_result

def matriz_adj(mtz_1):
    adj_result = mtz_1.T.conj()
    return adj_result

def matriz_x_vector(mtz, vec):
    '''La funcion multiplica una matriz por un vector.
    Para computacion cuantica representa la accion de una
    compuerta sobre un estado.'''
    
    m_x_v_result = np.dot(mtz, vec)
    return m_x_v_result

def matriz_dimension(mtz):
    dimension = mtz.shape
    return dimension

# ===== PRODUCTO INTERNO VEC/MAT =====

def prod_int_vec(vec_1, vec_2):
    prod_int_result = np.vdot(vec_1, vec_2)
    return prod_int_result

def prod_int_mtz(mtz_1, mtz_2):
    mtz_1 = matriz_adj(mtz_1)
    prod_int_result = np.trace(matriz_mult(mtz_1, mtz_2))
    return prod_int_result

# ===== PRODUCTO TENSOR =====

def prod_tensor_vec(vec_1, vec_2):
    '''Esta funcion realiza el producto tensor entre dos vectores.
    En computacion cuantica, el producto tensor combina dos estados
    cuanticos en un espacio de Hilbert mayor.'''
    
    prod_tensor_result = np.kron(vec_1, vec_2)
    return prod_tensor_result

def prod_tensor_mtz(mtz_1, mtz_2):
    '''Esta funcion realiza el producto tensor entre dos matrices.
    En computacion cuantica, el producto tensor se utiliza para
    combinar multiples compuertas cuanticas.'''
    
    prod_tensor_result = np.kron(mtz_1, mtz_2)
    return prod_tensor_result


if __name__ == "__main__":
    
    # vectores columna de prueba
    v1 = np.array([[2+3j], 
                   [5-4j], 
                   [1+1j]])
    v2 = np.array([[1-1j], 
                   [3+2j], 
                   [4-4j]])
    v3 = np.array([[2+3j],
                   [1+1j]])
    phi = np.array([[5-1j],
                    [2j],
                    [3-1j],
                    [1+1j]])
    
    # matrices de prueba
    m1 = np.array([[1+1j, 2],
                   [3, 4-1j]])
    m2 = np.array([[5, 6+1j],
                   [7-1j, 8]])
    
    # numero escalar  
    escalar = 2-3j
    
    # ===== VECTORES =====
    suma = vector_sum(v1, v2)
    print("SUMA VECTORES")
    print(f"{suma} \n")
    
    resta = vector_sub(v1, v2)
    print("RESTA VECTORES")
    print(f"{resta} \n")
    
    mult_escalar = escalar_x_vector(escalar, v1)
    print("ESCALAR POR VECTOR")
    print(f"{mult_escalar} \n")
    
    inverso = vector_inv(v1)
    print("INVERSO DE VECTOR")
    print(f"{inverso} \n")
    
    traspuesta = vector_transpose(v1)
    print("TRASPUESTA DE VECTOR")
    print(f"{traspuesta} \n")
    
    conjugado = vector_conj(v1)
    print("CONJUGADO DE VECTOR")
    print(f"{conjugado} \n")
    
    adjunta = vector_adj(v1)
    print("ADJUNTA DE VECTOR")
    print(f"{adjunta} \n")
    
    prod_int = prod_int_vec(v1, v2)
    print("PROD INTERNO VECTORES")
    print(f"{prod_int} \n")
    
    magnitud = vector_mag(phi)
    print("MAGNITUD VECTOR")
    print(f"{magnitud} \n")

    # ===== MATRICES =====
    suma = matriz_sum(m1, m2)
    print("SUMA MATRICES")
    print(f"{suma} \n")
    
    resta = matriz_sub(m1, m2)
    print("RESTA MATRICES")
    print(f"{resta} \n")
    
    multiplicacion = matriz_mult(m1, m2)
    print("MULTIPLICACION MATRICES")
    print(f"{multiplicacion} \n")
    
    mult_escalar = escalar_x_matriz(escalar, m1)
    print("ESCALAR POR MATRIZ")
    print(f"{mult_escalar} \n")
    
    inverso = matriz_inv(m1)
    print("INVERSO DE MATRIZ")
    print(f"{inverso} \n")
    
    traspuesta = matriz_transpose(m1)
    print("TRASPUESTA DE MATRIZ")
    print(f"{traspuesta} \n")
    
    conjugado = matriz_conj(m1)
    print("CONJUGADO DE MATRIZ")
    print(f"{conjugado} \n")
    
    adjunta = matriz_adj(m1)
    print("ADJUNTA DE MATRIZ")
    print(f"{adjunta} \n")
    
    accion_mv = matriz_x_vector(m1, v3)
    print("MATRIZ POR VECTOR")
    print(f"{accion_mv} \n")
    
    dimension = matriz_dimension(m1)
    print("DIMENSION MATRIZ")
    print(f"{dimension} \n")
    
    prod_int = prod_int_mtz(m1, m2)
    print("PROD INTERNO MATRICES")
    print(f"{prod_int} \n")
    
    # ===== PRODUCTO TENSOR =====
    prod_tensor_v = prod_tensor_vec(v3, v3)
    print("PRODUCTO TENSOR VECTORES")
    print(f"{prod_tensor_v} \n")
    
    prod_tensor_m = prod_tensor_mtz(m1, m2)
    print("PRODUCTO TENSOR MATRICES")
    print(f"{prod_tensor_m} \n")


    # ================== Q14 ==================
    estado_phi = np.array([[1/np.sqrt(2)],
                           [1j/np.sqrt(2)]])
    
    observable = np.array([[0, -1j],
                           [1j, 0]])
    
    norma_estado = vector_mag(estado_phi)
    print(norma_estado)

    # ================== Q9 ==================
    dinamica_sistema = np.array([[0,0,0,1,0,0],
                                 [0,1,0,0,0,0],
                                 [0,0,0,0,0,1],
                                 [0,0,0,0,1,0],
                                 [0,0,1,0,0,0],
                                 [1,0,0,0,0,0]])
    
    est_inicial = np.array([[4],
                            [1],
                            [5],
                            [3],
                            [10],
                            [2]])
    
    for i in range(4):
        est_inicial = matriz_mult(dinamica_sistema, est_inicial)

        print(f"{est_inicial} \n")

    # ================== Q12 ==================
    estado_0 = np.array([[1],
                         [0]])
    
    operador_x = np.array([[0, 1],
                           [1, 0]])
    
    # VECTOR NORMALIZADO
    norma_estado_0 = vector_mag(estado_0)
    estado_0 = escalar_x_vector(norma_estado_0, estado_0)
    print(f"{estado_0} \n")

    # VALOR ESPERADO
    parte_1 = matriz_mult(operador_x, estado_0)
    adjunta_estado_0 = vector_adj(estado_0)
    val_esperado = matriz_mult(adjunta_estado_0, parte_1)
    print(f"{val_esperado} \n")

    # ============ Q5 ==========
    M = np.array([[2/15, 7/15, 6/15],
                  [9/15, 5/15, 1/15],
                  [4/15, 3/15, 8/15]])
    
    estado_t = np.array([[0],
                         [0],
                         [1]])
    
    cl1 = matriz_mult(M, estado_t)
    print(f"{cl1} \n")
    suma = 0
    p1 = cl1[1][0]
    p2 = cl1[2][0]

    suma_prob = p1 + p2
    print(suma_prob)