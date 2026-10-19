# Cálculo e Investigación Matemática: Sumas de Riemann por Punto Medio

**Asignatura:** Cálculo Intermedio

**Integrantes:** Alejandro (Grupo 3)

**Función:** $f(x) = 2x^2$

**Intervalo:** $[a, b] = [0, 2]$

**Método:** Suma de Riemann con Punto Medio ($x_i^*$)

---

## 1. Fundamentación Teórica del Método del Punto Medio

Para aproximar el área bajo la curva $f(x) = 2x^2$ en el intervalo $[0, 2]$, dividimos el dominio en $n$ subintervalos de igual longitud:

$$
\Delta x = \frac{b - a}{n} = \frac{2 - 0}{n} = \frac{2}{n}
$$

En el método del punto medio, la altura de cada rectángulo se evalúa en el centro de cada subintervalo $[x_{i-1}, x_i]$. Matemáticamente, el punto medio $x_i^*$ se define como el promedio entre los extremos del subintervalo:

$$
x_i^* = \frac{x_{i-1} + x_i}{2} = (i - 0.5) \cdot \Delta x = (i - 0.5) \cdot \frac{2}{n} = \frac{2i - 1}{n}
$$

La suma de Riemann general para $n$ particiones viene dada por:

$$
S_n = \sum_{i=1}^{n} f(x_i^*) \cdot \Delta x = \sum_{i=1}^{n} 2(x_i^*)^2 \cdot \Delta x
$$

---

## 2. Desarrollo de Cálculos Manuales ($n = 4$ y $n = 8$)

### 2.1 Caso $n = 4$

* **Ancho de subintervalo:** $\Delta x = \frac{2}{4} = 0.5$

* **Subintervalos y Puntos Medios ($x_i^*$):**
  * $[0, 0.5] \rightarrow x_1^* = 0.25$
  * $[0.5, 1.0] \rightarrow x_2^* = 0.75$
  * $[1.0, 1.5] \rightarrow x_3^* = 1.25$
  * $[1.5, 2.0] \rightarrow x_4^* = 1.75$

* **Alturas $f(x_i^*) = 2(x_i^*)^2$:**
  * $f(x_1^*) = 2 \cdot (0.25)^2 = 0.125$
  * $f(x_2^*) = 2 \cdot (0.75)^2 = 1.125$
  * $f(x_3^*) = 2 \cdot (1.25)^2 = 3.125$
  * $f(x_4^*) = 2 \cdot (1.75)^2 = 6.125$

* **Áreas de Rectángulos y Suma de Riemann:**
  * $A_1 = 0.5 \cdot 0.125 = 0.0625$
  * $A_2 = 0.5 \cdot 1.125 = 0.5625$
  * $A_3 = 0.5 \cdot 3.125 = 1.5625$
  * $A_4 = 0.5 \cdot 6.125 = 3.0625$

$$
S_4 = 0.0625 + 0.5625 + 1.5625 + 3.0625 = 5.2500
$$

### 2.2 Caso $n = 8$

* **Ancho de subintervalo:** $\Delta x = \frac{2}{8} = 0.25$

* **Planteamiento:** $S_8 = \sum_{i=1}^{8} \left[ 2 \cdot ((i - 0.5) \cdot 0.25)^2 \cdot 0.25 \right]$

* **Desarrollo de constantes y binomio:**
  * $S_8 = 0.03125 \cdot \left[ \sum_{i=1}^{8} i^2 - \sum_{i=1}^{8} i + \sum_{i=1}^{8} 0.25 \right]$
  * $\sum_{i=1}^{8} i^2 = \frac{8 \cdot 9 \cdot 17}{6} = 204$
  * $\sum_{i=1}^{8} i = \frac{8 \cdot 9}{2} = 36$
  * Suma de constante = $8 \cdot 0.25 = 2$
  * Paréntesis total = $204 - 36 + 2 = 170$

$$
S_8 = 0.03125 \cdot 170 = 5.3125
$$

---

## 3. Generalización mediante Sumatorias para Particiones Grandes

### 3.1 Caso $n = 16$

* **Ancho de subintervalo:** $\Delta x = \frac{2}{16} = 0.125 \rightarrow (\Delta x)^3 \cdot 2 = 0.00390625$

* **Aplicación de fórmulas:**
  * $\sum_{i=1}^{16} i^2 = \frac{16 \cdot 17 \cdot 33}{6} = 1496$
  * $\sum_{i=1}^{16} i = \frac{16 \cdot 17}{2} = 136$
  * Suma de constante = $16 \cdot 0.25 = 4$
  * Paréntesis total = $1496 - 136 + 4 = 1364$

$$
S_{16} = 0.00390625 \cdot 1364 = 5.328125
$$

### 3.2 Caso $n = 32$

* **Ancho de subintervalo:** $\Delta x = \frac{2}{32} = 0.0625 \rightarrow (\Delta x)^3 \cdot 2 = 0.00048828125$

* **Aplicación de fórmulas:**
  * $\sum_{i=1}^{32} i^2 = \frac{32 \cdot 33 \cdot 65}{6} = 11440$
  * $\sum_{i=1}^{32} i = \frac{32 \cdot 33}{2} = 528$
  * Suma de constante = $32 \cdot 0.25 = 8$
  * Paréntesis total = $11440 - 528 + 8 = 10920$

$$
S_{32} = 0.00048828125 \cdot 10920 = 5.33203125
$$

---

## 4. Demostración del Límite al Infinito ($n \to \infty$)

1. **Planteamiento formal de la sumatoria:**

$$
\lim_{n \to \infty} \sum_{i=1}^{n} 2 \left( \frac{2i - 1}{n} \right)^2 \cdot \frac{2}{n}
$$

2. **Desarrollo del binomio al cuadrado:**

$$
\lim_{n \to \infty} \sum_{i=1}^{n} 2 \left( \frac{4i^2 - 4i + 1}{n^2} \right) \cdot \frac{2}{n} = \lim_{n \to \infty} \sum_{i=1}^{n} \frac{16i^2 - 16i + 4}{n^3}
$$

3. **Distribución de sumatorias y constantes:**

$$
\lim_{n \to \infty} \frac{1}{n^3} \left( 16 \sum_{i=1}^{n} i^2 - 16 \sum_{i=1}^{n} i + \sum_{i=1}^{n} 4 \right)
$$

4. **Sustitución por fórmulas de sumatoria conocidas:**

$$
\lim_{n \to \infty} \frac{1}{n^3} \left( 16 \left[ \frac{n(n+1)(2n+1)}{6} \right] - 16 \left[ \frac{n(n+1)}{2} \right] + 4n \right)
$$

5. **Simplificación algebraica:**

$$
\lim_{n \to \infty} \frac{1}{n^3} \left( \frac{16}{3}n^3 - \frac{4}{3}n \right) = \lim_{n \to \infty} \left( \frac{16}{3} - \frac{4}{3n^2} \right)
$$

6. **Evaluación del límite:**

$$
\lim_{n \to \infty} \left( \frac{16}{3} - \frac{4}{3n^2} \right) = \frac{16}{3} \approx 5.333333...
$$

---

## 5. Tabla Resumen y Conclusión

| Cantidad de Subintervalos ($n$) | Ancho de Subintervalo ($\Delta x$) | Valor de la Suma de Riemann ($S_n$) |
| :---: | :---: | :---: |
| **4** | 0.5000 | 5.25000000 |
| **8** | 0.2500 | 5.31250000 |
| **16** | 0.1250 | 5.32812500 |
| **32** | 0.0625 | 5.33203125 |

### Conclusión Matemática:

A medida que el número de rectángulos $n$ aumenta, la aproximación por el punto medio se acerca de manera monótona al valor real del área bajo la curva. El valor exacto obtenido analíticamente mediante la integral definida coincide con el resultado del límite evaluado:

$$
\text{Área Exacta} = \int_{0}^{2} 2x^2 \, dx = \left[ \frac{2x^3}{3} \right]_{0}^{2} = \frac{16}{3} \approx 5.333333...
$$