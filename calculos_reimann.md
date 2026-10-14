# Cálculo e Investigación Matemática: Sumas de Riemann por Punto Medio

**Asignatura:** Cálculo Intermedio  
**Redactor:** Alejandro (Grupo 3) apoyado en la IA, para redaccion formal   
**Función:** f(x) = x^2  
**Intervalo:** [a, b] = [0, 2]  
**Método:** Suma de Riemann con Punto Medio (x_i*)

---

## 1. Fundamentación Teórica del Método del Punto Medio

Para aproximar el área bajo la curva f(x) = x^2 en el intervalo [0, 2], dividimos el dominio en n subintervalos de igual longitud:

Delta x = (b - a) / n = (2 - 0) / n = 2 / n

En el método del punto medio, la altura de cada rectángulo se evalúa en el centro de cada subintervalo [x_{i-1}, x_i]. Matemáticamente, el punto medio x_i* se define como el promedio entre los extremos del subintervalo:

x_i* = (x_{i-1} + x_i) / 2 = (i - 0.5) * Delta x

La suma de Riemann general para n particiones viene dada por:

S_n = Sumatoria desde i=1 hasta n de [ f(x_i*) * Delta x ] = Sumatoria desde i=1 hasta n de [ (x_i*)^2 * Delta x ]

---

## 2. Desarrollo de Cálculos Manuales (n = 4 y n = 8)

### 2.1 Caso n = 4
* **Ancho de subintervalo:** Delta x = 2 / 4 = 0.5
* **Subintervalos y Puntos Medios (x_i*):**
  * [0, 0.5] -> x_1* = 0.25
  * [0.5, 1.0] -> x_2* = 0.75
  * [1.0, 1.5] -> x_3* = 1.25
  * [1.5, 2.0] -> x_4* = 1.75
* **Alturas f(x_i*) = (x_i*)^2:**
  * f(x_1*) = 0.25^2 = 0.0625
  * f(x_2*) = 0.75^2 = 0.5625
  * f(x_3*) = 1.25^2 = 1.5625
  * f(x_4*) = 1.75^2 = 3.0625
* **Áreas de Rectángulos y Suma de Riemann:**
  * A_1 = 0.5 * 0.0625 = 0.03125
  * A_2 = 0.5 * 0.5625 = 0.28125
  * A_3 = 0.5 * 1.5625 = 0.78125
  * A_4 = 0.5 * 3.0625 = 1.53125

S_4 = 0.03125 + 0.28125 + 0.78125 + 1.53125 = 2.625

---

### 2.2 Caso n = 8
* **Ancho de subintervalo:** Delta x = 2 / 8 = 0.25
* **Puntos Medios (x_i*):**  
  x_1* = 0.125, x_2* = 0.375, x_3* = 0.625, x_4* = 0.875, x_5* = 1.125, x_6* = 1.375, x_7* = 1.625, x_8* = 1.875
* **Alturas f(x_i*):**  
  0.015625, 0.140625, 0.390625, 0.765625, 1.265625, 1.890625, 2.640625, 3.515625
* **Cálculo de la Suma:**
  * Suma de áreas izquierdas (A_1 a A_4): 0.328125
  * Suma de áreas derechas (A_5 a A_8): 2.328125

S_8 = 0.328125 + 2.328125 = 2.65625

---

## 3. Generalización mediante Sumatorias para Particiones Grandes

Cuando el número de subintervalos aumenta (n = 16 y n = 32), la evaluación individual resulta ineficiente. Se utiliza la notación de sumatoria desarrollando el binomio del punto medio:

S_n = (Delta x)^3 * [ Suma de i^2 - Suma de i + Suma de 0.25 ]

Utilizando las fórmulas conocidas:
* Suma de i^2 = [n(n+1)(2n+1)] / 6
* Suma de i = [n(n+1)] / 2
* Suma de constante = 0.25 * n

---

### 3.1 Caso n = 16
* Delta x = 0.125 -> (Delta x)^3 = 0.001953125
* Suma de i^2 = (16 * 17 * 33) / 6 = 1496
* Suma de i = (16 * 17) / 2 = 136
* Suma de constante = 16 * 0.25 = 4

S_16 = 0.001953125 * (1496 - 136 + 4) = 0.001953125 * 1364 = 2.6640625

---

### 3.2 Caso n = 32
* Delta x = 0.0625 -> (Delta x)^3 = 0.000244140625
* Suma de i^2 = (32 * 33 * 65) / 6 = 11440
* Suma de i = (32 * 33) / 2 = 528
* Suma de constante = 32 * 0.25 = 8

S_32 = 0.000244140625 * (11440 - 528 + 8) = 0.000244140625 * 10920 = 2.666015625

---

## 4. Tabla Resumen y Conclusión

| Cantidad de Subintervalos (n) | Ancho de Subintervalo (Delta x) | Valor de la Suma de Riemann (S_n) |
| :---: | :---: | :---: |
| 4 | 0.5000 | 2.625000000 |
| 8 | 0.2500 | 2.656250000 |
| 16 | 0.1250 | 2.664062500 |
| 32 | 0.0625 | 2.666015625 |

### Conclusión Matemática:
A medida que el número de rectángulos n aumenta, la aproximación por el punto medio se acerca de manera monótona al valor real del área bajo la curva. El valor exacto se obtiene mediante el límite cuando n tiende a infinito:

Área Exacta = Integral desde 0 hasta 2 de (x^2) dx = x^3 / 3 (evaluado entre 0 y 2) = 8 / 3 aprox. 2.666666...
