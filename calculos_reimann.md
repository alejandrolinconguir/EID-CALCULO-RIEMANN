# Cálculo e Investigación Matemática: Sumas de Riemann por Punto Medio

**Asignatura:** Cálculo Intermedio  
**Integrantes:** Alejandro (Grupo 3)  
**Función:** f(x) = 2x^2  
**Intervalo:** [a, b] = [0, 2]  
**Método:** Suma de Riemann con Punto Medio (x_i*)

---

## 1. Fundamentación Teórica del Método del Punto Medio

Para aproximar el área bajo la curva f(x) = 2x^2 en el intervalo [0, 2], dividimos el dominio en n subintervalos de igual longitud:

Delta x = (b - a) / n = (2 - 0) / n = 2 / n

En el método del punto medio, la altura de cada rectángulo se evalúa en el centro de cada subintervalo [x_{i-1}, x_i]. Matemáticamente, el punto medio x_i* se define como el promedio entre los extremos del subintervalo:

x_i* = (x_{i-1} + x_i) / 2 = (i - 0.5) * Delta x

La suma de Riemann general para n particiones viene dada por:

S_n = Sumatoria desde i=1 hasta n de [ f(x_i*) * Delta x ] = Sumatoria desde i=1 hasta n de [ 2(x_i*)^2 * Delta x ]

---

## 2. Desarrollo de Cálculos Manuales (n = 4 y n = 8)

### 2.1 Caso n = 4
* **Ancho de subintervalo:** Delta x = 2 / 4 = 0.5
* **Subintervalos y Puntos Medios (x_i*):**
  * [0, 0.5] -> x_1* = 0.25
  * [0.5, 1.0] -> x_2* = 0.75
  * [1.0, 1.5] -> x_3* = 1.25
  * [1.5, 2.0] -> x_4* = 1.75
* **Alturas f(x_i*) = 2(x_i*)^2:**
  * f(x_1*) = 2 * (0.25)^2 = 0.125
  * f(x_2*) = 2 * (0.75)^2 = 1.125
  * f(x_3*) = 2 * (1.25)^2 = 3.125
  * f(x_4*) = 2 * (1.75)^2 = 6.125
* **Áreas de Rectángulos y Suma de Riemann:**
  * A_1 = 0.5 * 0.125 = 0.0625
  * A_2 = 0.5 * 1.125 = 0.5625
  * A_3 = 0.5 * 3.125 = 1.5625
  * A_4 = 0.5 * 6.125 = 3.0625

S_4 = 0.0625 + 0.5625 + 1.5625 + 3.0625 = 5.2500

---

### 2.2 Caso n = 8
* **Ancho de subintervalo:** Delta x = 2 / 8 = 0.25
* **Planteamiento:** S_8 = Sumatoria desde i=1 hasta 8 de [ 2 * ((i - 0.5) * 0.25)^2 * 0.25 ]
* **Desarrollo de constantes y binomio:**
  * S_8 = 0.03125 * [ Suma de i^2 - Suma de i + Suma de 0.25 ]
  * Suma de i^2 = (8 * 9 * 17) / 6 = 204
  * Suma de i = (8 * 9) / 2 = 36
  * Suma de constante = 8 * 0.25 = 2
  * Paréntesis = 204 - 36 + 2 = 170

S_8 = 0.03125 * 170 = 5.3125

---

## 3. Generalización mediante Sumatorias para Particiones Grandes

### 3.1 Caso n = 16
* **Ancho de subintervalo:** Delta x = 2 / 16 = 0.125 -> (Delta x)^3 * 2 = 0.00390625
* **Aplicación de fórmulas:**
  * Suma de i^2 = (16 * 17 * 33) / 6 = 1496
  * Suma de i = (16 * 17) / 2 = 136
  * Suma de constante = 16 * 0.25 = 4
  * Paréntesis = 1496 - 136 + 4 = 1364

S_16 = 0.00390625 * 1364 = 5.328125

---

### 3.2 Caso n = 32
* **Ancho de subintervalo:** Delta x = 2 / 32 = 0.0625 -> (Delta x)^3 * 2 = 0.00048828125
* **Aplicación de fórmulas:**
  * Suma de i^2 = (32 * 33 * 65) / 6 = 11440
  * Suma de i = (32 * 33) / 2 = 528
  * Suma de constante = 32 * 0.25 = 8
  * Paréntesis = 11440 - 528 + 8 = 10920

S_32 = 0.00048828125 * 10920 = 5.33203125

---

## 4. Tabla Resumen y Conclusión

| Cantidad de Subintervalos (n) | Ancho de Subintervalo (Delta x) | Valor de la Suma de Riemann (S_n) |
| :---: | :---: | :---: |
| 4 | 0.5000 | 5.25000000 |
| 8 | 0.2500 | 5.31250000 |
| 16 | 0.1250 | 5.32812500 |
| 32 | 0.0625 | 5.33203125 |

### Conclusión Matemática:
A medida que el número de rectángulos n aumenta, la aproximación por el punto medio se acerca de manera monótona al valor real del área bajo la curva. El valor exacto se obtiene mediante el límite cuando n tiende a infinito:

Área Exacta = Integral desde 0 hasta 2 de (2x^2) dx = [ 2x^3 / 3 ] evaluado entre 0 y 2 = 16 / 3 aprox. 5.333333...
