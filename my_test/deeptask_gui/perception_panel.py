# -*- coding: utf-8 -*-

import wx.media
import time
import roslib
import rospy
import threading
import wx
import etc_functions as ef

roslib.load_manifest('rospy')
roslib.load_manifest('sensor_msgs')

CUSTOM_COLOR_RED = '#df0a4b'
CUSTOM_COLOR_GREEN = '#2aaa67'
CUSTOM_COLOR_DARK_GRAY = '#363b41'
CUSTOM_COLOR_LIGHT_GRAY = '#696c70'


class PerceptionPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # self.SetBackgroundColour(wx.NullColour)
        self.SetBackgroundColour(wx.WHITE)
        main_sizer = wx.GridBagSizer(hgap=5, vgap=-1)

        title_panel = ef.BlockWindow(self, ID=-1, label="Perception Status", size=(640, 50), style=wx.ALL, label_color=wx.WHITE, bg_color=CUSTOM_COLOR_DARK_GRAY, font_set=[18, wx.NORMAL, wx.NORMAL, wx.BOLD])

        title_pi = ef.BlockWindow(self, ID=-1, label="Personal Information", style=wx.ALL, label_color=wx.WHITE, bg_color=CUSTOM_COLOR_LIGHT_GRAY, font_set=[14, wx.DEFAULT, wx.NORMAL, wx.NORMAL])

        sizer_pi_label = wx.BoxSizer(wx.HORIZONTAL)
        sizer_pi_label.Add(ef.BlockWindow(self, label="Name", label_color=wx.BLACK, bg_color=wx.WHITE), proportion=1, flag=wx.EXPAND)
        sizer_pi_label.Add(ef.BlockWindow(self, label="Age", label_color=wx.BLACK, bg_color=wx.WHITE), proportion=1, flag=wx.EXPAND)
        sizer_pi_label.Add(ef.BlockWindow(self, label="Gender", label_color=wx.BLACK, bg_color=wx.WHITE), proportion=1, flag=wx.EXPAND)

        sizer_pi_data = wx.BoxSizer(wx.HORIZONTAL)
        self.pi_data_name = ef.BlockWindow(self, label="", style=wx.ALL, size=(100, 50), label_color=wx.BLACK, bg_color=wx.WHITE)
        self.pi_data_age = ef.BlockWindow(self, label="", style=wx.ALL, size=(100, 50), label_color=wx.BLACK, bg_color=wx.WHITE)
        self.pi_data_gender = ef.BlockWindow(self, label="", style=wx.ALL, size=(100, 50), label_color=wx.BLACK, bg_color=wx.WHITE)
        sizer_pi_data.Add(self.pi_data_name, proportion=1, flag=wx.EXPAND)
        sizer_pi_data.Add(self.pi_data_age, proportion=1, flag=wx.EXPAND)
        sizer_pi_data.Add(self.pi_data_gender, proportion=1, flag=wx.EXPAND)

        title_motion = ef.BlockWindow(self, ID=-1, label="Motion", style=wx.ALL, label_color=wx.WHITE, bg_color=CUSTOM_COLOR_LIGHT_GRAY, font_set=[14, wx.DEFAULT, wx.NORMAL, wx.NORMAL])

        sizer_motion_label = wx.BoxSizer(wx.HORIZONTAL)
        sizer_motion_label.Add(ef.BlockWindow(self, label="attention", label_color=wx.BLACK, bg_color=wx.WHITE), proportion=1, flag=wx.EXPAND)
        sizer_motion_label.Add(ef.BlockWindow(self, label="encouragement", label_color=wx.BLACK, bg_color=wx.WHITE), proportion=1, flag=wx.EXPAND)
        sizer_motion_label.Add(ef.BlockWindow(self, label="greeting", label_color=wx.BLACK, bg_color=wx.WHITE), proportion=1, flag=wx.EXPAND)

        sizer_motion_led = wx.BoxSizer(wx.HORIZONTAL)
        self.motion_led_attention = ef.CircleWindow(self, ID=-1, color=CUSTOM_COLOR_RED)
        self.motion_led_encouragement = ef.CircleWindow(self, ID=-1, color=CUSTOM_COLOR_RED)
        self.motion_led_greeting = ef.CircleWindow(self, ID=-1, color=CUSTOM_COLOR_RED)
        sizer_motion_led.Add(self.motion_led_attention, proportion=1, flag=wx.EXPAND)
        sizer_motion_led.Add(self.motion_led_encouragement, proportion=1, flag=wx.EXPAND)
        sizer_motion_led.Add(self.motion_led_greeting, proportion=1, flag=wx.EXPAND)

        sizer_motion_data = wx.BoxSizer(wx.HORIZONTAL)
        self.motion_data_attention = ef.BlockWindow(self, label="", style=wx.ALL, size=(100, 50), label_color=wx.BLACK, bg_color=wx.WHITE)
        self.motion_data_encouragement = ef.BlockWindow(self, label="", style=wx.ALL, size=(100, 50), label_color=wx.BLACK, bg_color=wx.WHITE)
        self.motion_data_greeting = ef.BlockWindow(self, label="", style=wx.ALL, size=(100, 50), label_color=wx.BLACK, bg_color=wx.WHITE)
        sizer_motion_data.Add(self.motion_data_attention, proportion=1, flag=wx.EXPAND)
        sizer_motion_data.Add(self.motion_data_encouragement, proportion=1, flag=wx.EXPAND)
        sizer_motion_data.Add(self.motion_data_greeting, proportion=1, flag=wx.EXPAND)



        title_rl = ef.BlockWindow(self, ID=-1, label="Relative Location", size=(640, 30), style=wx.ALL, label_color=wx.WHITE, bg_color=CUSTOM_COLOR_LIGHT_GRAY, font_set=[14, wx.DEFAULT, wx.NORMAL, wx.NORMAL])

        sizer_rl_label = wx.BoxSizer(wx.HORIZONTAL)
        sizer_rl_label.Add(ef.BlockWindow(self, label="near_robot", label_color=wx.BLACK, bg_color=wx.WHITE), proportion=1, flag=wx.EXPAND)
        sizer_rl_label.Add(ef.BlockWindow(self, label="near_signboard", label_color=wx.BLACK, bg_color=wx.WHITE), proportion=1, flag=wx.EXPAND)
        sizer_rl_label.Add(ef.BlockWindow(self, label="near_restroom", label_color=wx.BLACK, bg_color=wx.WHITE), proportion=1, flag=wx.EXPAND)

        sizer_rl_led = wx.BoxSizer(wx.HORIZONTAL)
        self.rl_led_is_near_robot = ef.CircleWindow(self, ID=-1, color=CUSTOM_COLOR_RED)
        self.rl_led_is_near_signboard = ef.CircleWindow(self, ID=-1, color=CUSTOM_COLOR_RED)
        self.rl_led_is_near_restroom = ef.CircleWindow(self, ID=-1, color=CUSTOM_COLOR_RED)
        sizer_rl_led.Add(self.rl_led_is_near_robot, proportion=1, flag=wx.EXPAND)
        sizer_rl_led.Add(self.rl_led_is_near_signboard, proportion=1, flag=wx.EXPAND)
        sizer_rl_led.Add(self.rl_led_is_near_restroom, proportion=1, flag=wx.EXPAND)

        title_sd = ef.BlockWindow(self, ID=-1, label="Social Distance", style=wx.ALL, label_color=wx.WHITE, bg_color=CUSTOM_COLOR_LIGHT_GRAY, font_set=[14, wx.DEFAULT, wx.NORMAL, wx.NORMAL])

        sizer_sd_label = wx.BoxSizer(wx.HORIZONTAL)
        sizer_sd_label.Add(ef.BlockWindow(self, label="public_space", label_color=wx.BLACK, bg_color=wx.WHITE), proportion=1, flag=wx.EXPAND)
        sizer_sd_label.Add(ef.BlockWindow(self, label="social_space", label_color=wx.BLACK, bg_color=wx.WHITE), proportion=1, flag=wx.EXPAND)
        sizer_sd_label.Add(ef.BlockWindow(self, label="personal_space", label_color=wx.BLACK, bg_color=wx.WHITE), proportion=1, flag=wx.EXPAND)
        sizer_sd_label.Add(ef.BlockWindow(self, label="intimate_space", label_color=wx.BLACK, bg_color=wx.WHITE), proportion=1, flag=wx.EXPAND)

        sizer_sd_led = wx.BoxSizer(wx.HORIZONTAL)
        self.sd_led_public_space = ef.CircleWindow(self, ID=-1, color=CUSTOM_COLOR_RED)
        self.sd_led_social_space = ef.CircleWindow(self, ID=-1, color=CUSTOM_COLOR_RED)
        self.sd_led_personal_space = ef.CircleWindow(self, ID=-1, color=CUSTOM_COLOR_RED)
        self.sd_led_intimate_space = ef.CircleWindow(self, ID=-1, color=CUSTOM_COLOR_RED)
        sizer_sd_led.Add(self.sd_led_public_space, proportion=1, flag=wx.EXPAND)
        sizer_sd_led.Add(self.sd_led_social_space, proportion=1, flag=wx.EXPAND)
        sizer_sd_led.Add(self.sd_led_personal_space, proportion=1, flag=wx.EXPAND)
        sizer_sd_led.Add(self.sd_led_intimate_space, proportion=1, flag=wx.EXPAND)

        title_issp = ef.BlockWindow(self, ID=-1, label="isSpeaking", style=wx.ALL, label_color=wx.WHITE, bg_color=CUSTOM_COLOR_LIGHT_GRAY, font_set=[14, wx.DEFAULT, wx.NORMAL, wx.NORMAL])
        sizer_issp_label = wx.BoxSizer(wx.HORIZONTAL)
        sizer_issp_label.Add(ef.BlockWindow(self, label="human", label_color=wx.BLACK, bg_color=wx.WHITE), proportion=1, flag=wx.EXPAND)
        sizer_issp_label.Add(ef.BlockWindow(self, label="robot", label_color=wx.BLACK, bg_color=wx.WHITE), proportion=1, flag=wx.EXPAND)
        sizer_issp_label.Add(ef.BlockWindow(self, label="reply_to_Robot", label_color=wx.BLACK, bg_color=wx.WHITE), proportion=1, flag=wx.EXPAND)

        sizer_issp_led = wx.BoxSizer(wx.HORIZONTAL)
        self.issp_led_is_speaking_human = ef.CircleWindow(self, ID=-1, color=CUSTOM_COLOR_RED)
        self.issp_led_is_speaking_robot = ef.CircleWindow(self, ID=-1, color=CUSTOM_COLOR_RED)
        self.issp_led_reply_to_robot = ef.CircleWindow(self, ID=-1, color=CUSTOM_COLOR_RED)
        sizer_issp_led.Add(self.issp_led_is_speaking_human, proportion=1, flag=wx.EXPAND)
        sizer_issp_led.Add(self.issp_led_is_speaking_robot, proportion=1, flag=wx.EXPAND)
        sizer_issp_led.Add(self.issp_led_reply_to_robot, proportion=1, flag=wx.EXPAND)

        title_per = ef.BlockWindow(self, ID=-1, label="User Personality", style=wx.ALL, label_color=wx.WHITE, bg_color=CUSTOM_COLOR_LIGHT_GRAY, font_set=[14, wx.DEFAULT, wx.NORMAL, wx.NORMAL])

        sizer_per_label = wx.BoxSizer(wx.HORIZONTAL)
        sizer_per_label.Add(ef.BlockWindow(self, label="Openness", label_color=wx.BLACK, bg_color=wx.WHITE), proportion=1, flag=wx.EXPAND)
        sizer_per_label.Add(ef.BlockWindow(self, label="Conscientiousness", label_color=wx.BLACK, bg_color=wx.WHITE), proportion=1, flag=wx.EXPAND)
        sizer_per_label.Add(ef.BlockWindow(self, label="Extraversion", label_color=wx.BLACK, bg_color=wx.WHITE), proportion=1, flag=wx.EXPAND)
        sizer_per_label.Add(ef.BlockWindow(self, label="Agreeableness", label_color=wx.BLACK, bg_color=wx.WHITE), proportion=1, flag=wx.EXPAND)
        sizer_per_label.Add(ef.BlockWindow(self, label="Neuroticism", label_color=wx.BLACK, bg_color=wx.WHITE), proportion=1, flag=wx.EXPAND)

        sizer_per_guage = wx.BoxSizer(wx.HORIZONTAL)
        self.per_gauge_o = wx.Gauge(self, range=3, size=(100, 60), style=wx.GA_VERTICAL)
        self.per_gauge_o.SetValue(1)
        self.per_gauge_o.SetBackgroundColour(wx.WHITE)

        self.per_gauge_c = wx.Gauge(self, range=3, size=(100, 60), style=wx.GA_VERTICAL)
        self.per_gauge_c.SetValue(2)
        self.per_gauge_c.SetBackgroundColour(wx.WHITE)

        self.per_gauge_e = wx.Gauge(self, range=3, size=(100, 60), style=wx.GA_VERTICAL)
        self.per_gauge_e.SetValue(3)
        self.per_gauge_e.SetBackgroundColour(wx.WHITE)

        self.per_gauge_a = wx.Gauge(self, range=3, size=(100, 60), style=wx.GA_VERTICAL)
        self.per_gauge_a.SetValue(1)
        self.per_gauge_a.SetBackgroundColour(wx.WHITE)

        self.per_gauge_n = wx.Gauge(self, range=3, size=(100, 60), style=wx.GA_VERTICAL)
        self.per_gauge_n.SetValue(2)
        self.per_gauge_n.SetBackgroundColour(wx.WHITE)

        sizer_per_guage.Add(self.per_gauge_o, proportion=1, flag=wx.EXPAND)
        sizer_per_guage.Add(self.per_gauge_c, proportion=1, flag=wx.EXPAND)
        sizer_per_guage.Add(self.per_gauge_e, proportion=1, flag=wx.EXPAND)
        sizer_per_guage.Add(self.per_gauge_a, proportion=1, flag=wx.EXPAND)
        sizer_per_guage.Add(self.per_gauge_n, proportion=1, flag=wx.EXPAND)

        main_sizer.Add(title_panel, pos=(0, 0), span=(1, 5), flag=wx.EXPAND)

        main_sizer.Add(title_pi, pos=(2, 0), span=(1, 5), flag=wx.EXPAND)
        main_sizer.Add(sizer_pi_label, pos=(3, 0), span=(1, 5), flag=wx.EXPAND)
        main_sizer.Add(sizer_pi_data, pos=(4, 0), span=(1, 5), flag=wx.EXPAND)

        main_sizer.Add(title_motion, pos=(6, 0), span=(1, 5), flag=wx.EXPAND)
        main_sizer.Add(sizer_motion_label, pos=(7, 0), span=(1, 5), flag=wx.EXPAND)
        main_sizer.Add(sizer_motion_led, pos=(8, 0), span=(1, 5), flag=wx.EXPAND)
        main_sizer.Add(sizer_motion_data, pos=(9, 0), span=(1, 5), flag=wx.EXPAND)

        main_sizer.Add(title_rl, pos=(11, 0), span=(1, 5), flag=wx.EXPAND)
        main_sizer.Add(sizer_rl_label, pos=(12, 0), span=(1, 5), flag=wx.EXPAND)
        main_sizer.Add(sizer_rl_led, pos=(13, 0), span=(1, 5), flag=wx.EXPAND)

        main_sizer.Add(title_sd, pos=(15, 0), span=(1, 5), flag=wx.EXPAND)
        main_sizer.Add(sizer_sd_label, pos=(16, 0), span=(1, 5), flag=wx.EXPAND)
        main_sizer.Add(sizer_sd_led, pos=(17, 0), span=(1, 5), flag=wx.EXPAND)

        main_sizer.Add(title_issp, pos=(19, 0), span=(1, 5), flag=wx.EXPAND)
        main_sizer.Add(sizer_issp_label, pos=(20, 0), span=(1, 5), flag=wx.EXPAND)
        main_sizer.Add(sizer_issp_led, pos=(21, 0), span=(1, 5), flag=wx.EXPAND)

        main_sizer.Add(title_per, pos=(23, 0), span=(1, 5), flag=wx.EXPAND)
        main_sizer.Add(sizer_per_label, pos=(24, 0), span=(1, 5), flag=wx.EXPAND)
        main_sizer.Add(sizer_per_guage, pos=(25, 0), span=(1, 5), flag=wx.EXPAND)

        main_sizer.AddGrowableCol(0)

        self.SetSizer(main_sizer)
        self.Fit()
