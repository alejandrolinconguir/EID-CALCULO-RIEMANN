from manim import *

# Parámetros globales del problema: f(x) = 2x^2 en el intervalo [0, 2]
A = 0
B = 2
AREA_EXACTA = 16 / 3


def funcion(x):
    return 2 * x**2


# --- PARTE 1: Título y Bienvenida ---
class Escena01_IntroBienvenida(Scene):
    def construct(self):
        titulo = Text(
            "El Calculo Integral y las Sumas de Riemann",
            font_size=34
        ).to_edge(UP)

        sub = Text(
            "Visualizando la construccion del area exacta",
            font_size=24,
            color=BLUE
        ).next_to(titulo, DOWN, buff=0.4)

        pregunta = Text(
            "¿Como podemos medir el area bajo una curva?",
            font_size=28,
            color=YELLOW
        ).shift(DOWN * 0.5)

        self.play(Write(titulo), run_time=2)
        self.wait(1)
        self.play(FadeIn(sub), run_time=1.5)
        self.wait(1.5)
        self.play(FadeIn(pregunta), run_time=2)
        self.wait(3.5)


# --- PARTE 2: Figuras Regulares vs Curvas ---
class Escena02_FigurasVsCurvas(Scene):
    def construct(self):
        titulo = Text(
            "Geometria Elemental vs. Formas Curvas",
            font_size=32
        ).to_edge(UP)

        rectangulo = Rectangle(width=3, height=2, color=GREEN).shift(LEFT * 3 + DOWN * 0.5)
        txt_rect = Text("Area = base x altura", font_size=20).next_to(rectangulo, DOWN)

        ejes = Axes(
            x_range=[0, 2.5, 0.5],
            y_range=[0, 10, 2],
            x_length=4,
            y_length=3,
            axis_config={"include_numbers": True, "label_constructor": Text},
            tips=False
        ).shift(RIGHT * 3 + DOWN * 0.5)

        curva = ejes.plot(funcion, x_range=[A, B], color=YELLOW)
        area = ejes.get_area(curva, x_range=[A, B], color=YELLOW, opacity=0.3)
        txt_curva = Text("¿Formula directa?", font_size=20, color=RED).next_to(ejes, DOWN)

        self.play(Write(titulo), run_time=1.5)
        self.play(Create(rectangulo), Write(txt_rect), run_time=2)
        self.wait(1)
        self.play(Create(ejes), Create(curva), FadeIn(area), Write(txt_curva), run_time=2.5)
        self.wait(3.5)


# --- PARTE 3: Planteamiento de la Función ---
class Escena03_PlanteamientoFuncion(Scene):
    def construct(self):
        titulo = Text(
            "Problema Modelo: f(x) = 2x^2",
            font_size=32
        ).to_edge(UP)

        ejes = Axes(
            x_range=[0, 2.5, 0.5],
            y_range=[0, 10, 2],
            x_length=6,
            y_length=4,
            axis_config={"include_numbers": True, "label_constructor": Text},
            tips=False
        ).shift(DOWN * 0.5)

        curva = ejes.plot(funcion, x_range=[A, B], color=YELLOW)
        etiqueta = Text("f(x) = 2x^2", color=YELLOW, font_size=26).next_to(ejes, RIGHT).shift(UP * 1.5)
        intervalo = Text("Intervalo: x en [0, 2]", font_size=24, color=BLUE).to_edge(DOWN)

        self.play(Write(titulo), run_time=1.5)
        self.play(Create(ejes), run_time=2)
        self.play(Create(curva), Write(etiqueta), run_time=2)
        self.wait(1)
        self.play(Write(intervalo), run_time=1.5)
        self.wait(3.5)


# --- PARTE 4: La Estrategia de Bernhard Riemann ---
class Escena04_EstrategiaRiemann(Scene):
    def construct(self):
        titulo = Text(
            "La Idea de Bernhard Riemann",
            font_size=32
        ).to_edge(UP)

        idea1 = Text(
            "1. Dividir el intervalo en subintervalos iguales.",
            font_size=26
        ).shift(UP * 1)

        idea2 = Text(
            "2. Construir rectangulos sobre cada subintervalo.",
            font_size=26,
            color=BLUE
        ).next_to(idea1, DOWN, buff=0.5)

        idea3 = Text(
            "3. Sumar las areas simples de todos los rectangulos.",
            font_size=26,
            color=GREEN
        ).next_to(idea2, DOWN, buff=0.5)

        self.play(Write(titulo), run_time=1.5)
        self.wait(1)
        self.play(FadeIn(idea1), run_time=1.5)
        self.wait(1)
        self.play(FadeIn(idea2), run_time=1.5)
        self.wait(1)
        self.play(FadeIn(idea3), run_time=1.5)
        self.wait(4)


class Escena05_ExplicacionPuntoMedio(Scene):
    def construct(self):
        titulo = Text(
            "Criterio de Altura: Punto Medio",
            font_size=30
        ).to_edge(UP)

        ejes = Axes(
            x_range=[0, 2.5, 0.5],
            y_range=[0, 10, 2],
            x_length=6,
            y_length=4,
            axis_config={"include_numbers": True, "label_constructor": Text},
            tips=False
        ).shift(LEFT * 1.4 + DOWN * 0.5)

        curva = ejes.plot(funcion, x_range=[A, B], color=YELLOW)

        # Ejemplo en un solo subintervalo [0, 0.5] con i = 1
        rect = ejes.get_riemann_rectangles(curva, x_range=[0, 0.5], dx=0.5, input_sample_type="center", color=BLUE, fill_opacity=0.45)
        dot = Dot(ejes.c2p(0.25, funcion(0.25)), color=RED, radius=0.08)

        info = VGroup(
            Text("Para cada rectangulo i:", font_size=22, color=YELLOW),
            Text("x_i = a + (i - 0.5) * Dx", font_size=22, color=GREEN),
            Text("i = 1 -> x_1 = 0 + (0.5) * 0.5 = 0.25", font_size=20, color=RED),
            Text("Restamos 0.5 para ir al centro exacto", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).to_edge(RIGHT).shift(DOWN * 0.5)

        self.play(Write(titulo), Create(ejes), Create(curva), run_time=2)
        self.wait(1)
        self.play(FadeIn(rect), FadeIn(dot), Write(info), run_time=2.5)
        self.wait(3.5)


# --- PARTE 6: Primera Aproximación Burda (n = 2) ---
class Escena06_AproximacionN2(Scene):
    def construct(self):
        titulo = Text(
            "Aproximacion Burda: n = 2 rectangulos",
            font_size=30
        ).to_edge(UP)

        ejes = Axes(
            x_range=[0, 2.5, 0.5],
            y_range=[0, 10, 2],
            x_length=6,
            y_length=4,
            axis_config={"include_numbers": True, "label_constructor": Text},
            tips=False
        ).shift(LEFT * 1.4 + DOWN * 0.5)

        curva = ejes.plot(funcion, x_range=[A, B], color=YELLOW)

        n = 2
        dx = (B - A) / n
        suma = sum(funcion(A + (i - 0.5) * dx) * dx for i in range(1, n + 1))
        rects = ejes.get_riemann_rectangles(curva, x_range=[A, B], dx=dx, input_sample_type="center", color=RED, fill_opacity=0.4)

        info = VGroup(
            Text(f"n = {n}   (Dx = {dx:.2f})", font_size=24),
            Text("x_i = 0 + (i - 0.5) * 1.0", font_size=22, color=YELLOW),
            Text(f"S_2 = {suma:.2f}", font_size=24),
            Text("Error visual grande", font_size=22, color=RED)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).to_edge(RIGHT).shift(DOWN * 0.5)

        self.play(Write(titulo), Create(ejes), Create(curva), run_time=2)
        self.wait(1)
        self.play(FadeIn(rects), Write(info), run_time=2)
        self.wait(3.5)


# --- PARTE 7: Refinando a n = 4 ---
class Escena07_AproximacionN4(Scene):
    def construct(self):
        titulo = Text(
            "Mejorando la estimacion: n = 4",
            font_size=30
        ).to_edge(UP)

        ejes = Axes(
            x_range=[0, 2.5, 0.5],
            y_range=[0, 10, 2],
            x_length=6,
            y_length=4,
            axis_config={"include_numbers": True, "label_constructor": Text},
            tips=False
        ).shift(LEFT * 1.4 + DOWN * 0.5)

        curva = ejes.plot(funcion, x_range=[A, B], color=YELLOW)

        n = 4
        dx = (B - A) / n
        suma = sum(funcion(A + (i - 0.5) * dx) * dx for i in range(1, n + 1))
        rects = ejes.get_riemann_rectangles(curva, x_range=[A, B], dx=dx, input_sample_type="center", color=BLUE, fill_opacity=0.45)

        info = VGroup(
            Text(f"n = {n}   (Dx = {dx:.2f})", font_size=24),
            Text("x_i = (i - 0.5) * 0.5", font_size=22, color=YELLOW),
            Text(f"S_4 = {suma:.4f}", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).to_edge(RIGHT).shift(DOWN * 0.5)

        self.play(Write(titulo), Create(ejes), Create(curva), run_time=2)
        self.wait(1)
        self.play(FadeIn(rects), Write(info), run_time=2)
        self.wait(3.5)


# --- PARTE 8: Transición Suave a n = 8 ---
class Escena08_TransicionN8(Scene):
    def construct(self):
        titulo = Text(
            "Duplicando la precision: n = 8",
            font_size=30
        ).to_edge(UP)

        ejes = Axes(
            x_range=[0, 2.5, 0.5],
            y_range=[0, 10, 2],
            x_length=6,
            y_length=4,
            axis_config={"include_numbers": True, "label_constructor": Text},
            tips=False
        ).shift(LEFT * 1.4 + DOWN * 0.5)

        curva = ejes.plot(funcion, x_range=[A, B], color=YELLOW)

        dx1 = (B - A) / 4
        rects1 = ejes.get_riemann_rectangles(curva, x_range=[A, B], dx=dx1, input_sample_type="center", color=BLUE, fill_opacity=0.45)

        dx2 = (B - A) / 8
        suma2 = sum(funcion(A + (i - 0.5) * dx2) * dx2 for i in range(1, 9))
        rects2 = ejes.get_riemann_rectangles(curva, x_range=[A, B], dx=dx2, input_sample_type="center", color=BLUE, fill_opacity=0.45)

        info2 = VGroup(
            Text("n = 8   (Dx = 0.25)", font_size=24),
            Text("x_i = (i - 0.5) * 0.25", font_size=22, color=YELLOW),
            Text(f"S_8 = {suma2:.4f}", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).to_edge(RIGHT).shift(DOWN * 0.5)

        self.play(Write(titulo), Create(ejes), Create(curva), FadeIn(rects1), run_time=2)
        self.wait(1)
        self.play(ReplacementTransform(rects1, rects2), Write(info2), run_time=2.5)
        self.wait(3.5)


# --- PARTE 9: Comportamiento y Error Numérico ---
class Escena09_AnalisisError(Scene):
    def construct(self):
        titulo = Text("Analisis del Error de Aproximacion", font_size=30).to_edge(UP)

        valores = [4, 8, 16, 32]
        lineas = [Text("Area Exacta = 16 / 3 aprox 5.3333", font_size=24, color=YELLOW)]

        for n in valores:
            dx = (B - A) / n
            suma = sum(funcion(A + (i - 0.5) * dx) * dx for i in range(1, n + 1))
            error = abs(suma - AREA_EXACTA)
            lineas.append(Text(f"n = {n} -> S_{n} = {suma:.4f}  |  Error = {error:.4f}", font_size=20))

        grupo = VGroup(*lineas).arrange(DOWN, aligned_edge=LEFT, buff=0.35).shift(UP * 0.3)

        self.play(Write(titulo), run_time=1.5)
        self.wait(1)
        for linea in grupo:
            self.play(FadeIn(linea), run_time=1)
            self.wait(0.8)
        self.wait(3.5)


# --- PARTE 10: Tendencia de Ancho Infinitesimal ---
class Escena10_AnchoInfinitesimal(Scene):
    def construct(self):
        titulo = Text("¿Que ocurre cuando Dx tiende a Cero?", font_size=30).to_edge(UP)

        p1 = Text("1. El numero de rectangulos (n) crece hacia el infinito.", font_size=24).shift(UP * 1)
        p2 = Text("2. El ancho Dx = (b - a) / n se vuelve infinitesimal.", font_size=24, color=BLUE).next_to(p1, DOWN, buff=0.5)
        p3 = Text("3. Los huecos o excesos de area desaparecen por completo.", font_size=24, color=GREEN).next_to(p2, DOWN, buff=0.5)

        self.play(Write(titulo), run_time=2)
        self.wait(1)
        self.play(FadeIn(p1), run_time=1.5)
        self.wait(1)
        self.play(FadeIn(p2), run_time=1.5)
        self.wait(1)
        self.play(FadeIn(p3), run_time=1.5)
        self.wait(4)


# --- PARTE 11: Definición Formal del Límite ---
class Escena11_LimiteFormal(Scene):
    def construct(self):
        titulo = Text("El Paso al Limite de Riemann", font_size=32).to_edge(UP)

        sumatoria = Text("Suma: Suma( f(a + (i - 0.5)*Dx) * Dx )", font_size=24).shift(UP * 1)
        limite = Text("lim (n -> inf) Suma( f(x_i) * Dx )", font_size=30, color=BLUE).next_to(sumatoria, DOWN, buff=0.6)
        resultado = Text("= 16 / 3", font_size=34, color=GREEN).next_to(limite, DOWN, buff=0.6)

        self.play(Write(titulo), run_time=2)
        self.wait(1)
        self.play(Write(sumatoria), run_time=2)
        self.wait(1.5)
        self.play(Write(limite), run_time=2)
        self.wait(1.5)
        self.play(Write(resultado), run_time=2)
        self.wait(3.5)


# --- PARTE 12: Cierre e Integral Definida ---
class Escena12_CierreIntegral(Scene):
    def construct(self):
        titulo = Text("El Nacimiento de la Integral Definida", font_size=32).to_edge(UP)

        formula = Text("Integral de 0 a 2 de (2x^2) dx = 16 / 3", font_size=32, color=GREEN).shift(UP * 0.5)
        conclusion = Text("Las Sumas de Riemann son el puente\nentre lo discreto y lo continuo.", font_size=26, color=YELLOW).next_to(formula, DOWN, buff=0.8)

        self.play(Write(titulo), run_time=2)
        self.wait(1)
        self.play(Write(formula), run_time=2.5)
        self.wait(1.5)
        self.play(FadeIn(conclusion), run_time=2)
        self.wait(4)