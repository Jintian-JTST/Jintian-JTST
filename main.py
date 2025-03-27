from manim import *

'''class BilingualSubtitles:
    """Manim 双语字幕控制器（全局可复用）"""
    def __init__(self, scene, ch_subtitles, en_subtitles, 
                ch_font_size=30, en_font_size=24,
                line_spacing=0.5, margin=1.5):
        """
        参数说明：
        scene: Manim 场景对象
        ch_subtitles/en_subtitles: 中英文字幕列表（需一一对应）
        ch_font_size/en_font_size: 字号设置
        line_spacing: 行间距（单位：屏幕高度比例）
        margin: 字幕距离底部的边距（单位：屏幕高度比例）
        """
        self.scene = scene
        self.ch_subs = ch_subtitles
        self.en_subs = en_subtitles
        self.ch_font_size = ch_font_size
        self.en_font_size = en_font_size
        self.line_spacing = line_spacing
        self.margin = margin
        self.current_subs = []  # 当前显示的字幕对象

    # 自动换行计算（根据屏幕宽度和字号）
    def _auto_wrap(self, text, is_chinese):
        max_width = config.frame_width * 0.9
        avg_char_width = self.ch_font_size * 0.05 if is_chinese else self.en_font_size * 0.03
        max_chars = int(max_width / avg_char_width)
        return '\n'.join(textwrap.wrap(text, width=max_chars))

    # 生成双语字幕组
    def _create_sub_group(self, ch_text, en_text):
        # 中文处理
        wrapped_ch = self._auto_wrap(ch_text, is_chinese=True)
        ch_label = Text(wrapped_ch, font="Source Han Sans CN", 
                       font_size=self.ch_font_size, color=WHITE)
        
        # 英文处理
        wrapped_en = self._auto_wrap(en_text, is_chinese=False)
        en_label = Text(wrapped_en, font="Arial", 
                       font_size=self.en_font_size, color=WHITE)
        
        # 垂直排列
        en_label.next_to(ch_label, DOWN, buff=self.line_spacing)
        return VGroup(ch_label, en_label).set_y(-config.frame_height/2 + self.margin)

    # 显示字幕动画
    def display_subtitle(self, index, duration=2):
        """显示指定索引的字幕（duration 为自动计算的基础时长）"""
        # 自动计算显示时长
        total_lines = (self.ch_subs[index].count('\n') + 1 + 
                      self.en_subs[index].count('\n') + 1)
        final_duration = max(duration, total_lines * 0.8)
        
        # 创建字幕组
        sub_group = self._create_sub_group(self.ch_subs[index], self.en_subs[index])
        
        # 执行动画
        self.scene.play(FadeIn(sub_group, run_time=0.5))
        self.scene.wait(final_duration)
        self.scene.play(FadeOut(sub_group, run_time=0.5))
        self.current_subs = []
'''

#111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111



class first(Scene):
    def construct(self):
        Title=Text("Derivations of Lagrange Equation")
        self.play(Write(Title))
        self.wait(1)
        JTST=Tex('JTST').shift(DOWN)
        self.play(Title.animate.shift(UP*0.5),FadeIn(JTST,shift=DOWN))
        self.wait(5)
        self.play(FadeOut(Title,JTST))



class Intro(Scene):
    def construct(self): 


        # Derivation of Lagrange Equation
        minimal_principle=[Text("The Principle of Least Action",color=YELLOW),
                           Text("Hamilton's Principle").shift(DOWN)]
        self.play(Write(minimal_principle[0]))
        self.wait(1)

        # 按顺序显示字幕

        self.play(minimal_principle[0].animate.shift(UP),TransformFromCopy(minimal_principle[0],minimal_principle[1]))
        des=[Tex("Something acculumates over time is the smallest").scale(0.75).shift(DOWN*2),
             Tex("Something acculumates over time"," is the smallest").scale(0.75).shift(DOWN*2),
             Tex("Action is the smallest").scale(0.75).shift(DOWN*2)]
        self.wait(2)
        self.play(FadeOut(minimal_principle[1]))


        self.play(TransformFromCopy(minimal_principle[0],des[0]))
        #des[0].become(des[1])
        self.add(des[1])
        self.remove(des[0])
        #self.play(FadeOut(des[0]))
        self.wait()

        self.play(Indicate(des[1][0]))
        self.play(Transform(des[1],des[2]))
        self.play(Circumscribe(des[2],shape=Rectangle))
        self.wait(2)
        self.play(FadeOut(des[2],des[1]),minimal_principle[0].animate.shift(UP*2))


class Lagrange(Scene):
    def construct(self):
        minimal_principle=[Text("The Principle of Least Action",color=YELLOW).shift(UP*3)]
        self.add(minimal_principle[0])
        # Define the action
        action=MathTex(r"S",r" = \int_{t_1}^{t_2} L(",r"q",r",\dot{q},t)\ \mathrm{d}t")
        self.play(Write(action))
        label=[
            MathTex(r"Action",color=RED).scale(0.75).next_to(action,LEFT),
            MathTex(r"q:\ Generalized\ Coordinates",color=GREEN).scale(0.5).next_to(action,DOWN)
        ]
        self.wait(1)
        self.play(TransformFromCopy(action[0],label[0]))
        self.play(TransformFromCopy(action[2],label[1]))
        self.wait(2)
        action.generate_target()
        action.target.scale(0.75).shift(UP*1.5)
        self.play(MoveToTarget(action),FadeOut(label[0],label[1]))
        self.wait(1)

        axes = Axes(x_range=[1.5, 5.5], y_range=[2, 9], x_length=9, y_length=6).shift(DOWN*2)
        func = axes.plot(lambda x: -x**2+6*x-1, color=BLUE, x_range=[2,5])
        dot_s=axes.get_graph_label(
            graph=func,
            label=MathTex(r'q(t_1)').scale(0.5),
            x_val=2,
            dot=True,
            direction=LEFT
        )
        dot_e=axes.get_graph_label(
            graph=func,
            label=MathTex(r'q(t_2)').scale(0.5),
            x_val=5,
            dot=True,
            direction=RIGHT
        )
        fun1 = axes.plot(lambda x: -x**2+6*x-1+0.5*(x-2)*(x-5)*(x-3)*(x-4), color=RED, x_range=[2,5])
        funcs=[
            axes.plot(lambda x: -x**2+6*x-1+0.5*(x-2)*(x-5)*(x-2.7)*(x-3.68), color=RED, x_range=[2,5]),
            axes.plot(lambda x: -x**2+6*x-1+0.4*(x-2)*(x-5)*(x-3.9)*(x-2.7), color=RED, x_range=[2,5]),
            axes.plot(lambda x: -x**2+6*x-1+0.1*(x-2)*(x-5)*(x-3.88)*(x-2.46), color=RED, x_range=[2,5])
        ]
        COOR0=MathTex(r'q(t)')
        COOR1=MathTex(r'q(t)+',r'\delta q(t)').align_to(COOR0,LEFT).shift(DOWN*0.5)
        COOR=VGroup(COOR0,COOR1).scale(0.75).shift(RIGHT*5)
        S=2.0
        s_S=Variable(S,Text('S'),num_decimal_places=3)
        s_S.label.set_color(BLUE)
        s_S.shift(LEFT*5+UP*1.5)
        # creates the T_label
        self.play(Create(func),FadeIn(dot_s))
        self.play(FadeIn(dot_e))
        self.wait(2)
        self.play(TransformFromCopy(func,COOR[0]))
        self.play(Write(s_S))
        self.wait(1)
        S_tracker=s_S.tracker
        stwo=MathTex(r'>2').shift(LEFT*2.75+UP*1.5)
        S=2.5
        self.play(TransformFromCopy(func,fun1),S_tracker.animate.set_value(S))
        self.wait(1)
        self.play(TransformFromCopy(fun1,COOR[1]),COOR[0].animate.shift(UP*0.5))
        self.play(s_S.animate.shift(LEFT*0.5),GrowFromEdge(stwo,LEFT))
        self.play(Indicate(s_S),Indicate(stwo))
        self.wait()
        S=2.3
        self.play(ReplacementTransform(fun1,funcs[0]),S_tracker.animate.set_value(S))
        S=2.7
        self.play(ReplacementTransform(funcs[0],funcs[1]),S_tracker.animate.set_value(S))
        S=2.2
        self.play(ReplacementTransform(funcs[1],funcs[2]),S_tracker.animate.set_value(S))
        self.wait()
        self.play(Wiggle(funcs[2]),Circumscribe(COOR1),Circumscribe(stwo))
        self.wait(2)
        deltaQ=MathTex(r'\delta q(t_1)=\delta q(t_2)=0').shift(DOWN*3)
        self.play(FadeOut(minimal_principle[0],s_S,stwo,action,COOR),
                  func.animate.shift(UP),dot_e.animate.shift(UP),dot_s.animate.shift(UP),funcs[2].animate.shift(UP))
        self.wait(0.5)
        self.play(Indicate(dot_e),Indicate(dot_s))
        self.play(Write(deltaQ))


        self.wait()

class DERIVE(Scene):
    def construct(self):
        # Remove the Title scene class usage
        title = Title("Formal Derivations",color=BLUE)  # Use Tex instead
        self.play(Write(title))
        
        
        minimal_principle = Text("The Principle of Least Action")
        self.play(FadeIn(minimal_principle))
        self.wait()

        s_ds = MathTex(r'S+\delta S=S').shift(UP*2)
        ds_0 = MathTex(r'\longrightarrow\quad',r'\delta S=0').shift(UP*2 + RIGHT*1.5)
        self.play(ReplacementTransform(minimal_principle, s_ds))
        self.wait(2)
        self.play(s_ds.animate.shift(LEFT*2), GrowFromEdge(ds_0,LEFT))
        self.wait(3)
        ds_0[1].generate_target()
        ds_0[1].target.scale(0.75).shift(LEFT*8)
        self.play(Unwrite(s_ds),FadeOut(ds_0[0]), MoveToTarget(ds_0[1]))
        self.wait()

        par = [
            MathTex(
                r"\mathrm{d}",
                r"Z",
                r" = \left( ",
                r"\frac{\partial }{\partial \textcolor{yellow}{x}}",
                r"Z ",
                r" \right) ",
                r"\mathrm{d}",
                r"\textcolor{yellow}{x} + \left( ",
                r"\frac{\partial }{\partial \textcolor{cyan}{y}}",
                r" Z",
                r" \right)",
                r"\mathrm{d}",
                r"\textcolor{cyan}{y}",
                tex_template=TexTemplateLibrary.ctex),
            Tex("Total Differential").shift(UP*1.5)
        ]


        # 创建替换后的公式
        new_formula = MathTex(
            r"\delta",#0
            r"Z",
            r"=\left( ",
            r"\frac{\partial }{\partial {\textcolor{yellow}{x}}}",
            r"Z",
            r"\right)",
            r"\delta",#6
            r"{\textcolor{yellow}{x}} + \left( ",
            r"\frac{\partial }{\partial {\textcolor{cyan}{y}}}",
            r"Z",
            r"\right)",
            r"\delta", #11
            r"{\textcolor{cyan}{y}}",tex_template=TexTemplateLibrary.ctex
        )

        self.play(FadeIn(par[1], shift=UP))
        self.play(Write(par[0]))
        self.wait(1)
        self.play(Circumscribe(par[0][0]),Circumscribe(par[0][6]),Circumscribe(par[0][11]))
        # 执行替换动画
        self.play(
            ReplacementTransform(par[0], new_formula))
        self.wait(2)
        self.play(#new_formula.animate.shift(UP*1.5),
                  #par[0].animate.shift(UP*1.5),
                  FadeOut(par[1]))
        
        L_formula =[ MathTex(
            r"\delta",
            r"L",
            r"=\left(",
            r" \frac{\partial }{\partial {\textcolor{yellow}{x}}}",
            r"L",
            r"\right)",
            r"\delta",
            r"{\textcolor{yellow}{x}} + \left( ",
            r"\frac{\partial }{\partial {\textcolor{cyan}{y}}}",
            r"L",
            r"\right)",
            r"\delta", 
            r"{\textcolor{cyan}{y}}",tex_template=TexTemplateLibrary.ctex
        ),
        MathTex(
            r"\delta",
            r"L",#1
            r"=\left( ",
            r"\frac{\partial }{\partial {\textcolor{yellow}{q}}}",#3
            r"L",#4
            r"\right)",
            r"\delta",
            r"{\textcolor{yellow}{q}} + \left( ",
            r"\frac{\partial }{\partial {\textcolor{cyan}{\dot{q}}}}",#8
            r"L",#9
            r"\right)",
            r"\delta", 
            r"{\textcolor{cyan}{\dot{q}}}",tex_template=TexTemplateLibrary.ctex
        ),
        
        ]
        self.play(Circumscribe(new_formula[1]),Circumscribe(new_formula[4]),Circumscribe(new_formula[9]))
        L=MathTex(r'L(\textcolor{yellow}{q}(t),\textcolor{cyan}{\dot{q}}(t))',tex_template=TexTemplateLibrary.ctex).shift(DOWN*2)
        self.play(ReplacementTransform(new_formula,L_formula[0]))
        self.wait()
        self.play(Write(L))
        self.wait()
        self.play(Circumscribe(L_formula[0][3]),Circumscribe(L_formula[0][8]))
        self.play(ReplacementTransform(L_formula[0],L_formula[1]))
        self.wait(2)

        L_formula[1].generate_target()
        L_formula[1].target.scale(0.75).shift(UP*1.5)
        action=MathTex(r"\ ",
                       r"S=",
                       r"\ ",
                       r" \int_{t_1}^{t_2}",
                       r" L",
                       r"(q ,\dot{q},t)\ ",
                       r"\mathrm{d}t")
        d_action=[MathTex(r"\delta",
                          r"S=  ",
                          r"\delta",
                          r"\int_{t_1}^{t_2}",
                          r" L",
                          r"(q,\dot{q},t)\ ",
                          r"\mathrm{d}t=0"),
                  MathTex(r"\delta",#0
                          r"S=  ",
                          r"\int_{t_1}^{t_2}",#2
                          r" \delta ",#3
                          r"L",#4
                          r"(q,\dot{q},t)\ ",
                          r"\mathrm{d}t=0")]
        self.play(FadeOut(L),MoveToTarget(L_formula[1]),Write(action))

        self.wait()
        self.play(Indicate(ds_0[1]))
        self.play(ReplacementTransform(action,d_action[1]))
        self.wait()
        self.play(d_action[1][3].animate.set_color(BLUE),
                  d_action[1][4].animate.set_color(BLUE),
                  d_action[1][5].animate.set_color(BLUE),
                  L_formula[1].animate.set_color(BLUE))
        self.wait(2)
        d_a=[
            MathTex(r"\delta S= \int_{t_1}^{t_2}",
            r"\frac{\partial L}{\partial {\textcolor{yellow}{q}}}\delta {\textcolor{yellow}{q}}  ",
            r"+",
            r"\frac{\partial L}{\partial {\textcolor{cyan}{\dot{q}}}} \delta {\textcolor{cyan}{\dot{q}}} \ \mathrm{d}t",
                          r"=0",tex_template=TexTemplateLibrary.ctex).scale(0.75),#0

            MathTex(r"\delta S= \int_{t_1}^{t_2}",
            r" \frac{\partial L}{\partial {\textcolor{yellow}{q}}}\delta {\textcolor{yellow}{q}}  ",
            r"\ \mathrm{d}t+\int_{t_1}^{t_2}",
            r"\frac{\partial L}{\partial {\textcolor{cyan}{\dot{q}}}} \delta {\textcolor{cyan}{\dot{q}}} \ \mathrm{d}t",
                          r"=0",tex_template=TexTemplateLibrary.ctex).scale(0.75),#1
            MathTex(r"\delta S=",
            r" \int_{t_1}^{t_2}",
            r" \frac{\partial L}{\partial {\textcolor{yellow}{q}}}\delta {\textcolor{yellow}{q}} ",
            r" \ \mathrm{d}t",
            r"+",
            r"\int_{t_1}^{t_2} ",
            r" \frac{\partial L}{\partial {\textcolor{cyan}{\dot{q}}}} \delta {\textcolor{cyan}{\dot{q}}} ",
            r"\ \mathrm{d}t",
                          r"=0",tex_template=TexTemplateLibrary.ctex).scale(0.75),#2
            MathTex(r"\delta S=",
            r" \int_{t_1}^{t_2}",
            r"\frac{\partial L}{\partial {\textcolor{yellow}{q}}}\delta {\textcolor{yellow}{q}}",
            r" \ \mathrm{d}t",
            r"+",
            r"\int_{t_1}^{t_2} ",
            r"\frac{\partial L}{\partial {\textcolor{cyan}{\dot{q}}}} \delta {\textcolor{cyan}{\dot{q}}} ",
            r"\ \mathrm{d}t",
            r"=0",tex_template=TexTemplateLibrary.ctex).scale(0.75),#3
            MathTex(r"\delta S=",
            r" \int_{t_1}^{t_2}",
            r"\frac{\partial L}{\partial {\textcolor{yellow}{q}}}\delta {\textcolor{yellow}{q}}",
            r" \ \mathrm{d}t",
            r"+",
            r"\int_{t_1}^{t_2} ",
            r"\frac{\partial L}{\partial {\textcolor{cyan}{\dot{q}}}} ",
            r"\delta {\textcolor{cyan}{\dot{q}}} ",################7
            r"\ \mathrm{d}t",
            r"=0",tex_template=TexTemplateLibrary.ctex).scale(0.75),#4
            MathTex(r"\delta S=",
            r" \int_{t_1}^{t_2}",
            r"\frac{\partial L}{\partial {\textcolor{yellow}{q}}}\delta {\textcolor{yellow}{q}}",
            r" \ \mathrm{d}t",
            r"+",
            r"\int_{t_1}^{t_2} ",
            r"\frac{\partial L}{\partial {\textcolor{cyan}{\dot{q}}}} ",
            r"\frac{\mathrm{d}}{\mathrm{d}t}(\delta \textcolor{yellow}{q})",
            r"\ \mathrm{d}t",
            r"=0",tex_template=TexTemplateLibrary.ctex).scale(0.75),#5

        ]
        d_act=[
            MathTex(r"\delta S=",
            r" \int_{t_1}^{t_2}",
            r"\frac{\partial L}{\partial {\textcolor{yellow}{q}}}\delta {\textcolor{yellow}{q}}",
            r" \ \mathrm{d}t",
            r"+",
            r"\int_{t_1}^{t_2} ",
            r"\frac{\partial L}{\partial {\textcolor{cyan}{\dot{q}}}} ",#6
            r"\mathrm{d}",#7
            r" (\delta \textcolor{yellow}{q})",#8
            r"=0",tex_template=TexTemplateLibrary.ctex).scale(0.75),#0
            MathTex(r"\delta S=",
            r" \int_{t_1}^{t_2}",
            r"\frac{\partial L}{\partial {\textcolor{yellow}{q}}}\delta {\textcolor{yellow}{q}}",
            r" \ \mathrm{d}t",
            r"+",
            r"\int_{t_1}^{t_2} ",
            r"-\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial L}{\partial {\textcolor{cyan}{\dot{q}}}}\delta \textcolor{yellow}{q} \ \mathrm{d}t",
            r"+\frac{\partial L}{\partial {\textcolor{cyan}{\dot{q}}}}",
            r"\delta \textcolor{yellow}{q} \bigg|_{t_1}^{t_2}",
            r"=0",tex_template=TexTemplateLibrary.ctex).scale(0.75),#1
            MathTex(r"\delta S=",
            r" \int_{t_1}^{t_2}",
            r"\frac{\partial L}{\partial {\textcolor{yellow}{q}}}\delta {\textcolor{yellow}{q}}",
            r" \ \mathrm{d}t",
            r"+",
            r"\int_{t_1}^{t_2} ",
            r"-\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial L}{\partial {\textcolor{cyan}{\dot{q}}}}\delta \textcolor{yellow}{q}  \ \mathrm{d}t",
            r"+\frac{\partial L}{\partial {\textcolor{cyan}{\dot{q}}}}",
            r" (\delta\textcolor{yellow}{q}(t_1)-\delta\textcolor{yellow}{q}(t_2)) ",#8
            r"=0",tex_template=TexTemplateLibrary.ctex).scale(0.75),#2
            MathTex(r"\delta S=",
            r" \int_{t_1}^{t_2}",
            r"\frac{\partial L}{\partial {\textcolor{yellow}{q}}}\delta {\textcolor{yellow}{q}}",
            r" \ \mathrm{d}t",
            r"+",
            r"\int_{t_1}^{t_2} ",
            r"-\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial L}{\partial {\textcolor{cyan}{\dot{q}}}} \delta \textcolor{yellow}{q} \ \mathrm{d}t",
            r"+",
            r"0",
            r"=0",tex_template=TexTemplateLibrary.ctex).scale(0.75),
            MathTex(r"\delta S=",
            r" \int_{t_1}^{t_2}",
            r"\frac{\partial L}{\partial {\textcolor{yellow}{q}}}\delta {\textcolor{yellow}{q}}",
            r" \ \mathrm{d}t",
            r"+",
            r"\int_{t_1}^{t_2} ",
            r"-\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial L}{\partial {\textcolor{cyan}{\dot{q}}}} \delta \textcolor{yellow}{q} \ \mathrm{d}t",
            r"+0=",
            r"0",tex_template=TexTemplateLibrary.ctex).scale(0.75),#4
            MathTex(r"\delta S=",
            r" \int_{t_1}^{t_2}",
            r"\frac{\partial L}{\partial {\textcolor{yellow}{q}}}\delta {\textcolor{yellow}{q}}",
            r" \ \mathrm{d}t",
            r"+",
            r"\int_{t_1}^{t_2} ",
            r"-\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial L}{\partial {\textcolor{cyan}{\dot{q}}}} \delta \textcolor{yellow}{q} \ \mathrm{d}t",
            r"=",
            r"0",tex_template=TexTemplateLibrary.ctex).scale(0.75),#5
        ]
        self.play(ReplacementTransform(d_action[-1],d_a[0]))
        self.play(FadeOut(L_formula[1]))
        parfra=Text("Partial Fraction").scale(0.75).shift(DOWN*2)
        self.wait()
        self.play(ReplacementTransform(d_a[0],d_a[1]))#+ int dt
        self.wait()
        self.add(d_a[4])
        self.remove(d_a[1])
        ddotq=MathTex(r'\delta\dot{q}=\delta\frac{\mathrm{d}}{\mathrm{d}t}q=\frac{\mathrm{d}}{\mathrm{d}t}\delta q').scale(0.75).shift(DOWN*2)
        self.wait()
        self.play(Write(ddotq))
        self.play(Circumscribe(d_a[4][7]))
        self.remove(d_a[3])
        self.play(ReplacementTransform(d_a[4],d_a[5]))
        self.wait()
        self.play(ReplacementTransform(d_a[5],d_act[0]),FadeOut(ddotq))
        self.play(Write(parfra))
        self.play(Indicate(d_act[0][6]),Indicate(d_act[0][7]),Indicate(d_act[0][8]))
        self.wait()
        self.play(ReplacementTransform(d_act[0],d_act[1]),ShrinkToCenter(parfra))
        deltaQ=MathTex(r'\delta q(t_1)=\delta q(t_2)=0').shift(DOWN*2)
        self.wait(1)
        self.play(ReplacementTransform(d_act[1],d_act[2]))
        self.wait(2)
        self.play(Write(deltaQ))
        self.play(Indicate(deltaQ),Circumscribe(d_act[2][8]))
        self.wait()
        self.play(ReplacementTransform(d_act[2],d_act[3]))
        self.add(d_act[4])
        self.remove(d_act[3])
        self.wait()
        self.play(Unwrite(deltaQ),ReplacementTransform(d_act[4],d_act[5]))
        main=[
            MathTex(r"\delta S=",
            r" \int_{t_1}^{t_2}",
            r"\frac{\partial L}{\partial {\textcolor{yellow}{q}}}\delta {\textcolor{yellow}{q}}",
            r" \ \mathrm{d}t+\int_{t_1}^{t_2} -",
            r"\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial L}{\partial {\textcolor{cyan}{\dot{q}}}} \delta \textcolor{yellow}{q} \ \mathrm{d}t",
            r"=0",tex_template=TexTemplateLibrary.ctex).scale(0.75),#0
            MathTex(r"\delta S=",
            r" \int_{t_1}^{t_2}",
            r"\frac{\partial L}{\partial {\textcolor{yellow}{q}}}\delta {\textcolor{yellow}{q}}",
            r" -",
            r"\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial L}{\partial {\textcolor{cyan}{\dot{q}}}} \delta \textcolor{yellow}{q} \ \mathrm{d}t",
            r"=0",tex_template=TexTemplateLibrary.ctex).scale(0.75),#1
            #NO CHANGE
            MathTex(r"\delta S=",
            r" \int_{t_1}^{t_2}",
            r"\frac{\partial L}{\partial {\textcolor{yellow}{q}}}",
            r" \delta {\textcolor{yellow}{q}}",#3
            r" -",
            r"\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial L}{\partial {\textcolor{cyan}{\dot{q}}}} ",
            r" \delta \textcolor{yellow}{q} ",#6
            r" \ \mathrm{d}t",
            r"=0",tex_template=TexTemplateLibrary.ctex).scale(0.75),#2
            #NO CHANGE
            MathTex(r"\delta S=",
            r" \int_{t_1}^{t_2}",
            r"\frac{\partial L}{\partial {\textcolor{yellow}{q}}} \delta {\textcolor{yellow}{q}}",#3
            r" -",
            r"\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial L}{\partial {\textcolor{cyan}{\dot{q}}}} ",
            r" \delta \textcolor{yellow}{q} ",#6
            r" \ \mathrm{d}t",
            r"=0",tex_template=TexTemplateLibrary.ctex).scale(0.75),#3
            MathTex(r"\delta S=",
            r" \int_{t_1}^{t_2}",
            r"\left( \frac{\partial L}{\partial {\textcolor{yellow}{q}}}",#3
            r" -",
            r"\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial L}{\partial {\textcolor{cyan}{\dot{q}}}} \right)",
            r" \delta \textcolor{yellow}{q} ",#6
            r" \ \mathrm{d}t",
            r"=0",tex_template=TexTemplateLibrary.ctex).scale(0.75),#4
            #NO CHANGE
            MathTex(r"\delta S",
            r"= \int_{t_1}^{t_2}\left( ",
            r"\frac{\partial L}{\partial {\textcolor{yellow}{q}}} -\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial L}{\partial {\textcolor{cyan}{\dot{q}}}} ",
            r"\right) \delta \textcolor{yellow}{q} ",#6
            r" \ \mathrm{d}t=",
            r"0",tex_template=TexTemplateLibrary.ctex).scale(0.75),#5
            #NO CHANGE
            MathTex(r"\delta S= \int_{t_1}^{t_2}\left(",
                    r"\frac{\partial L}{\partial {\textcolor{yellow}{q}}} -\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial L}{\partial {\textcolor{cyan}{\dot{q}}}} ",
                    r"\right) \delta \textcolor{yellow}{q} \ \mathrm{d}t",
                    r"=0",tex_template=TexTemplateLibrary.ctex).scale(0.75),#6
            MathTex(r"\ ",
                    r"\frac{\partial L}{\partial {\textcolor{yellow}{q}}} -\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial L}{\partial {\textcolor{cyan}{\dot{q}}}} ",
                   r"\ ",
                   r"=0",tex_template=TexTemplateLibrary.ctex).scale(0.75)#7
        ]
        EL=MathTex(r"\frac{\partial L}{\partial q} -\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial L}{\partial \dot{q}} ",
                   r"=0").scale(0.75).scale(1.5)

        self.add(main[0])
        self.remove(d_act[5])
        self.wait()
        self.play(ReplacementTransform(main[0],main[1]))
        self.add(main[2])
        self.remove(main[1])
        self.wait(0.5)
        self.play(Wiggle(main[2][3]),Wiggle(main[2][6]))
        self.add(main[3])
        self.remove(main[2])
        self.wait(0.5)
        self.play(ReplacementTransform(main[3],main[4]))
        self.add(main[5])
        self.remove(main[4])
        self.wait()
        self.play(ApplyWave(
            main[5][2],
        ))
        self.wait(2)
        self.add(main[6])
        self.remove(main[5])

        self.play(ReplacementTransform(main[6],EL))
        self.play(Circumscribe(EL))

        self.wait(3)
        self.play(FadeOut(EL,title,ds_0[1]))




class equiv(Scene):
    def construct(self):
        EL=MathTex(r"\frac{\partial }{\partial q} L -",r"\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial }{\partial \dot{q}} L ",#3
                   r"=0")
        l=[
            MathTex(r'L','\mathrm{\ about\ }',r'\vec{v}').scale(0.75).shift(UP*1.5),
            MathTex(r'L','\mathrm{\ about\ }',r'|\vec{v}|^2').scale(0.75).shift(UP*1.5),
        ]
        Lq=MathTex(r'L=L(\dot{q}^2)').scale(0.75).shift(UP*1.5+RIGHT*2)
        title=Title("Proof of Equivalence with the Newtonian")
        self.play(Write(title))
        self.play(FadeIn(EL))
        self.wait()
        self.play(Write(l[0]))
        self.wait()
        self.play(ReplacementTransform(l[0],l[1]))
        self.wait(0.5)
        self.play(l[1].animate.shift(LEFT*2),Write(Lq))
        self.wait()
        Lq.generate_target()
        Lq.target.shift(LEFT*3.5)
        sth0=MathTex(r"\longrightarrow \quad \frac{\partial }{\partial q} L=0").scale(0.75).shift(UP*1.5+RIGHT*1.5)
        self.play(FadeOut(l[1]),MoveToTarget(Lq),GrowFromEdge(sth0,LEFT))
        EL1=MathTex(r"\ ",r"\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial }{\partial \dot{q}} L ",#3
                   r"=0")
        self.wait()
        self.play(ReplacementTransform(EL,EL1))
        EL11=MathTex(r"\ \frac{\mathrm{d}}{\mathrm{d}t}",r"\frac{\partial }{\partial \dot{q}} L =",#3
                   r"0")
        self.add(EL11).remove(EL1)
        EL2=MathTex(r"\ ",r"\frac{\partial }{\partial \dot{q}} L= ",#3
                   r"\mathrm{const.}")
        self.wait()
        self.play(ReplacementTransform(EL11,EL2),FadeOut(Lq,sth0))
        downarrow=MathTex(r'\Downarrow ').scale(1.5)
        vcons=MathTex(r'\dot{q}=\mathrm{const.}').shift(DOWN*1.5)
        self.wait()
        self.play(EL2.animate.shift(UP*1.25),GrowFromCenter(downarrow),GrowFromEdge(vcons,UP))
        self.wait()
        galileo=Text('ONLY in inertial reference frame',color=YELLOW).scale(0.5).shift(DOWN*2.25)
        self.play(Write(galileo))
        self.wait(2)
        self.play(FadeOut(galileo,EL2,vcons,downarrow))
        v_e=MathTex(r"\dot{q}\longrightarrow q'= \dot{q}+\varepsilon").shift(UP*1.5)
        L_e=MathTex(r"L(\dot{q}^2)\longrightarrow L(\dot{q}'^2)")
        L_E0=MathTex(r"L(\dot{q}'^2)=",r"L((\dot{q}+\varepsilon)^2)").shift(DOWN*1.5)
        L_E1=MathTex(r"L(\dot{q}'^2)=",r"L(\dot{q}^2+2\dot{q}\varepsilon+\varepsilon^2)").shift(DOWN*1.5)
        L_E2=MathTex(r"L(\dot{q}'^2)=",r"L(\dot{q}^2)+2\frac{\partial L}{\partial \dot{q}^2} \dot{q}\varepsilon+O(\dot{q},\varepsilon)").shift(DOWN*1.5)
        L_E21=MathTex(r"L(\dot{q}'^2)=",r"L(\dot{q}^2)+2\frac{\partial L}{\partial \dot{q}^2}",r" \dot{q}\varepsilon+O(\dot{q},\varepsilon)").shift(DOWN*1.5)
        L_E3=MathTex(r"L(\dot{q}'^2)=",r"L(\dot{q}^2)+2\frac{\partial L}{\partial \dot{q}^2} ",r"\dot{q}\varepsilon").shift(DOWN*1.5)
        L_E31=MathTex(r"L(\dot{q}'^2)=",r"L(\dot{q}^2)+",r"2\frac{\partial L}{\partial \dot{q}^2} \dot{q}\varepsilon").shift(DOWN*1.5)
        L_E4=MathTex(r"2\frac{\partial L}{\partial \dot{q}^2} \dot{q}\varepsilon",r"\propto \dot{q}")
        L_E5=MathTex(r"\frac{\partial L}{\partial \dot{q}^2} ",r"=\mathrm{const.}")
        L_E6=MathTex(r"L_{\dot{q}}=\frac{1}{2}m",r"\dot{q}^2")
        L_E7=MathTex(r"L_{\dot{q}}=\frac{1}{2}m",r"v^2")
        self.play(Write(v_e))
        self.wait()
        self.play(Write(L_e))
        self.wait()
        self.play(Write(L_E0),FadeOut(v_e,L_e))  
        self.wait()
        self.play(ReplacementTransform(L_E0,L_E1)) 
        self.wait()
        self.play(ReplacementTransform(L_E1,L_E2))  
        self.add(L_E21).remove(L_E2)   
        self.wait()
        self.play(ReplacementTransform(L_E21,L_E3))
        self.add(L_E31).remove(L_E3)
        self.wait()
        self.play(Indicate(L_E31[-1]))
        self.play(FadeOut(L_E31[0],L_E31[1]),ReplacementTransform(L_E31[-1],L_E4))     
        self.wait()
        self.play(ReplacementTransform(L_E4,L_E5))
        self.wait()
        self.play(ReplacementTransform(L_E5,L_E6))
        self.wait()
        self.play(ReplacementTransform(L_E6,L_E7))
        ggl=Text('ONLY in free system',color=YELLOW).scale(0.5).shift(DOWN*2.25)
        self.play(Write(ggl))

        self.wait(2)
        self.play(FadeOut(ggl,L_E7))

        el=MathTex(r"\frac{\partial }{\partial q} L_{q} ",r"-",r"\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial }{\partial \dot{q}} L_{\dot{q}} =0")
        el1=MathTex(r"\frac{\partial }{\partial q} L_{q} ",r"=",r"\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial }{\partial \dot{q}} L_{\dot{q}} ")
        el11=MathTex(r"\frac{\partial }{\partial q} L_{q} ",r"=",r"\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial }{\partial \dot{q}}",r" L_{\dot{q}} ")
        el2=MathTex(r"\frac{\partial }{\partial q} L_{q} ",r"=",r"\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial }{\partial \dot{q}}",r" \left(\frac{1}{2}m \dot{q}^2\right)")
        el21=MathTex(r"\frac{\partial }{\partial q} L_{q} ",r"=",r"\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial }{\partial \dot{q}} \left(\frac{1}{2}m\dot{q}^2\right)")
        el3=MathTex(r"\frac{\partial }{\partial q} L_{q} ",r"=",r"m\frac{\mathrm{d}q}{\mathrm{d}t} ")
        el31=MathTex(r"\frac{\partial }{\partial q} ",r"L_{q} ",r"=m\frac{\mathrm{d}q}{\mathrm{d}t}")
        el4=MathTex(r"-\frac{\partial }{\partial q} ",r"V",r"=m\frac{\mathrm{d}q}{\mathrm{d}t} ")

        self.play(Write(el))
        self.wait()
        self.play(ReplacementTransform(el,el1))
        L_E6.shift(DOWN*1.5) #=MathTex(r"L_{\dot{q}}=\frac{1}{2}m",r"\dot{q}^2")

        self.wait()
        self.play(Write(L_E6))
        self.play(Circumscribe(el1[-1]))
        self.remove(el1).add(el11)
        self.wait()
        self.play(ReplacementTransform(el11,el2),FadeOut(L_E6))
        self.remove(el2).add(el21)
        self.wait()
        self.play(ReplacementTransform(el21,el3))

        energy=MathTex(r'[L]=[Energy]=[M][l]^2[T]^{-2}').shift(DOWN*1.5)
        self.wait()
        self.play(Write(energy))
        self.play(Indicate(el3[0]))
        self.remove(el3).add(el31)
        self.wait()
        self.play(ReplacementTransform(el31,el4),FadeOut(energy))
        self.wait()
        da=MathTex(r'\Downarrow').shift(UP*0.75)
        fma=MathTex(r'F=ma').shift(UP*1.5)

        self.play(TransformFromCopy(el4,da),TransformFromCopy(el4,fma))
        self.wait()
        da1=MathTex(r'\Downarrow').shift(UP*-0.75)
        fma1=MathTex(r'L_q=-V').shift(UP*-1.5)

        self.play(TransformFromCopy(el4,da1),TransformFromCopy(el4,fma1))
        ltv=MathTex(r'L=T-V').scale(2)

        self.wait(4)
        self.play(FadeOut(da,da1,fma,fma1,el4),FadeIn(ltv))
        self.play(Indicate(ltv,run_time=4))
        self.wait()
        ln=MathTex(r'\mathrm{Lagrangian}\sim\mathrm{Newtonian}').shift(DOWN*1.5)
        self.play(ltv.animate.shift(UP),GrowFromEdge(ln,UP))
        self.wait(4)
        self.play(FadeOut(ltv,ln,title))
        self.wait()




class TOTAL(Scene):
    def construct(self):
        tex0 = MathTex(r'''
            \delta S&=0\\
            &=\delta \int ^{t_2}_{t_1} \mathcal{L} (q(t),\dot{q}(t) )\ \mathrm{d}t\\
            &=\int ^{t_2}_{t_1}\delta  \mathcal{L} (q(t),\dot{q}(t) )\ \mathrm{d}t\\
            &=\int ^{t_2}_{t_1} \left( \frac{\partial \mathcal{L} }{\partial q} \delta q +\frac{\partial \mathcal{L} }{\partial\dot{q}  } \delta \dot{q}  \right )\ \mathrm{d}t\\
            &=\int ^{t_2}_{t_1} \left( \frac{\partial \mathcal{L} }{\partial q} \delta q \right)\ \mathrm{d}t+\int ^{t_2}_{t_1} \left( \frac{\partial \mathcal{L} }{\partial\dot{q}  } \delta \dot{q}  \right )\ \mathrm{d}t\\
            &=\int ^{t_2}_{t_1} \left( \frac{\partial \mathcal{L} }{\partial q} \delta q \right)\ \mathrm{d}t+\int ^{t_2}_{t_1} \left( \frac{\partial \mathcal{L} }{\partial\dot{q}  } \delta \frac{\mathrm{d} }{\mathrm{d} t} q  \right )\ \mathrm{d}t\\

            ''',color=GREEN_B, font_size=25).shift(LEFT*4+UP)
        tex1 = MathTex(r'''
            &=\int ^{t_2}_{t_1} \left( \frac{\partial \mathcal{L} }{\partial q} \delta q \right)\ \mathrm{d}t+\int ^{t_2}_{t_1} \left( \frac{\partial \mathcal{L} }{\partial\dot{q}  }  \frac{\mathrm{d} }{\mathrm{d} t}[\delta q ] \right )\ \mathrm{d}t\\
            &=\int ^{t_2}_{t_1} \left( \frac{\partial \mathcal{L} }{\partial q} \delta q \right)\ \mathrm{d}t+\left( \frac{\partial \mathcal{L} }{\partial\dot{q}  } \delta q  \right )^{t_2}_{t_1}- \int ^{t_2}_{t_1} \left( \frac{\mathrm{d} }{\mathrm{d} t}\frac{\partial \mathcal{L} }{\partial\dot{q}  }  \delta q  \right )\ \mathrm{d}t\\
            &=\int ^{t_2}_{t_1} \left( \frac{\partial \mathcal{L} }{\partial q} \delta q \right)\ \mathrm{d}t+\left( \frac{\partial \mathcal{L} }{\partial\dot{q}  } [\delta q(t_2)-\delta q(t_1) ] \right )- \int ^{t_2}_{t_1} \left( \frac{\mathrm{d} }{\mathrm{d} t}\frac{\partial \mathcal{L} }{\partial\dot{q}  }  \delta q  \right )\ \mathrm{d}t\\
            &=\int ^{t_2}_{t_1} \left( \frac{\partial \mathcal{L} }{\partial q} \delta q \right)\ \mathrm{d}t- \int ^{t_2}_{t_1} \left( \frac{\mathrm{d} }{\mathrm{d} t}\frac{\partial \mathcal{L} }{\partial\dot{q}  }  \delta q  \right )\ \mathrm{d}t\\
            &=\int ^{t_2}_{t_1} \left( \frac{\partial \mathcal{L} }{\partial q} -  \frac{\mathrm{d} }{\mathrm{d} t}\frac{\partial \mathcal{L} }{\partial\dot{q}  } \right )\delta q\ \mathrm{d}t
            ''', color=BLUE_B,font_size=25).shift(LEFT*-3+UP)
        
        tex=MathTex(r'\frac{\partial \mathcal{L} }{\partial q} =  \frac{\mathrm{d} }{\mathrm{d} t}\frac{\partial \mathcal{L} }{\partial\dot{q}  }',
                    color=YELLOW).scale(0.75).shift(DOWN*2)
        TEX=SurroundingRectangle(tex,color=YELLOW)
        self.play(Write(tex0),Write(tex1),run_time=3)
        self.play(FadeIn(tex),Create(TEX))
        self.wait(3)
        self.play(FadeOut(tex0,tex1,tex,TEX))
        



class zhuangbi(Scene):
    def construct(self):
        chn = Paragraph(
            "The loathsome mask has fallen, the man remains Sceptreless, free, ",
            "uncircumscribed, but man equal, unclassed, tribeless, and nationless, ",
            "Exempt from awe, worship, degree, the king over himself.",
            "",
            "苍天，你还有秘密吗?",
            "人类已揭开面纱，一切都显露无遗。",
            alignment='left',
            line_spacing=1.25
        ).scale(0.5).shift(UP*0.75)
        
        # 将段落所有字符提取并作为整体设置渐变
        all_chars = VGroup(*[char for line in chn for char in line])
        all_chars.set_color_by_gradient(YELLOW, BLUE)
        # 通过多次描边模拟粗体效果
        #chn.set_stroke(width=0.5, color=chn.get_color(), opacity=1)
        #chn.set_stroke(width=0.5, color=chn.get_color(), opacity=1, background=True)
        
        ch = Text(
            "Prometheus Unbound, Ack Lynch", 
            t2s={"Prometheus Unbound": ITALIC},color=BLUE
        ).scale(0.5).shift(DOWN*2.25+RIGHT*3)
        
        self.play(Write(chn[:3]), run_time=3)
        self.play(Write(chn[-2:]), run_time=2)
        self.wait()
        self.play(Write(ch))
        self.wait(3)
        self.play(FadeOut(chn,ch))