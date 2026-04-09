# 🚀 COMPUTACIÓN CUÁNTICA (CNYT)

> [!IMPORTANT]
> Para que el programa principal funcione se deben usar las librerías `numpy` y `cmath`.
> 
> La única librería que hay que instalar es `numpy` para esta hay que escribir la siguiente línea en la terminal de su dispositivo:
> 
> ```
> pip install numpy
> ```

## Operaciones de números complejos
### Suma
$$
C_1 + C_2 = (a+c) + (b+d)i
$$
### Resta
$$
C_1 - C_2 = (a-c) + (b-d)i
$$
### Multiplicación
$$
C_1 \cdot C_2 = (ac-bd) + (ad+cb)i
$$
### División
$$
\frac{C_1}{C_2} = \frac{(a+bi)(c-di)}{(c+di)(c-di)}
$$
### Conjugado
$$
\overline{C_1} = a-bi
$$
### Magnitud
$$
\|C_2\| = \sqrt{c^2 + b^2}
$$
### Conversión coordenadas rectangulares a polares
$$
\rho = \sqrt{a^2 + b^2}
$$

$$
\theta = \tan \left(\frac{b}{a} \right)
$$
### Conversión coordenadas polares a rectangulares
$$
a = \rho\cos(\theta)
$$

$$
b = \rho\sin(\theta)
$$

## Operaciones de vectores y matrices
### Vectores
Dados los vectores $A$ y $B$ y el número complejo $C$, las operaciones que se pueden realizar con vectores son:
$$A = \begin{bmatrix} a + bi \\ c + di \end{bmatrix} \quad y \quad B = \begin{bmatrix} e + fi \\ g + hi \end{bmatrix}$$

#### Suma de vectores
$$A+B = \begin{bmatrix} (a+e) + (b+f)i \\ (c+g) + (d+h)i \end{bmatrix}$$

#### Resta de vectores
$$A-B = \begin{bmatrix} (a-e) + (b-f)i \\ (c-g) + (d-h)i \end{bmatrix}$$

#### Multiplicación de escalar por vector
$$C \cdot A = \begin{bmatrix} C(a+bi) \\ C(c+di) \end{bmatrix}$$
#### Inverso de un vector
$$-A = \begin{bmatrix} -(a + bi) \\ -(c + di) \end{bmatrix}$$

#### Transpuesta de un vector
$$A^T = \begin{bmatrix} a + bi & c + di \end{bmatrix}$$

#### Conjugado de un vector
$$\overline{A} = \begin{bmatrix} a-bi \\ c-di \end{bmatrix}$$

#### Adjunto de un vector
$$A^{\dagger} = \begin{bmatrix} a - bi & c - di \end{bmatrix}$$

#### Producto interno entre vectores
$$
\langle A|B\rangle = A^{\dagger} \cdot B
$$

#### Magnitud de un vector
$$
\|A\| = \sqrt{\langle A|A \rangle}
$$

### Matrices
Dadas las matrices $A$ y $B$ y el número complejo $C$, las operaciones que se pueden realizar con matrices son:
$$A = \begin{bmatrix} a + bi & c + di \\ e + fi & g + hi \end{bmatrix} \quad y \quad B = \begin{bmatrix} j + ki & l + mi \\ n + oi & p + qi \end{bmatrix}$$

#### Suma de matrices
$$A+B = \begin{bmatrix} (a+j) + (b+k)i & (c+l) + (d+m)i \\ (e+n) + (f+o)i & (g+p) + (h+q)i \end{bmatrix}$$

#### Resta de matrices
$$A-B = \begin{bmatrix} (a-j) + (b-k)i & (c-l) + (d-m)i \\ (e-n) + (f-o)i & (g-p) + (h-q)i \end{bmatrix}$$

#### Multiplicación de escalar por matriz
$$C \cdot A = \begin{bmatrix} C(a+bi) & C(c+di) \\ C(e+fi) & C(g+hi) \end{bmatrix}$$

#### Inverso de una matriz
$$-A = \begin{bmatrix} -(a + bi) & -(c + di) \\ -(e + fi) & -(g + hi) \end{bmatrix}$$

#### Transpuesta de una matriz
$$A^T = \begin{bmatrix} a + bi & e + fi \\ c + di & g + hi \end{bmatrix}$$

#### Conjugado de una matriz
$$\overline{A} = \begin{bmatrix} a-bi & c-di \\ e-fi & g-hi \end{bmatrix}$$

#### Adjunta de una matriz
$$A^{\dagger} = \begin{bmatrix} a - bi & e - fi \\ c - di & g - hi \end{bmatrix}$$

#### Multiplicación de matrices
$$A \cdot B = \begin{bmatrix} (a + bi)(j + ki) + (c + di)(n + oi) & (a + bi)(l + mi) + (c + di)(p + qi) \\ (e + fi)(j + ki) + (g + hi)(n + oi) & (e + fi)(l + mi) + (g + hi)(p + qi) \end{bmatrix}$$

#### Producto interno de matrices
$$
\langle A|B\rangle = \text{tr}(A^{\dagger} \cdot B)
$$