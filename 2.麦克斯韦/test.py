from manim import *


class ImageMobjectGrid(Scene):
    def construct(s):
        eqs=VGroup(MathTex(r'\nabla \cdot \mathbf{D} =\rho _f').set_color(BLUE),
                      MathTex(r'\nabla \cdot \mathbf{B} = 0').set_color(RED),
                      MathTex(r'\nabla \times  \mathbf{E} = -\cfrac{\partial \mathbf{B}}{\partial t }').set_color(YELLOW),
                      MathTex(r'\nabla \times  \mathbf{H} = \mathbf{J}_f +  \cfrac{\partial \mathbf{D}}{\partial t }').set_color(GREEN)
        ).arrange(DOWN, aligned_edge=LEFT)
        eqt=Text('Maxwell Equation').to_edge(DOWN,buff=0.25)
        e=MathTex(r'\varepsilon_0 ?').scale(2).shift(UP*2+RIGHT*3)
        m=ImageMobject('Maxwell').scale_to_fit_height(5).to_edge(LEFT,buff=0.5)
        c=ImageMobject('Coulomb').scale_to_fit_height(4).to_corner(DR)
        s.add(eqs,eqt,e,m,c)