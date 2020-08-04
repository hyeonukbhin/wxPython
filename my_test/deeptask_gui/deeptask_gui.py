#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import wx.media
import time
import roslib
from sensor_msgs.msg import Image
import rospy
from audio_msgs.msg import AudioData, FeatureData
import numpy as np
import threading
import wx

import image_voice_panel as ivp
import perception_panel as pp
import dialog_panel as dp
import etc_functions as ef

roslib.load_manifest('rospy')
roslib.load_manifest('sensor_msgs')

VOICE_SCALE = "linear"  # or "db"
CUSTOM_COLOR_RED = '#df0a4b'
CUSTOM_COLOR_GREEN = '#2aaa67'
CUSTOM_COLOR_DARK_GRAY = '#363b41'
CUSTOM_COLOR_LIGHT_GRAY = '#696c70'
CUSTOM_COLOR_VERY_LIGHT_GRAY = '#f0f0f0'
CUSTOM_COLOR_BLUE = '#385cf4'

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class MainFrame(wx.Frame):
    def __init__(self, parent, id, title):
        # SETUP
        wx.Frame.__init__(self, parent, id, title=title, size=(1980, 950))
        self.top_panel = TopPanel(self)


class TopPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        _sizer = wx.BoxSizer(wx.HORIZONTAL)
        # voice_scale = "linear"
        self.image_voice_panel = ivp.ImageVoicePanel(self, voice_scale=VOICE_SCALE)
        _sizer.Add(self.image_voice_panel, proportion=1, flag=wx.EXPAND)

        self.perception_panel = pp.PerceptionPanel(self)
        # self.perception_panel.SetBackgroundColour(CUSTOM_COLOR_VERY_LIGHT_GRAY)
        _sizer.Add(self.perception_panel, proportion=1, flag=wx.EXPAND)

        self.dialog_panel = dp.DialogPanel(self)
        _sizer.Add(self.dialog_panel, proportion=1, flag=wx.EXPAND)

        self.SetSizer(_sizer)


class ParameterGetter(threading.Thread):
    def __init__(self, frame):
        threading.Thread.__init__(self)
        self.frame = frame

    def run(self):

        once_flag = 0
        while True:
            try:
                update_function = self.frame.top_panel.perception_panel
                # Personal Information
                human_name = ef.get_param("/perception/human_name/data")
                handle_param(update_function.pi_data_name.UpdateLabel, human_name)
                human_age = ef.get_param("/perception/human_age/data")
                handle_param(update_function.pi_data_age.UpdateLabel, human_age)
                human_gender = ef.get_param("/perception/human_gender/data")
                handle_param(update_function.pi_data_gender.UpdateLabel, human_gender)

                # Motion
                # state 바꿔서 문제 없게 한다음에 이부분 다시 수정
                human_motion = ef.get_param("/perception/human_motion")
                attention = human_motion["attention"]
                if attention == "None": #이런애들 애초에 State에서 없게 하자 None 없이
                    handle_param(update_function.motion_data_attention.UpdateLabel, "")
                else:
                    handle_param(update_function.motion_data_attention.UpdateLabel, attention)

                if attention == "gaze":
                    handle_param(update_function.motion_led_attention.UpdateColor, CUSTOM_COLOR_BLUE)
                else:
                    handle_param(update_function.motion_led_attention.UpdateColor, CUSTOM_COLOR_VERY_LIGHT_GRAY)

                encouragement = human_motion["encouragement"]
                if encouragement == "None":
                    handle_param(update_function.motion_data_encouragement.UpdateLabel, "")
                else:
                    handle_param(update_function.motion_data_encouragement.UpdateLabel, encouragement)


                if encouragement == "v":
                    handle_param(update_function.motion_led_encouragement.UpdateColor, CUSTOM_COLOR_BLUE)
                else:
                    handle_param(update_function.motion_led_encouragement.UpdateColor, CUSTOM_COLOR_VERY_LIGHT_GRAY)

                greeting = human_motion["greeting"]
                if greeting == "None":
                    handle_param(update_function.motion_data_greeting.UpdateLabel, "")
                else:
                    handle_param(update_function.motion_data_greeting.UpdateLabel, greeting)
                if greeting == "waving_hand":
                    handle_param(update_function.motion_led_greeting.UpdateColor, CUSTOM_COLOR_BLUE)
                else:
                    handle_param(update_function.motion_led_greeting.UpdateColor, CUSTOM_COLOR_VERY_LIGHT_GRAY)

                # Relative Location
                human_relative_location = ef.get_param("/perception/human_relative_location")
                is_near_restroom = human_relative_location["is_near_restroom"]
                if is_near_restroom is True:
                    handle_param(update_function.rl_led_is_near_restroom.UpdateColor, CUSTOM_COLOR_BLUE)
                else:
                    handle_param(update_function.rl_led_is_near_restroom.UpdateColor, CUSTOM_COLOR_VERY_LIGHT_GRAY)

                is_near_robot = human_relative_location["is_near_robot"]
                if is_near_robot is True:
                    handle_param(update_function.rl_led_is_near_robot.UpdateColor, CUSTOM_COLOR_BLUE)
                else:
                    handle_param(update_function.rl_led_is_near_robot.UpdateColor, CUSTOM_COLOR_VERY_LIGHT_GRAY)
                is_near_signboard = human_relative_location["is_near_signboard"]
                if is_near_signboard is True:
                    handle_param(update_function.rl_led_is_near_signboard.UpdateColor, CUSTOM_COLOR_BLUE)
                else:
                    handle_param(update_function.rl_led_is_near_signboard.UpdateColor, CUSTOM_COLOR_VERY_LIGHT_GRAY)

                # is Speaking
                is_speaking_human = ef.get_param("/perception/is_speaking_human/data")
                if is_speaking_human is True:
                    handle_param(update_function.issp_led_is_speaking_human.UpdateColor, CUSTOM_COLOR_BLUE)
                else:
                    handle_param(update_function.issp_led_is_speaking_human.UpdateColor, CUSTOM_COLOR_VERY_LIGHT_GRAY)

                is_speaking_robot = ef.get_param("/perception/is_speaking_robot/data")
                if is_speaking_robot is True:
                    handle_param(update_function.issp_led_is_speaking_robot.UpdateColor, CUSTOM_COLOR_BLUE)
                else:
                    handle_param(update_function.issp_led_is_speaking_robot.UpdateColor, CUSTOM_COLOR_VERY_LIGHT_GRAY)

                reply_to_robot = ef.get_param("/perception/reply_to_robot/data")
                if reply_to_robot is True:
                    handle_param(update_function.issp_led_reply_to_robot.UpdateColor, CUSTOM_COLOR_BLUE)
                else:
                    handle_param(update_function.issp_led_reply_to_robot.UpdateColor, CUSTOM_COLOR_VERY_LIGHT_GRAY)

                # Location
                human_location = ef.get_param("/perception/social_distance")
                robot_location = ef.get_param("/perception/social_distance")
                social_distance = ef.get_param("/perception/social_distance")
                if social_distance == "public_space":
                    handle_param(update_function.sd_led_public_space.UpdateColor, CUSTOM_COLOR_BLUE)
                    handle_param(update_function.sd_led_social_space.UpdateColor, CUSTOM_COLOR_VERY_LIGHT_GRAY)
                    handle_param(update_function.sd_led_personal_space.UpdateColor, CUSTOM_COLOR_VERY_LIGHT_GRAY)
                    handle_param(update_function.sd_led_intimate_space.UpdateColor, CUSTOM_COLOR_VERY_LIGHT_GRAY)
                elif social_distance == "social_space":
                    handle_param(update_function.sd_led_public_space.UpdateColor, CUSTOM_COLOR_VERY_LIGHT_GRAY)
                    handle_param(update_function.sd_led_social_space.UpdateColor, CUSTOM_COLOR_BLUE)
                    handle_param(update_function.sd_led_personal_space.UpdateColor, CUSTOM_COLOR_VERY_LIGHT_GRAY)
                    handle_param(update_function.sd_led_intimate_space.UpdateColor, CUSTOM_COLOR_VERY_LIGHT_GRAY)
                elif social_distance == "personal_space":
                    handle_param(update_function.sd_led_public_space.UpdateColor, CUSTOM_COLOR_VERY_LIGHT_GRAY)
                    handle_param(update_function.sd_led_social_space.UpdateColor, CUSTOM_COLOR_VERY_LIGHT_GRAY)
                    handle_param(update_function.sd_led_personal_space.UpdateColor, CUSTOM_COLOR_BLUE)
                    handle_param(update_function.sd_led_intimate_space.UpdateColor, CUSTOM_COLOR_VERY_LIGHT_GRAY)
                elif social_distance == "intimate_space":
                    handle_param(update_function.sd_led_public_space.UpdateColor, CUSTOM_COLOR_VERY_LIGHT_GRAY)
                    handle_param(update_function.sd_led_social_space.UpdateColor, CUSTOM_COLOR_VERY_LIGHT_GRAY)
                    handle_param(update_function.sd_led_personal_space.UpdateColor, CUSTOM_COLOR_VERY_LIGHT_GRAY)
                    handle_param(update_function.sd_led_intimate_space.UpdateColor, CUSTOM_COLOR_BLUE)
                else:
                    handle_param(update_function.sd_led_public_space.UpdateColor, CUSTOM_COLOR_VERY_LIGHT_GRAY)
                    handle_param(update_function.sd_led_social_space.UpdateColor, CUSTOM_COLOR_VERY_LIGHT_GRAY)
                    handle_param(update_function.sd_led_personal_space.UpdateColor, CUSTOM_COLOR_VERY_LIGHT_GRAY)
                    handle_param(update_function.sd_led_intimate_space.UpdateColor, CUSTOM_COLOR_VERY_LIGHT_GRAY)

                # User Personality
                human_personality = ef.get_param("/perception/human_personality")

                # Dialog
                update_function_dialog = self.frame.top_panel.dialog_panel

                human_dialog = ef.get_param("/perception/human_dialog/data")
                human_dialog_ts = ef.get_param("/perception/human_dialog/timestamp")

                # 이부분 고려해!!!
                if once_flag == 0 and float(time.time()) - float(human_dialog_ts) < 3:
                    handle_param(update_function_dialog.AppendData, human_dialog)
                    once_flag = 1
                if once_flag == 1 and float(time.time()) - float(human_dialog_ts) > 3:
                    once_flag = 0

                human_intent = ef.get_param("/perception/human_intent/data")
                robot_dialog = ef.get_param("/perception/robot_dialog/data")

                time.sleep(0.2)
            except AttributeError as e:
                break


def handle_param(function, value):
    try:
        wx.CallAfter(function, value)
    except AttributeError as e:
        print(e)


def handle_image(image, frame):
    # wx.CallAfter(_update_function, image)
    try:
        _update_function = frame.top_panel.image_voice_panel.ros_image.update
        wx.CallAfter(_update_function, image)
    except AttributeError as e:
        print(e)


def handle_voice(topic, frame):
    audio_stream = topic.data
    msg_sequence = topic.header.seq
    byte_str = ef.make_byte_str(audio_stream)
    if VOICE_SCALE == "linear":
        wav_raw = ef.make_wav_raw(byte_str)  # Integer (-32768 to 32767)
    else:
        wav_raw = ef.convert_db(ef.make_wav_raw(byte_str))  # Integer (-32768 to 32767)
    try:
        _update_function = frame.top_panel.image_voice_panel.ros_voice.update
        wx.CallAfter(_update_function, wav_raw)
    except AttributeError as e:
        print(e)


def main():
    app = wx.App()
    frame = MainFrame(None, -1, "DeepTask GUI")

    rospy.init_node('deeptask_gui')
    topic_name_image = '/camera/color/image_raw'
    # topic_name_image = '/sn_kinect2/rgb/image_color/raw'
    topic_name_voice = '/audio_stream'
    rospy.Subscriber(topic_name_image, Image, handle_image, frame)
    rospy.Subscriber(topic_name_voice, AudioData, handle_voice, frame, queue_size=50)

    param_thread = ParameterGetter(frame)
    param_thread.start()
    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
