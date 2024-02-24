from manim import *
import numpy as np

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
