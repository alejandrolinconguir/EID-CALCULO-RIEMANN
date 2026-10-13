
from manim import *

# Configuración matemática
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
