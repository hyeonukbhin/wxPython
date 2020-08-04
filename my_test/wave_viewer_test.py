import rospy
from audio_msgs.msg import AudioData, FeatureData
import numpy as np
import matplotlib
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure

import wx

matplotlib.use('WXAgg')


def callback_packet(topic):
    audio_stream = topic.data
    msg_sequence = topic.header.seq
    byte_str = make_byte_str(audio_stream)
    wav_raw = make_wav_raw(byte_str)
    wx.CallAfter(panel.update, wav_raw)


def make_byte_str(int16Array):
    byte_str = "".join(map(chr, int16Array))
    return byte_str

def make_wav_raw(byte_str):
    # wav_raw = np.fromstring(byte_str, dtype=np.int16).astype(np.float64) / 32768 / Integer (-32768 to 32767)
    wav_raw = np.fromstring(byte_str, dtype=np.int16)
    return wav_raw


class CanvasPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.SetSizer(self.sizer)
        self.Fit()

    def draw(self):
        x = range(0, 8000)
        y = [0] * len(x)
        self.axes.set_ylim([-2 ** 15, (2 ** 15) - 1])
        self.axes.plot(x, y)

    def update(self, data):
        x = range(0, len(data))
        y = data
        self.axes.clear()
        self.axes.set_ylim([-2 ** 15, (2 ** 15) - 1])
        self.axes.plot(x, y)
        self.canvas.draw()
        self.canvas.flush_events()


if __name__ == '__main__':
    try:
        # voice_viewer = VoiceSignalViewer()
        # voice_viewer.start()
        rospy.init_node("audio_signal_processor", anonymous=False)
        rospy.Subscriber("audio_stream", AudioData, callback_packet, queue_size=50)
        app = wx.App()
        fr = wx.Frame(None, title='test')
        panel = CanvasPanel(fr)
        panel.draw()
        fr.Show()
        app.MainLoop()
        # AudioSignalProcessor()
    except rospy.ROSInterruptException:
        pass
