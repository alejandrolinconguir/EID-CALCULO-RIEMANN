
from manim import *



A = 0
B = 4
VALORES_N = [4, 8, 16, 32]
AREA_EXACTA = 128 / 3


def funcion(x):
    return 2 * x**2


def suma_riemann_derecha(n):
    dx = (B - A) / n
    return sum(
        funcion(A + i * dx) * dx
        for i in range(1, n + 1)
    )



class SumasRiemann(Scene):
    def construct(self):
        titulo = Text(
            "Sumas de Riemann: extremos derechos",
            font_size=32
        ).to_edge(UP)

        ejes = Axes(
            x_range=[0, 4.5, 1],
            y_range=[0, 36, 8],
            x_length=6,
            y_length=4,
            axis_config={"include_numbers": True},
            tips=False
        ).shift(LEFT * 1.6 + DOWN * 0.5)

        curva = ejes.plot(
            funcion,
            x_range=[A, B],
            color=YELLOW
        )

        etiqueta = MathTex(
            "f(x)=2x^2",
            color=YELLOW
        ).scale(0.8).to_edge(RIGHT).shift(UP * 1.8)

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
                MathTex(rf"n={n}"),
                MathTex(rf"\Delta x={dx:.4f}"),
                MathTex(rf"R_{{{n}}}={suma:.4f}"),
                MathTex(rf"\text{{Error}}={error:.4f}")
            ).arrange(
                DOWN,
                aligned_edge=LEFT,
                buff=0.35
            )

            informacion.scale(0.7)
            informacion.to_edge(RIGHT).shift(DOWN * 0.5)

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
            font_size=27,
            color=GREEN
        ).to_edge(DOWN)

        self.play(FadeIn(conclusion))
        self.wait(3)



class IntroduccionRiemann(Scene):
    def construct(self):
        titulo = Text(
            "De pocos rectangulos a una mejor aproximacion",
            font_size=32
        ).to_edge(UP)

        pregunta = Text(
            "Como aproximamos el area bajo una curva?",
            font_size=26
        ).next_to(titulo, DOWN, buff=0.4)

        ejes = Axes(
            x_range=[0, 4.5, 1],
            y_range=[0, 36, 8],
            x_length=6,
            y_length=3.5,
            axis_config={"include_numbers": True},
            tips=False
        ).shift(DOWN * 0.8)

        curva = ejes.plot(
            funcion,
            x_range=[A, B],
            color=YELLOW
        )

        etiqueta = MathTex(
            r"f(x)=2x^2",
            color=YELLOW
        ).scale(0.8).next_to(ejes, RIGHT).shift(UP)

        area = ejes.get_area(
            curva,
            x_range=[A, B],
            color=BLUE,
            opacity=0.4
        )

        intervalo = MathTex(
            r"x\in[0,4]"
        ).to_edge(DOWN)

        self.play(Write(titulo), run_time=2)
        self.play(FadeIn(pregunta), run_time=1.5)
        self.wait(1)

        self.play(Create(ejes), run_time=2)
        self.play(
            Create(curva),
            Write(etiqueta),
            run_time=2
        )
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
            x_range=[0, 4.5, 1],
            y_range=[0, 36, 8],
            x_length=6,
            y_length=4,
            axis_config={"include_numbers": True},
            tips=False
        ).shift(LEFT * 1.4 + DOWN * 0.5)

        curva = ejes.plot(
            funcion,
            x_range=[A, B],
            color=YELLOW
        )

        etiqueta = MathTex(
            r"f(x)=2x^2",
            color=YELLOW
        ).scale(0.75).to_edge(RIGHT).shift(UP * 1.7)

        formula_dx = MathTex(
            r"\Delta x=\frac{4-0}{4}=1"
        ).scale(0.75).to_edge(RIGHT).shift(UP * 0.7)

        self.play(Write(titulo))
        self.play(Create(ejes), Create(curva), run_time=2)
        self.play(Write(etiqueta), Write(formula_dx))
        self.wait(1)

        # Construccion progresiva de los 4 rectangulos
        for i in range(4):
            izquierda = A + i
            derecha = izquierda + 1

            rectangulo = ejes.get_riemann_rectangles(
                curva,
                x_range=[izquierda, derecha],
                dx=1,
                input_sample_type="right",
                color=BLUE,
                fill_opacity=0.45,
                stroke_width=2
            )

            punto = Dot(
                ejes.c2p(derecha, funcion(derecha)),
                color=RED,
                radius=0.06
            )

            self.play(
                FadeIn(rectangulo),
                FadeIn(punto),
                run_time=1
            )
            self.wait(0.5)

        resultado = MathTex(
            r"R_4=2+8+18+32=60"
        ).scale(0.75).to_edge(RIGHT).shift(DOWN * 0.8)

        self.play(Write(resultado), run_time=2)
        self.wait(3)


class ComparacionAreaExacta(Scene):
    def construct(self):
        titulo = Text(
            "Comparacion con el area exacta",
            font_size=32
        ).to_edge(UP)

        ejes = Axes(
            x_range=[0, 4.5, 1],
            y_range=[0, 36, 8],
            x_length=6,
            y_length=4,
            axis_config={"include_numbers": True},
            tips=False
        ).shift(LEFT * 1.6 + DOWN * 0.5)

        curva = ejes.plot(
            funcion,
            x_range=[A, B],
            color=YELLOW
        )

        area = ejes.get_area(
            curva,
            x_range=[A, B],
            color=GREEN,
            opacity=0.35
        )

        formula = MathTex(
            r"A=\int_0^4 2x^2\,dx",
            r"=\frac{128}{3}"
        ).scale(0.7).to_edge(RIGHT).shift(UP * 1.5)

        area_decimal = MathTex(
            r"A\approx42.6667"
        ).scale(0.75).next_to(formula, DOWN, buff=0.3)

        self.play(Write(titulo))
        self.play(Create(ejes), Create(curva), run_time=2)
        self.play(FadeIn(area), Write(formula))
        self.play(Write(area_decimal))
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
                fill_opacity=0.5,
                stroke_width=1
            )

            informacion = VGroup(
                MathTex(rf"n={n}"),
                MathTex(rf"R_{{{n}}}={suma:.4f}"),
                MathTex(rf"\text{{Error}}={error:.4f}")
            ).arrange(
                DOWN,
                aligned_edge=LEFT,
                buff=0.3
            )

            informacion.scale(0.7)
            informacion.to_edge(RIGHT).shift(DOWN * 0.7)

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
            "La aproximacion se acerca al area exacta",
            font_size=27,
            color=GREEN
        ).to_edge(DOWN)

        self.play(FadeIn(conclusion))
        self.wait(3)


class ConclusionRiemann(Scene):
    def construct(self):
        titulo = Text(
            "Conclusion: hacia el area exacta",
            font_size=34
        ).to_edge(UP)

        formula_dx = MathTex(
            r"\Delta x=\frac{4}{n}"
        ).scale(1.2).shift(UP * 1.5)

        explicacion = Text(
            "Al aumentar n, disminuye el ancho",
            font_size=29
        ).next_to(formula_dx, DOWN, buff=0.6)

        limite = MathTex(
            r"\lim_{n\to\infty}R_n",
            r"=",
            r"\int_0^4 2x^2\,dx",
            r"=",
            r"\frac{128}{3}"
        ).scale(0.9).shift(DOWN * 0.7)

        resultado = Text(
            "Mas rectangulos, menor error",
            font_size=32,
            color=GREEN
        ).to_edge(DOWN)

        self.play(Write(titulo), run_time=2)
        self.play(Write(formula_dx), run_time=2)
        self.play(FadeIn(explicacion), run_time=2)
        self.wait(1)

        self.play(Write(limite), run_time=3)
        self.wait(2)

        self.play(FadeIn(resultado), run_time=2)
        self.wait(3)

