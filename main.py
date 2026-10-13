
from manim import *


A = 0
B = 2
VALORES_N = [4, 8, 16, 32]
AREA_EXACTA = 8 / 3


def funcion(x):
    return x**2


def suma_riemann_derecha(n):
    dx = (B - A) / n
    return sum(funcion(A + i * dx) * dx for i in range(1, n + 1))


class SumasRiemann(Scene):
    def construct(self):
        titulo = Text(
            "Sumas de Riemann: extremos derechos",
            font_size=34
        ).to_edge(UP)

        ejes = Axes(
            x_range=[0, 2.2, 0.5],
            y_range=[0, 4.5, 1],
            x_length=7,
            y_length=4.5,
            axis_config={"include_numbers": True},
            tips=False
        ).shift(LEFT * 1.3 + DOWN * 0.4)

        curva = ejes.plot(
            funcion,
            x_range=[A, B],
            color=YELLOW
        )

        etiqueta = MathTex(
            "f(x)=x^2",
            color=YELLOW
        ).next_to(ejes, RIGHT).shift(UP * 1.5)

        self.play(Write(titulo))
        self.play(Create(ejes), run_time=1.5)
        self.play(Create(curva), Write(etiqueta))
        self.wait(1)

        rectangulos_anteriores = None
        informacion_anterior = None

        for n in VALORES_N:
            dx = (B - A) / n
            suma = suma_riemann_derecha(n)
            error = abs(suma - AREA_EXACTA)

            rectangulos = ejes.get_riemann_rectangles(
                curva,
                x_range=[A, B],
                dx=dx,
                input_sample_type="right",
                color=BLUE,
                fill_opacity=0.45,
                stroke_width=1
            )

            informacion = VGroup(
                MathTex(f"n={n}"),
                MathTex(
                    rf"\Delta x={dx:.4f}"
                ),
                MathTex(
                    rf"R_{{{n}}}={suma:.4f}"
                ),
                MathTex(
                    rf"\text{{Error}}={error:.4f}"
                )
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)

            informacion.scale(0.75)
            informacion.to_edge(RIGHT).shift(DOWN * 0.6)

            if rectangulos_anteriores is None:
                self.play(
                    FadeIn(rectangulos),
                    FadeIn(informacion),
                    run_time=1.5
                )
            else:
                self.play(
                    ReplacementTransform(
                        rectangulos_anteriores,
                        rectangulos
                    ),
                    ReplacementTransform(
                        informacion_anterior,
                        informacion
                    ),
                    run_time=2
                )

            self.wait(2)

            rectangulos_anteriores = rectangulos
            informacion_anterior = informacion

        conclusion = Text(
            "A mayor n, menor error de aproximacion",
            font_size=30,
            color=GREEN
        ).to_edge(DOWN)

        self.play(FadeIn(conclusion))
        self.wait(3)


class IntroduccionRiemann(Scene):
    def construct(self):
  
        titulo = Text(
            "De pocos rectangulos a una mejor aproximacion",
            font_size=34
        ).to_edge(UP)

        pregunta = Text(
            "Como aproximamos el area bajo una curva?",
            font_size=27
        ).next_to(titulo, DOWN, buff=0.5)

        ejes = Axes(
            x_range=[0, 2.5, 0.5],
            y_range=[0, 4.5, 1],
            x_length=6,
            y_length=3.5,
            axis_config={"include_numbers": True},
            tips=False
        ).shift(DOWN * 0.8)

        curva = ejes.plot(
            lambda x: x**2,
            x_range=[0, 2],
            color=YELLOW
        )

        etiqueta = MathTex(
            "f(x)=x^2",
            color=YELLOW
        ).next_to(ejes, RIGHT).shift(UP)

        area = ejes.get_area(
            curva,
            x_range=[0, 2],
            color=BLUE,
            opacity=0.4
        )

        intervalo = MathTex(
            r"x\in[0,2]"
        ).to_edge(DOWN)


        self.play(Write(titulo), run_time=2)
        self.play(FadeIn(pregunta), run_time=1.5)
        self.wait(1)

        self.play(Create(ejes), run_time=2)
        self.play(Create(curva), Write(etiqueta), run_time=2)
        self.play(FadeIn(area), run_time=2)
        self.play(Write(intervalo), run_time=1)

        self.wait(3)

class ConstruccionRectangulos(Scene):
    def construct(self):
        titulo = Text(
            "Construccion de rectangulos derechos",
            font_size=32
        ).to_edge(UP)

        ejes = Axes(
            x_range=[0, 2.5, 0.5],
            y_range=[0, 4.5, 1],
            x_length=6,
            y_length=4,
            axis_config={"include_numbers": True},
            tips=False
        ).shift(LEFT * 1.6 + DOWN * 0.5)

        curva = ejes.plot(
            lambda x: x**2,
            x_range=[0, 2],
            color=YELLOW
        )

        formula_dx = MathTex(
            r"\Delta x=\frac{2-0}{4}=0.5"
        ).scale(0.8).to_edge(RIGHT).shift(UP * 1.5)

        explicacion = Text(
            "Altura: extremo derecho",
            font_size=23
        ).next_to(formula_dx, DOWN, buff=0.5)

        self.play(Write(titulo))
        self.play(Create(ejes), Create(curva))
        self.play(Write(formula_dx), FadeIn(explicacion))

        rectangulos = VGroup()
        puntos = VGroup()

        dx = 0.5

        for i in range(1, 5):
            x_izq = (i - 1) * dx
            x_der = i * dx
            altura = x_der**2

            rectangulo = Polygon(
                ejes.c2p(x_izq, 0),
                ejes.c2p(x_der, 0),
                ejes.c2p(x_der, altura),
                ejes.c2p(x_izq, altura),
                color=BLUE,
                fill_color=BLUE,
                fill_opacity=0.35,
                stroke_width=2
            )

            # Punto de contacto con la curva
            punto = Dot(
                ejes.c2p(x_der, altura),
                color=RED,
                radius=0.07
            )

            rectangulos.add(rectangulo)
            puntos.add(punto)

            self.play(
                FadeIn(rectangulo),
                FadeIn(punto),
                run_time=1
            )
            self.wait(0.5)

        resultado = MathTex(
            r"R_4=3.75"
        ).scale(0.9).to_edge(RIGHT).shift(DOWN * 1.5)

        self.play(Write(resultado))
        self.wait(3)
