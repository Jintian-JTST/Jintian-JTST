from manim import *
import math
import numpy as np

OMEGA = np.array([math.sqrt(3)/2, -1/2, 0])
class SnowRing(VGroup):
    def __init__(self, radius):

        super().__init__()
        for i in range(radius):
            snowhexi = SnowHex(radius, i)
            self.add(snowhexi)

class SnowHex(VGroup):
    def __init__(self, x_position, omega_position):

        super().__init__()
        x = x_position
        omega = omega_position
        for i in range(6):
            snowi = Snow(x, omega)
            self.add(snowi)
            (x, omega) = (x-omega, x)

class Snow(RegularPolygon):
    def __init__(self, x_position, omega_position):

        super().__init__(n = 6, stroke_width = 2)
        self.scale(0.5)
        self.shift( x_position*UP + omega_position*OMEGA)

class SnowFlake(VGroup):
    def __init__(self):

        super().__init__()
        snowhex1 = SnowHex(2, 1)
        snowhex2 = SnowHex(6,2)
        snowhex3 = SnowHex(6,3)
        snowhex4 = SnowHex(6,4)
        snowring2 = VGroup(snowhex1)
        snowring3 = SnowRing(3)
        snowring4 = SnowRing(4)
        snowring5 = SnowRing(5)
        snowring6 = VGroup(snowhex2, snowhex3, snowhex4)

        self.add(snowring2, snowring3, snowring4, snowring5, snowring6)
        self.scale(0.25)
class Start(Scene):
    def construct(self):
        quote0 = Text("I stand on the shoulders of Maxwell.").shift(UP)
        author0 = Text("—Albert Einstein", color = BLUE, font = "Times New Roman")
        author0.next_to(quote0.get_corner(DOWN + RIGHT), DOWN*3 + LEFT)
        self.play(Write(quote0), runtime = 3)
        self.play(Write(author0))
        self.wait(2)
        self.play(FadeOut(quote0,author0))
        self.wait()

class BG(Scene):
    def construct(self):
        # 创建雪花的主体
        snowflake = SnowFlake()
        # 播放动画
        self.play(Create(snowflake))
        self.wait()
        self.play(FadeOut(snowflake))

        male_smile = Text('😊', color=BLUE).shift(UP*0.5).scale(1.4)
        # 身体
        male_body = VGroup(
            Circle(radius=0.5, color=BLUE).shift(UP*0.5),
            Line(UP*0, DOWN*1.25),
            Line(DOWN*1.25, DOWN*2.5+LEFT*0.5),
            Line(DOWN*1.25, DOWN*2.5+RIGHT*0.5),
            Line(DOWN*0.5, DOWN*1.3+LEFT*0.6),
            Line(DOWN*0.5, DOWN*1.3+RIGHT*0.6),
        )

        # 女性小人
        female = VGroup(
            Circle(radius=0.5, color=RED),
            Text('😀', color=RED).scale(1.4),
            Line(DOWN*0.5, DOWN*1.5),
            Line(DOWN*1.5, DOWN*2.5+LEFT*0.5),
            Line(DOWN*1.5, DOWN*2.5+RIGHT*0.5),
            Line(DOWN*1, DOWN*1.3+LEFT*0.6),
            Line(DOWN*1, DOWN*1.3+RIGHT*0.6),
        )

        # 调整女性小人的位置和辫子
        female.shift(RIGHT*2)

        # 播放动画
        self.play(Create(male_body),Create(male_smile))
        self.wait(0.5)  # 等待一段时间
        self.play(Create(female))  # 显示女性小人
        self.wait()
        fsquare=Square(color="#FF0000",fill_opacity=1).rotate(np.pi/4).shift(UP*2+LEFT*3)
        fu=Text('福',font="STZhongsong").rotate(np.pi).scale(2).shift(UP*2+LEFT*3)
        self.play(DrawBorderThenFill(fsquare))
        self.play(Write(fu))
        self.wait()

        stu =[ VGroup(
            Circle(radius=0.5, color=RED_B).shift(UP*0.5),
            Text('🤔', color=RED_B).shift(UP*0.5).scale(1.4),
            Line(UP*0, DOWN*1.25),
            Line(DOWN*1.25, DOWN*2.5+LEFT*0.5),
            Line(DOWN*1.25, DOWN*2.5+RIGHT*0.5),
            Line(DOWN*0.5, DOWN*1.3+LEFT*0.6),
            Line(DOWN*0.5, DOWN*1.3+RIGHT*0.6),
        ).shift(LEFT*3),
        VGroup(
            Circle(radius=0.5, color=RED_B).shift(UP*0.5),
            Text('🤔', color=RED_B).shift(UP*0.5).scale(1.4),
            Line(UP*0, DOWN*1.25),
            Line(DOWN*1.25, DOWN*2.5+LEFT*0.5),
            Line(DOWN*1.25, DOWN*2.5+RIGHT*0.5),
            Line(DOWN*0.5, DOWN*1.3+LEFT*0.6),
            Line(DOWN*0.5, DOWN*1.3+RIGHT*0.6),
        ).shift(LEFT*3)]
        male_angry=Text('🤬', color=BLUE).shift(UP*0.5+RIGHT*3).scale(1.4)
        self.play(ReplacementTransform(fu,stu[0]),ReplacementTransform(fsquare,stu[1]),FadeOut(female),male_body.animate.shift(RIGHT*3),male_smile.animate.shift(RIGHT*3))
        self.wait()
        self.play(Transform(male_smile,male_angry))
        goaway=Text('gun n.枪').shift(UP+RIGHT)
        self.add(goaway)
        self.wait()
        self.play(stu[0].animate.shift(LEFT*10),stu[1].animate.shift(LEFT*10),FadeOut(goaway))
        self.wait()
        male_think=Text('🤔', color=BLUE).shift(UP*0.5+RIGHT*3).scale(1.4)
        self.play(Transform(male_smile,male_think))
        book=Text('📖').shift(LEFT).scale(2)
        no=Text('❌',color=RED).shift(LEFT).scale(2)
        self.wait()
        self.play(Write(book))
        self.play(FadeIn(no))
        self.wait(2)
        self.play(FadeOut(book,no,male_smile,male_body))
        self.wait()

class Twond(Scene):
    def construct(self):
        # Show image
        pic = ImageMobject('st.JPG').scale(2)
        self.play(FadeIn(pic))
        self.wait(2)
        self.play(pic.animate.shift(LEFT * 2).scale(0.5))

        # Show epsilon
        epsilon = MathTex(r"\varepsilon_0").shift(RIGHT * 2).scale(2)
        epsilon_text = Text('epsilon').next_to(epsilon).scale(0.75)

        # Show Coulomb's Law
        coulombs_law_expr = MathTex(r'\mathbf{F} = \frac{1}{4\pi\varepsilon_0} \frac{Qq}{r^2}').shift(LEFT * 3)
        coulombs_law_text = Text("Coulomb's Law").scale(0.5).next_to(coulombs_law_expr, UP)

        # Show Gauss's Law
        gauss_law_expr = MathTex(r'\nabla \cdot \mathbf{E} = \frac{\rho}{\varepsilon_0}')
        gauss_law_text = Text("Gauss's Law").scale(0.5).next_to(gauss_law_expr, DOWN)

        # Animations
        self.play(Write(epsilon))
        self.wait()
        self.play(Transform(epsilon, epsilon_text))
        self.wait()
        self.play(FadeOut(pic), 
                  Write(coulombs_law_expr.shift(UP * 2)),
                  Write(coulombs_law_text))

        self.play(Write(gauss_law_expr.shift(LEFT * 3+DOWN * 2)),
                  Write(gauss_law_text.shift(DOWN * 2 + LEFT * 3)))
        self.wait()

        self.play(
            FadeOut(gauss_law_text, gauss_law_expr, coulombs_law_text, epsilon),
            coulombs_law_expr.animate.shift(RIGHT * 3 + DOWN * 2).scale(2)
        )
        
        l=MathTex(r'4\pi').scale(2).shift(DOWN*0.7+LEFT*0.15)
        self.play(Circumscribe(l))

        gr_law_expr=MathTex(r'\mathbf{F} = G \frac{m_1 m_2}{r^2}').scale(2).shift(UP * 2)
        self.play(TransformFromCopy( coulombs_law_expr , gr_law_expr), coulombs_law_expr.animate.shift(DOWN*2))
        self.wait(2)
        self.play(FadeOut(gr_law_expr,coulombs_law_expr))
        self.play(Flash(Square(),line_length=5,num_lines=20,color=YELLOW,run_time=1))
        self.wait()

class Gauss(ThreeDScene):
    def construct(self):
        def parametric_func(u, v):
            x = u * np.cos(v) * np.exp(-0.1 * u)
            y = u * np.sin(v) * np.exp(-0.1 * u)
            z = 0.3 * u * np.sin(3*v) * np.exp(-0.1 * u)
            return np.array([x, y, z])   

        def parametric_surface1(u, v):
            return np.array([
                (2 + np.sin(3 * u)) * np.cos(v),
                (2 + np.sin(3 * u)) * np.sin(v),
                np.cos(3 * u) + np.sin(v)
            ])


        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.5)
        n = [
            Surface(
                    func=lambda u, v: [
                        1.3 * np.sin(u) * np.cos(v),
                        0.2 * np.sin(u) * np.sin(v),
                        2 * np.cos(u)
                    ],
                    u_range=(0, PI),
                    v_range=(0, 2 * PI),color=GREEN
                )
,
Surface(
            parametric_func,
            u_range=[0, PI],
            v_range=[0, 2 * PI],
            checkerboard_colors=[RED_D, RED_E],
            resolution=(15, 32)
        )
,
            Surface(parametric_surface1, u_range=(0, 2*PI), v_range=(0, 2*PI),fill_color=ORANGE)
,

            Surface(
            func=lambda u, v : [
                2 * np.sin(u) * np.cos(v),
                2 * np.sin(u) * np.sin(v),
                2 * np.cos(u)
            ],
            u_range=(0, PI),
            v_range=(0, 2 * PI)
        )
        ]

        def s(n):
            self.add(n[0])
            self.wait(2)
            for m in range(1, len(n)):
                self.play(Transform(n[0], n[m]))

        s(n)

class Franklin(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.15)
        torus=Cylinder(radius=3,height=4,show_ends=False).set_color(GREY)
        self.play(FadeIn(torus))
        self.wait(2)
        plus=Tex('+').scale(1.5).shift(UP*2+LEFT*4)
        self.add_fixed_in_frame_mobjects(plus)
        self.play(torus.animate.set_color(RED),Write(plus))
        self.wait()
        #self.stop_ambient_camera_rotation()
        self.play(FadeOut(plus))

        inner=Cylinder(radius=3,height=0.1,show_ends=False).set_color(YELLOW)
        q=MathTex('Q=0.0').scale(0.7).shift(DOWN*3).to_edge(RIGHT+DOWN)
        self.add_fixed_in_frame_mobjects(q)
        self.play(Create(inner),Write(q))
        self.play(inner.animate.shift([0,0,1.3]))
        self.play(inner.animate.shift([0,0,-3]))
        self.play(Indicate(q))

        detect=Dot3D(color=BLUE)
        self.move_camera(phi=20*DEGREES)
        self.play(Create(detect),Uncreate(inner))
        coor=[[0,1.542,1.123],[1.2,-1.2,2.43241],[0.454,1.35,-1.3251]]
        for i in range(len(coor)):
            self.play(detect.animate.shift(coor[i]))
        self.play(Indicate(q))
        self.play(FadeOut(q,detect,torus))

def generate_random_points(num_points):
    random_points = VGroup()
    for _ in range(num_points):
        radius = np.random.uniform(0, 2)
        polar_angle = np.random.uniform(0, PI)
        azimuthal_angle = np.random.uniform(0, 2 * PI)

        x = radius * np.sin(polar_angle) * np.cos(azimuthal_angle)
        y = radius * np.sin(polar_angle) * np.sin(azimuthal_angle)
        z = radius * np.cos(polar_angle)

        random_points.add(Dot3D(point=np.array([x, y, z]),color=random_color()))

    return random_points

class Gauss(ThreeDScene):
    def construct(self):
        def parametric_func(u, v):
            x = u * np.cos(v) * np.exp(-0.1 * u)
            y = u * np.sin(v) * np.exp(-0.1 * u)
            z = 0.3 * u * np.sin(3*v) * np.exp(-0.1 * u)
            return np.array([x, y, z])   

        def parametric_surface1(u, v):
            return np.array([
                (2 + np.sin(3 * u)) * np.cos(v),
                (2 + np.sin(3 * u)) * np.sin(v),
                np.cos(3 * u) + np.sin(v)
            ])

        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.5)
        n = [
            Surface(
                func=lambda u, v: [
                    1.3 * np.sin(u) * np.cos(v),
                    0.2 * np.sin(u) * np.sin(v),
                    2 * np.cos(u)
                ],
                u_range=(0, PI),
                v_range=(0, 2 * PI), color=GREEN
            ),
            Surface(
                parametric_func,
                u_range=[0, PI],
                v_range=[0, 2 * PI],
                checkerboard_colors=[RED_D, RED_E],
                resolution=(15, 32)
            ),
            Surface(parametric_surface1, u_range=(0, 2*PI), v_range=(0, 2*PI), fill_color=ORANGE),
            Surface(
                func=lambda u, v: [
                    2 * np.sin(u) * np.cos(v),
                    2 * np.sin(u) * np.sin(v),
                    2 * np.cos(u)
                ],
                u_range=(0, PI),
                v_range=(0, 2 * PI)
            )
        ]

        def s(n):
            self.add(n[0])
            self.wait(2)
            for m in range(1, len(n)):
                self.play(Transform(n[0], n[m]))

        s(n)
        self.wait()


        n.append(Surface(
            func=lambda u, v: [
                2 * np.sin(u) * np.cos(v),
                2 * np.sin(u) * np.sin(v),
                2 * np.cos(u)
            ],
            u_range=(0, PI),
            v_range=(0, 2 * PI),
            color=BLUE,
            fill_opacity=0.2
        ))
        points = generate_random_points(10)

        self.add(points) 
        self.play(ReplacementTransform(n[0], n[-1]))
        self.wait()
        self.wait(0.2)

class Solenoid(Scene):
    def construct(self):
        # 定义螺线的参数方程
        def parametric_function(t):
            x = 1.25 * np.sin(6 * PI * t)
            y = t
            return np.array([x, y, 0])

        # 创建 ParametricFunction 对象
        magnet = VGroup(
            Rectangle(color=RED, height=1, width=0.5, fill_opacity=1).shift(UP * 0.5),
            Rectangle(color=BLUE, height=1, width=0.5, fill_opacity=1).shift(DOWN * 0.5),
            MathTex('N').scale_to_fit_height(0.2).shift(UP * 0.9),
            MathTex('S').scale_to_fit_height(0.2).shift(UP * -0.9),
        ).shift(UP*2)
        solenoid_coil = ParametricFunction(parametric_function, t_range=[-3.25, -1.75], color=BLUE)
        y=100
        # 创建十个电子
        electrons = [Dot().scale(0.25).move_to(solenoid_coil.get_start()) for _ in range(y)]

        # 将电子放在一起
        electrons_group = VGroup(*electrons)

        # 显示螺线圈和电子
        self.play(FadeIn(solenoid_coil, electrons_group, magnet))

        # 同时移动十个电子，每个电子在等待时间上都是匀速的
        anim_electrons = [MoveAlongPath(electron, solenoid_coil, rate_func=linear) for electron in electrons]

        anim = []
        for i in range(y):
            anim.append(Succession(Wait(0.01 * i), anim_electrons[i], Wait(0.01 * (y-i))))

        self.play(*anim, magnet.animate.shift(DOWN*2.5) ,run_time=7.5)

        self.wait(2)



class Org(Scene):
    def construct(s):
        def TIME(time):
            n=len(time)-1
            timen=Text(str(time[n]))
            s.play(Write(timen.scale(2)))
            s.wait(0.5)
            s.play(timen.animate.scale(0.25).shift(RIGHT*6.6+UP*4-UP*(n+1)*0.35))

        time=[1745]
        TIME(time)

        jar=[ImageMobject('Leyden_jar_engraving.png').scale_to_fit_height(5.2),
             Text('Leyden jar').scale(0.7).shift(DOWN*3),
             ImageMobject('Andreas_Cunaeus_discovering_the_Leyden_jar.png').shift(RIGHT*2.2).scale_to_fit_height(5.2),
             Text('Ewald Georg von Kleist').scale(0.7).shift(RIGHT*2.2+DOWN*3)]
        s.play(FadeIn(jar[0].shift(LEFT*3.3),jar[1].shift(LEFT*3.3)))
        s.play(FadeIn(jar[2],jar[3]))
        s.wait(2)
        s.play(FadeOut(jar[2],jar[3]))
        
        ball=[VGroup(
                     Circle(color=BLUE,fill_opacity=1).scale_to_fit_height(0.5),
                     MathTex('\mathbf{+}').scale_to_fit_width(0.35)).shift(RIGHT*1),
              VGroup(
                     Circle(color=BLUE,fill_opacity=1).scale_to_fit_height(0.5),
                     MathTex('\mathbf{+}').scale_to_fit_width(0.35)).shift(RIGHT*5),
              VGroup(
                     Circle(color=RED,fill_opacity=1).scale_to_fit_height(0.5),
                     MathTex('\mathbf{-}').scale_to_fit_width(0.35)).shift(RIGHT*5),
                Arrow(RIGHT,RIGHT*2.5,color=BLUE_C),#3
                Arrow(RIGHT,RIGHT*-0.5,color=BLUE_C),
                Arrow(RIGHT*5,RIGHT*3.5,color=RED_C),
                Arrow(RIGHT*5,RIGHT*6.5,color=BLUE_C),
                MathTex('F=?').shift(RIGHT*3+DOWN*3),#7
                Arrow(RIGHT,LEFT,color=YELLOW),
                Arrow(RIGHT,RIGHT*3,color=YELLOW).rotate(np.pi/3.2,about_point=RIGHT),
                Arrow(RIGHT,RIGHT*5,color=YELLOW).rotate(-np.pi/5.4,about_point=RIGHT),
                Arrow(RIGHT,RIGHT*2,color=YELLOW).rotate(np.pi/0.8,about_point=RIGHT),
               ]
        s.play(FadeIn(ball[0]),FadeIn(ball[2]),
               GrowArrow(ball[3]),GrowArrow(ball[5]))
        s.wait(0.5)
        s.play(FadeOut(ball[5],ball[2],ball[3]))
        s.play(FadeIn(ball[1]),
               GrowArrow(ball[4]),GrowArrow(ball[6]))
        s.wait(0.5)
        s.play(FadeOut(ball[1],ball[6]))
        s.play(Write(ball[7]),
               Transform(ball[4],ball[8]))
        s.play(Transform(ball[4],ball[9]))
        s.play(Transform(ball[4],ball[10]))
        s.play(Transform(ball[4],ball[11]))
        s.play(FadeOut(ball[4],ball[0],jar[1],jar[0],ball[7]))

        time.append(1760)
        TIME(time)
        bnl=[
            ImageMobject('伯努利.jpg').scale_to_fit_height(4),
            ImageMobject('伯努利0.jpg').scale_to_fit_height(7.2),
            ImageMobject('伯努利1.jpg').scale_to_fit_height(7.2),
            MathTex('Bernoulli').scale(0.7).shift(RIGHT*2.5+DOWN*(1.6-2.2)),
            Text('That electrical attraction follows the \nlaw of the inverse square has been \n suspected by Daniel Bernoulli.',
                 line_spacing=1,
                 font_size=25).shift(UP*2+RIGHT*3),#4
            Text('The History and Present State of Electricity, \n with Original Experiments')
        ]
        bnl.append(ImageMobject('富兰克林.jpg').scale_to_fit_height(4))#6
        bnl.append(Text('Franklin').shift(RIGHT*2.5+DOWN*2.4))
        bnl.append(ImageMobject('普里斯特利.jpeg').scale_to_fit_height(4))#8
        bnl.append(Text('Priestley').shift(RIGHT*2.5+DOWN*2.4))
        s.play(FadeIn(bnl[0].shift(DOWN*(3.6-2)+RIGHT*2.5),bnl[1].shift(LEFT*2.5)),Write(bnl[3]))
        s.play(FadeIn(bnl[2].shift(LEFT*2.5)),Write(bnl[4]))
        s.wait(2)
        s.play(FadeOut(bnl[0],bnl[3]),Unwrite(bnl[4]))
        s.play(FadeIn(bnl[6].shift(RIGHT*2.5),bnl[7]))
        s.wait(0.5)
        s.play(FadeOut(bnl[6],bnl[7]),
               FadeIn(bnl[8].shift(RIGHT*2.5),bnl[9]))
        s.play(Write(bnl[5].scale_to_fit_width(bnl[0].get_width()).shift(LEFT*2.5+DOWN*3.8)))
        s.wait(2)
        s.play(FadeOut(bnl[5],bnl[2],bnl[1],bnl[8],bnl[9]),
               FadeIn(bnl[6].shift(RIGHT*-5.2),bnl[7].shift(LEFT*5.2)))

        bnl.append(#10
            ImageMobject("Familiar_Introduction_to_Electricity_by_Joseph_Priestly,_plate_7.jpg"
                         ).scale_to_fit_height(4).shift(RIGHT*2.7))
        bnl.append(Text('?').next_to(bnl[6],UP+RIGHT))
        s.play(FadeIn(bnl[10]))
        s.play(Write(bnl[11]))
        s.wait(0.5)
        s.play(FadeOut(bnl[11],bnl[10]),
               FadeIn(bnl[8].shift(RIGHT*0.3),bnl[9].shift(RIGHT*0.3)))
        
        left = Text('✉️').shift(LEFT*2+UP*2.5)
        left_c = left.copy()
        right_c = left_c.copy().shift(4 * RIGHT)
        # Make the circles in front of the text in front of the arcs.
        s.play(Write(left_c.set_z_index(3)))
        s.play(Transform(left_c, right_c, path_arc=-90 * DEGREES), run_time=2)
        s.wait(2)
        s.play(FadeOut(left_c,bnl[6],bnl[7],bnl[8],bnl[9]))
        s.wait()

        time.append(1766)
        Time=MathTex('December 21st').scale(0.7).shift(UP*0.9)
        timen=Text(str(time[2]))
        s.play(Write(Time))
        s.play(Write(timen.scale(2)),)
        s.wait(0.5)
        s.play(timen.animate.scale(0.25).shift(RIGHT*6.6+UP*4-UP*(2+1)*0.35),ShrinkToCenter(Time))
        s.wait(2)

#=======================================INSERT 3D.===================================================#
        ORG=LEFT*(np.sqrt(0.2**2+0.7**2))
        gvt=[
            AnnularSector(inner_radius=2,outer_radius=2.1,color=GREEN,angle=4 * PI / 2),#0
            Dot(point=UP*0.2+LEFT*0.7).set_color(RED),
            VGroup(Line(LEFT*2, RIGHT*2).set_color(BLUE).rotate(10 * DEGREES, about_point=ORG),
            Line(LEFT*2,RIGHT*2).set_color(BLUE).rotate(-10 * DEGREES, about_point=ORG)).rotate(-15.9453959*DEGREES),
            AnnularSector(inner_radius=2,outer_radius=2.1,color=BLUE,start_angle=(180-9)*DEGREES,angle=-13.5*DEGREES),
            AnnularSector(inner_radius=2,outer_radius=2.1,color=BLUE,start_angle=-2*DEGREES,angle=-27.5*DEGREES),
            ]
        s.play(FadeIn(gvt[0]),DrawBorderThenFill(gvt[1]))
        s.play(GrowFromPoint(gvt[2][0],UP*0.2+LEFT*0.7),GrowFromPoint(gvt[2][1],UP*0.2+LEFT*0.7),
               GrowFromCenter(gvt[4]),GrowFromCenter(gvt[3]))
        gvt.append(VGroup(MathTex(r'F=0').shift(DOWN*3.5),
                   MathTex(r'Q=0').shift(DOWN*3.5+RIGHT*2),
                   Arrow(RIGHT*-1.2,RIGHT*1.2).shift(DOWN*3.5)))#5
        s.play(Indicate(gvt[4]),Indicate(gvt[3]))
        s.play(Write(gvt[-1][0]))
        s.play(gvt[-1][0].animate.shift(LEFT*2),Write(gvt[-1][1]),GrowArrow(gvt[-1][2]))
        s.wait()
        Pst=[
            ImageMobject('富兰克林0').scale_to_fit_height(7.2).shift(LEFT*2.5),
            ImageMobject('富兰克林1').scale_to_fit_height(7.2).shift(LEFT*2.5),
            Text('The attraction of elecrticty is subject\nto the same laws with that of gravitat-\n-ation, and is therefore according to the\n squares of the distances.',
                 line_spacing=1,
                 font_size=25).shift(UP*1.5+RIGHT*3),
            Text('Since it is easily demonstrated that were\nthe earth in the form of a shell, a body \n in the inside of it would not be attr-\n-acted to one side more than another?'
                 ,t2c={'?':YELLOW,"easily demonstrated ":YELLOW},
                 line_spacing=1,
                 font_size=25).shift(DOWN+RIGHT*3),

        ]
        s.play(FadeOut(gvt[2],gvt[3],gvt[4],gvt[2],gvt[0],gvt[1]),FadeIn(Pst[0]),gvt[-1].animate.shift(RIGHT*3))
        s.play(FadeIn(Pst[1]),Write(Pst[2]))
        s.wait(0.5)
        s.play(Write(Pst[-1]))
        s.wait(3)
        s.play(Unwrite(Pst[-1]),Unwrite(Pst[-2]),FadeOut(gvt[-1],Pst[0],Pst[1]))
        s.wait()

        Cavendish=[
            ImageMobject('Cavendish_Henry_signature').scale_to_fit_height(6),
            Text('Henry Cavendish').scale(0.7).to_edge(DOWN,buff=0.25),
            Group(ImageMobject('8').scale_to_fit_height(6),
            ImageMobject('9').scale_to_fit_height(6)).arrange(RIGHT, buff=0.25),
            Text('The Electrical Researches of the Honourable Henry Cavendish').scale_to_fit_width(9).to_edge(DOWN,buff=0.25),
            ImageMobject('apparatus').scale_to_fit_width(7),
            MathTex(r'F\propto r^{-n},',r'\space  n=2\pm \frac{1}{60} ').scale(0.7).to_edge(DOWN,buff=0.5)
        ]
        s.play(FadeIn(Cavendish[0]),Write(Cavendish[1]))
        s.wait(0.5)
        s.play(FadeOut(Cavendish[0],Cavendish[1]),FadeIn(Cavendish[2],Cavendish[3]))
        s.wait(2)
        s.play(FadeOut(Cavendish[2],Cavendish[3]))
        s.play(FadeIn(Cavendish[-2]))
        s.play(Write(Cavendish[-1]))
        s.wait()
        s.play(Circumscribe(Cavendish[-1][-1]))
        s.wait(2)
        s.play(FadeOut(Cavendish[-1],Cavendish[-2]))
        s.wait()


        time.append(1785)
        n=len(time)-1
        timen=Text(str(time[n]))
        s.play(Write(timen.scale(2)))
        s.wait(0.5)
        s.play(timen.animate.scale(0.25).shift(RIGHT*6.6+UP*4-UP*(n+1)*0.35))


        cl=[
            ImageMobject('Coulomb').scale_to_fit_height(5),
            Text('Coulomb').to_edge(DOWN,buff=0.5),
            Tex('Conclusion:',' Inverse Squared Law'),
        ]
        s.play(FadeIn(cl[0]),Write(cl[1]))
        s.wait(0.2)
        s.play(FadeOut(cl[0],cl[1]),Write(cl[-1]))
        s.play(ApplyWave(cl[-1][-1]))
        s.wait()
        cl.append(Group(ImageMobject('库伦').scale_to_fit_height(6),
                        ImageMobject('库伦实验').scale_to_fit_height(6)).arrange(RIGHT,buff=0.75))
        s.play(FadeOut(cl[-2]),FadeIn(cl[-1]))
        s.wait()
        s.play(FadeOut(cl[-1]))

        cl.append(
            VGroup(
            MathTex(r'|\vec{\mathbf{F} } |\propto| \vec{r_1}-\vec{r_2}|^2'),
            MathTex(r'|\vec{\mathbf{F} } |\propto q_1\cdot q_2')
            )
        )
        cl[-1][-1].shift(cl[-1][0].get_left()+cl[-1][-1].get_width()/2+DOWN*0.25)
        cl.append(
            MathTex(r'|F|',r'=k_{\text{e}}{\frac {|q_{1}||q_{2}|}{r^{2}}}').shift(DOWN*1)
        )
        s.play(Write(cl[-2][-1]),run_time=1.5)
        s.play(Write(cl[-2][-2]),run_time=1.5)
        s.wait()
        cl.append(MathTex(r'\Downarrow ').scale(1.2))
        s.play(cl[-3].animate.shift(UP),GrowFromEdge(cl[-1],UP))
        s.play(Write(cl[-2]),run_time=3)
        s.wait()
        s.play(FadeOut(cl[-1],cl[-2],cl[-3]))


        func = lambda pos: pos
        colors = [RED, YELLOW, BLUE, DARK_GRAY]
        vf = ArrowVectorField(
            func, min_color_scheme_value=1, max_color_scheme_value=10, colors=colors
        )

        dot=Dot()
        point=always_redraw(
            lambda: Arrow(
                start=dot.get_center(),
                end=dot.get_center()/3+dot.get_center(),
                stroke_width=3
            )
        )
        similar=[MathTex(r'F_e'),
                 MathTex(r'\sim'),#1
                 MathTex(r'\gg'),#2
                 MathTex(r'attract').shift(RIGHT*-2+UP*1.5),#3
                 MathTex(r'repel').shift(RIGHT*-2+UP*-1.5),#4
                 MathTex(r'attract').shift(RIGHT*2+UP*1.5)#5
                 ]
        s.play(FadeIn(vf,dot,point))
        s.play(FadeIn(similar[0].to_edge(DOWN,buff=0.5)))
        s.play(dot.animate.shift(UP+RIGHT*2.21))
        s.play(dot.animate.shift(UP*0.242+RIGHT*2.984))
        s.play(dot.animate.shift(UP*-3.3+RIGHT*-5.8))
        s.play(dot.animate.shift(UP*2+RIGHT*-4.74))
        s.play(FadeOut(dot,point,vf))
        s.play(similar[0].animate.shift(LEFT-similar[0].get_center()))
        Fg=MathTex(r'F_g').shift(RIGHT)
        s.play(Write(similar[1]),Write(Fg))
        s.wait()
        s.play(TransformFromCopy(Fg,similar[-1]))
        s.wait()
        s.play(TransformFromCopy(similar[0],similar[3]))
        s.play(TransformFromCopy(similar[0],similar[4]))
        s.wait(0.2)
        s.play(ReplacementTransform(similar[1],similar[2]))
        s.play(Indicate(similar[2]))
        s.wait()
        s.play(FadeOut(similar[0],similar[3],similar[4],similar[2],Fg,similar[-1]))
        s.wait()

        def TIMe(time,n):
            timen=Text(str(time[n]))
            s.play(Write(timen.scale(2)))
            s.wait(0.5)
            s.play(timen.animate.scale(0.25).shift(RIGHT*6.6+UP*4-UP*(n+1)*0.35))

        time=[1745,1760,1766,1785,1825,1835,1860,1865,1873,1880]


        e0=[
            MathTex(r'\varepsilon 0 ?'),
            MathTex(r'\varepsilon 0')
        ]
        ke=[MathTex(r'k_e')]
        s.play(FadeIn(e0[0]))
        O=[
            ImageMobject('Oheaviside').scale_to_fit_height(6),
            Text('Oliver Heaviside').to_edge(DOWN,buff=0.25)
        ]
        s.wait(0.2)
        s.play(FadeOut(e0[0]),FadeIn(O[1],O[0]))
        s.wait()
        s.play(FadeOut(O[0],O[1]))
        TIMe(time,9)
        s.wait()
        s.play(FadeIn(e0[1]))
        s.play(e0[1].animate.shift(LEFT),TransformFromCopy(e0[1],ke[0].shift(RIGHT)))
        s.wait(0.2)
        s.play(FadeOut(e0[1],ke[0]))
        s.wait()

        TIMe(time,5)
        ke.append(MathTex(r'k_e=1'))
        s.play(Write(ke[1]))
        Gauss=[
            ImageMobject('Gauss').scale_to_fit_height(6)
        ]

        s.wait()
        s.play(FadeOut(ke[1]),Write(cl[-2].shift(UP)))
        #Here is 3b1b video that cut a ball into 4pir2
        s.wait(3)
        s.play(FadeIn(Gauss[0]))
        s.wait(2)
        area=MathTex(r'S=',r'4\pi',r'r^2')
        fm=MathTex(r'|F|=',r'k_{\text{e}}',r'{\frac {|q_{1}||q_{2}|}{r^{2}}}')
        fm1=MathTex(r"\frac{k'_e}{4\pi}")
        s.play(FadeOut(Gauss[0],cl[-2]),Write(area))
        s.wait()
        s.play(Indicate(area[-1])) 
        s.play(area.animate.shift(LEFT*2),Write(fm.shift(RIGHT*2)))
        s.play(Indicate(area[1]),Indicate(area[2]))
        s.play(ReplacementTransform(fm[1],fm1.shift(fm[1].get_center()+UP*0.1)))
        s.wait(2)
        rationalization=Text('Rationalization').scale(1.5)
        s.play(
            FadeOut(fm,fm1,area),
            ShowIncreasingSubsets(rationalization),run_time=2
        )

        s.wait(0.2)
        s.play(FadeOut(rationalization))

        circle = Circle(color=BLACK,fill_opacity=1)
        circle1 = Circle(color=BLUE)
        circle0 = Circle(color=BLUE,fill_opacity=1)
        inner=Text('Inner')
        outer=Text('Outer').to_edge(UP)
        rec=Rectangle(height=8.5,width=15,color=BLUE,fill_opacity=1)
        s.play(Create(circle1))
        s.wait()
        s.play(FadeIn(circle0),Write(inner))
        s.wait()
        s.play(FadeIn(rec,circle),FadeOut(inner),Write(outer))
        s.wait()
        s.play(FadeOut(outer,rec,circle0,circle1,circle))
#Gauss
        fml=[
            MathTex(r" \mathbf {E}=\frac {{k_e}'}{4\pi}\frac {q}{r^{2 }").to_edge(DOWN,buff=0.5),
            MathTex(r" \mathbf {E}=\frac { {k_e}' }{4\pi r^{2 }}q").to_edge(DOWN,buff=0.5),
            MathTex(r" \oint _{S}\mathbf {E} \cdot d\mathbf {A} =\oint _{S}\frac { {k_e}'  }{4\pi r^{2 }}q \cdot d\mathbf {A}").to_edge(DOWN,buff=0.5),
            MathTex(r" \oint _{S}\mathbf {E} \cdot d\mathbf {A} =q\cdot {k_e}'  \oint _{S}\frac {1 }{4\pi r^{2 } } \cdot d\mathbf {A}").to_edge(DOWN,buff=0.5),
            MathTex(r" \oint _{S}\mathbf {E} \cdot d\mathbf {A} =q\cdot {k_e}'").to_edge(DOWN,buff=0.5),
        ]
        s.play(Write(fml[0]))

        area=MathTex(r'S=4\pi r^2').to_edge(UP)
        s.play(Write(area))
        s.play(Transform(fml[0],fml[1]))
        s.play(Transform(fml[0],fml[2]))
        s.play(Transform(fml[0],fml[3]))
        s.play(Transform(fml[0],fml[4]))
        s.wait()
        s.play(FadeOut(fml[0],area))
        s.wait()

        TIMe(time,4)
        Faraday=[
            ImageMobject('Faraday').scale_to_fit_height(6),
            Text('Faraday').to_edge(DOWN,buff=0.25)

        ]
        s.play(FadeIn(Faraday[0],Faraday[-1]))
        Faraday.append(
            ImageMobject('Faraday_magnetic_rotation').scale_to_fit_height(6)
        )

        
        def electric_field_charge1(pos):
            distance = np.linalg.norm(pos - LEFT * 2)
            if distance == 0:
                return np.zeros(3)  # 返回零向量
            return 1 / distance * normalize(pos - LEFT * 2)

        def electric_field_charge2(pos):
            distance = np.linalg.norm(pos - RIGHT * 2)
            if distance == 0:
                return np.zeros(3)  # 返回零向量
            return 1 / distance * normalize(pos - RIGHT * 2)

        # 定义总电场函数为两个电荷电场的叠加
        def func(pos):
            field_charge1 = electric_field_charge1(pos)
            field_charge2 = electric_field_charge2(pos)
            
            # 处理零点，如果有一个电场为零，则返回零向量
            if np.all(field_charge1 == 0) or np.all(field_charge2 == 0):
                return np.zeros(3)
            
            return 3*(field_charge1 + field_charge2)
        
        s.wait(0.2)
        s.play(FadeOut(Faraday[0],Faraday[1]),FadeIn(Faraday[-1]))
        s.wait(0.2)
        s.play(FadeOut(Faraday[-1]))
        stream_lines = StreamLines(func, stroke_width=3, max_anchors_per_line=30)
        s.add(stream_lines)
        stream_lines.start_animation(warm_up=True, flow_speed=1.5)
        s.wait(3)
        s.play(stream_lines.end_animation())

        Lenz=[
            ImageMobject('800px-Heinrich_Friedrich_Emil_Lenz.jpg').scale_to_fit_height(6).shift(LEFT*-2.5),
            Text('Emil Lenz').to_edge(DOWN,buff=0.25).shift(LEFT*-2.5)

        ]
        s.play(FadeIn(Lenz[0],Lenz[1]))
        s.wait()#solenoid
        s.play(FadeOut(Lenz[0],Lenz[1]))
        ps=RIGHT
        Neumann=[
            ImageMobject('Neumann').scale_to_fit_height(6).shift(LEFT*2.5),
            Text('Franz Ernst Neumann').to_edge(DOWN,buff=0.25).shift(LEFT*2.5),
            MathTex(r' \Phi _{B}=\iint _{\Sigma (t)}\mathbf {B} (t)\cdot \mathrm {d} \mathbf {A} ').shift(UP*-4),
            MathTex(r' {\mathcal {E}}=-{\frac {\mathrm {d} \Phi _{B}}{\mathrm {d} t}}').shift(UP*-1.5),
            MathTex(r' {\mathcal {E}}=\oint \left(\mathbf {E} +\mathbf {v} \times \mathbf {B} \right)\cdot \mathrm {d} \mathbf {l} ').shift(UP*-1.5),
        ]
        for _ in range(2,len(Neumann)):
            Neumann[_].shift(Neumann[_].get_width()/2+ps)
        s.play(FadeIn(Neumann[0],Neumann[1]))
        s.play(Write(Neumann[2]),Write(Neumann[3]),Write(Neumann[4]))
        s.wait()
        s.play(FadeOut(Neumann[0],Neumann[1]),Unwrite(Neumann[2]),Unwrite(Neumann[3]),Unwrite(Neumann[4]))

        Maxwell=[
            ImageMobject('Maxwell').scale_to_fit_height(7.2)
        ]
        s.play(FadeIn(Maxwell[0]))
        s.wait()
        s.play(FadeOut(Maxwell[0]))

        lws=[
            Text("Faraday's Law").shift(UP*1.5),
            Text("Lenz's Law").shift(UP*-1.5),
            Text('?')
        ]
        s.play(GrowFromEdge(lws[0],DOWN))
        s.play(GrowFromEdge(lws[1],UP))
        s.play(DrawBorderThenFill(lws[-1]))
        s.wait()
        s.play(ShrinkToCenter(lws[0]),ShrinkToCenter(lws[-1]),ShrinkToCenter(lws[1]))
        s.wait()

        TIMe(time,6)

        Maxwell=[
            ImageMobject('Maxwell').scale_to_fit_height(7.2)
        ]


        def electric_field_charge1(pos):
            distance = np.linalg.norm(pos - LEFT * 2)
            epsilon = 0.1  # small constant to avoid division by zero
            return 1 / (distance + epsilon) * normalize(pos - LEFT * 2)

        def electric_field_charge2(pos):
            distance = np.linalg.norm(pos - RIGHT * 2)
            epsilon = 0.1  # small constant to avoid division by zero
            return 1 / (distance + epsilon) * normalize(pos - RIGHT * 2)


        # 定义总电场函数为两个电荷电场的叠加
        def func(pos):
            field_charge1 = electric_field_charge1(pos)
            field_charge2 = electric_field_charge2(pos)
            
            # 处理零点，如果有一个电场为零，则返回零向量
            if np.all(field_charge1 == 0) or np.all(field_charge2 == 0):
                return np.zeros(3)
            
            return 3*(field_charge1 - field_charge2)
        
        stream_lines = StreamLines(func, stroke_width=3, max_anchors_per_line=2,color=BLUE)
        s.add(stream_lines)
        rec=Rectangle(color=BLACK,fill_opacity=0.8).scale(18)
        nabla=VGroup(
            MathTex(r"\oint_{\mathbb{R}^2}  \mathbf{E} \cdot\mathrm{d}\mathbf{s} = {Q}\cdot {k_e}'"),
            MathTex(r'\Updownarrow  ?'),
            MathTex(r"\nabla \cdot \mathbf{E} ={\rho}\cdot {k_e}'"),
        ).arrange(DOWN,buff=1.25)
 
        Maxwell.append(
            Group(
                ImageMobject('E1 (1)').scale_to_fit_height(5),
                ImageMobject('E1 (2)').scale_to_fit_height(5),
            ).arrange(RIGHT,buff=0.25).to_edge(UP,buff=0.25)
        )
        Maxwell.append(
            MathTex(r"\mathbf{e}  = \frac{1}{4\pi E^2} \frac{Q}{r^2} \hat{r} ").to_edge(DOWN,buff=0.5)
        )
        stream_lines.start_animation(flow_speed=1.5)
        s.wait(3)
        s.play(FadeIn(rec))
        s.play(Write(nabla[1]))
        s.play(Write(nabla[0]))
        s.play(Write(nabla[-1]))
        s.wait()
        s.play(FadeOut(rec),Unwrite(nabla[0]),Unwrite(nabla[1]),Unwrite(nabla[-1]))
        s.play(stream_lines.end_animation(),FadeIn(Maxwell[-2]),Write(Maxwell[-1]))
        s.wait(2)
        s.play(FadeOut(Maxwell[-2],Maxwell[-1]))

        TIMe(time,7)
        # Create ImageMobject objects
        ImageMobjects0 = [
            ImageMobject("480"),
            ImageMobject("481"),
            ImageMobject("482"),
        ]
        ImageMobjects1 = [
            ImageMobject("483"),
            ImageMobject("484"),
            ImageMobject("485"),
        ]
        Image=ImageMobject("483").scale_to_fit_height(3.5)
        # Create a Mobject container and arrange the ImageMobjects
        ImageMobject_group0 = Group(*ImageMobjects0).scale_to_fit_height(3.5).arrange_in_grid(rows=1, cols=3, buff=0.75)
        ImageMobject_group1 = Group(*ImageMobjects1).scale_to_fit_height(3.5).arrange_in_grid(rows=1, cols=3, buff=0.75)
        ImageMobject_group = Group(ImageMobject_group0, ImageMobject_group1).arrange_in_grid(rows=2, cols=1, buff=0.25)

        # Add the ImageMobject group to the scene
        s.play(FadeIn(ImageMobject_group))
        s.wait(3)  # Optional waiting #TIMe before animation

        # Define the target position for the folded images
        folded_position = Image.to_corner(UL,buff=0.5).get_center()

        # Animation to move and resize the images into the folded position
        s.play(
            ImageMobject_group[0][0].animate.move_to(folded_position),
            ImageMobject_group[0][1].animate.move_to(folded_position),
            ImageMobject_group[0][2].animate.move_to(folded_position),
            ImageMobject_group[1][0].animate.move_to(folded_position),
            ImageMobject_group[1][1].animate.move_to(folded_position),
            ImageMobject_group[1][2].animate.move_to(folded_position),
            )

        s.wait(1)  # Optional waiting #TIMe after animation
 
        Eq = VGroup(
            MathTex(r"{[A]\space \space  \mathbf {J} _{\mathrm {tot} }=\mathbf {J} +{\frac {\partial \mathbf {D} }{\partial t}}}"),
            MathTex(r"{[B]\space \space  \mu \mathbf {H} =\nabla \times \mathbf {A} }"),
            MathTex(r"{[C]\space \space  \nabla \times \mathbf {H} =\mathbf {J} _{\mathrm {tot} }}"),
            MathTex(r"{[D]\space \space  \mathbf {E} =\mu \mathbf {v} \times \mathbf {H} -{\frac {\partial \mathbf {A} }{\partial t}}-\nabla \phi }"),
            MathTex(r"{[E]\space \space  \mathbf {E}\cdot {\varepsilon } =\mathbf {D} }"),
            MathTex(r"{[F]\space \space  \mathbf {E} \cdot {\sigma }=\mathbf {J} }"),
            MathTex(r"{[G]\space \space  \nabla \cdot \mathbf {D} =\rho }"),
            MathTex(r"{[H]\space \space  \nabla \cdot \mathbf {J} _{\mathrm {tot} }=0}"),
        ).arrange(DOWN, aligned_edge=LEFT).shift(RIGHT*1.5)

        # Animate the appearance of equations
        s.play(*[FadeIn(eq) for eq in Eq])
        s.wait()
        s.play(Eq[6].animate.set_color(YELLOW))
        s.wait(2)
        s.play(FadeOut(Eq,ImageMobject_group))        
        s.wait()

        TIMe(time,8)
        Maxwell.append(ImageMobject('100').scale_to_fit_height(6))
        s.play(FadeIn(Maxwell[-1]))
        s.wait(2)
        s.play(FadeOut(Maxwell[-1]))
        s.wait()

        Maxwell.append(
            Text('Although some of the equations could be combined to eliminate some \nquantities, the objective of his list was to express every relation of \nwhich there was any knowledge of, rather than to obtain compactness of \nmathematical formulae.',
                 font_size=27,line_spacing=1.5)
        )
        s.play(Write(Maxwell[-1]),run_time=5)
        s.wait(4)
        s.play(Unwrite(Maxwell[-1]))

        Maxwell.append(ImageMobject('light').scale_to_fit_height(6).to_edge(buff=1))
        Maxwell.append(Text(' The velocity of transverse undulations \n in our hypothetical medium, calculated \n from the electromagnetic experiments of\n MM. Kohlrausch and Weber, agrees so \n exactly with the velocity of light ca-\n -lculated from the optical experiments \n of M. Fizeau, that we can scarcely avoid \n the inference that light consists in the\n transverse undulations of the same medium \n which is the cause of electric and magnetic\n phenomena.'
                            ,line_spacing=1,
                        font_size=27).shift(RIGHT*2.5))
        s.play(FadeIn(Maxwell[-2]),Write(Maxwell[-1]))
        s.wait(2)
        s.play(FadeOut(Maxwell[-2],Maxwell[-1]))

        s.play(FadeIn(O[1],O[0]))
        s.wait()
        s.play(FadeOut(O[0],O[1]))

        eqs=VGroup(MathTex(r'\nabla \cdot \mathbf{D} =\rho _f').set_color(BLUE),
                      MathTex(r'\nabla \cdot \mathbf{B} = 0').set_color(RED),
                      MathTex(r'\nabla \times  \mathbf{E} = -\cfrac{\partial \mathbf{B}}{\partial t }').set_color(YELLOW),
                      MathTex(r'\nabla \times  \mathbf{H} = \mathbf{J}_f +  \cfrac{\partial \mathbf{D}}{\partial t }').set_color(GREEN)
        ).arrange(DOWN, aligned_edge=LEFT)
        eqt=Text('Maxwell Equation').to_edge(DOWN,buff=0.25)
        s.play(Write(eqs),run_time=2)
        s.wait()
        s.play(Write(eqt))
        s.wait(2)
        s.play(FadeOut(eqs,eqt))
        s.wait()




script1='''
The gods descended, not with a sudden clap,
But quiet, subtle, in a cosmic lap.
The world transformed, lost its former guise,
As gentle light unveiled celestial ties.

The ether fell from its divine height,
Lorenz's touch dimmed humanity's light.
A new deity, with love profound,
Wisdom vast, in grace, she was crowned.

In lively chatter, the verdict resounds,
Newton's spheres condemned to earthly bounds.
Oblivious, they'd return anew,
In divine warfare, an epoch true.

A grand spectacle, surpassing the past,
Anticipating a future so vast.
A tale of old and epochs untold,
In divine battles, destinies unfold.
'''

script2='''
祂来悄无声，
宙光微微映。
古远形踪隐，
辉柔故事精。

以太去神座，
不公洛伦兹。
新祂乃爱姓，
智滔塑绝迹。

喧哗下决断，
牛顿粒已斩。
忽回凡间境，
众人均未知。

此乃群祂世，
伟大胜今时。
如前无古人，
似后无来者。
'''

class ImageMobjectGrid(Scene):
    def construct(s):
        text1 = Text(script1, font='Times New Roman').scale_to_fit_height(7).shift(LEFT*2)
        text2 = Text(script2, font='Source Han Sans').scale_to_fit_height(7).shift(LEFT*-4)
        s.play(Write(text1),Write(text2),run_time=20)
        s.wait(2)
        s.play(FadeOut(text1,text2))


