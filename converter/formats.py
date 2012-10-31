#!/usr/bin/env python


class BaseFormat(object):
    """
    Base format class.

    Supported formats are: ogg, avi, mkv, webm, flv, mov, mp4, mpeg
    """

    format_name = None
    avconv_format_name = None

    def parse_options(self, opt):
        if 'format' not in opt or opt.get('format') != self.format_name:
            raise ValueError('invalid Format format')
        return ['-f', self.avconv_format_name]


class _3GPFormat(BaseFormat):
    """
    3gp container format.
    """
    format_name = '3gp'
    avconv_format_name = '3gp'


class OggFormat(BaseFormat):
    """
    Ogg container format, mostly used with Vorbis and Theora.
    """
    format_name = 'ogg'
    avconv_format_name = 'ogg'


class AviFormat(BaseFormat):
    """
    Avi container format, often used vith DivX video.
    """
    format_name = 'avi'
    avconv_format_name = 'avi'


class MkvFormat(BaseFormat):
    """
    Matroska format, often used with H.264 video.
    """
    format_name = 'mkv'
    avconv_format_name = 'matroska'


class WebmFormat(BaseFormat):
    """
    WebM is Google's variant of Matroska containing only
    VP8 for video and Vorbis for audio content.
    """
    format_name = 'webm'
    avconv_format_name = 'webm'


class FlvFormat(BaseFormat):
    """
    Flash Video container format.
    """
    format_name = 'flv'
    avconv_format_name = 'flv'


class MovFormat(BaseFormat):
    """
    Mov container format, used mostly with H.264 video
    content, often for mobile platforms.
    """
    format_name = 'mov'
    avconv_format_name = 'mov'


class Mp4Format(BaseFormat):
    """
    Mp4 container format, the default Format for H.264
    video content.
    """
    format_name = 'mp4'
    avconv_format_name = 'mp4'


class MpgFormat(BaseFormat):
    """
    MPEG(TS) container, used mainly for MPEG 1/2 video codecs.
    """
    format_name = 'mpg'
    avconv_format_name = 'mpegts'

class MpegFormat(BaseFormat):
    """
    MPEG(TS) container, used mainly for MPEG 1/2 video codecs.
    """
    format_name = 'mpeg'
    avconv_format_name = 'mpegts'


format_list = [
    OggFormat, AviFormat, MkvFormat, WebmFormat, FlvFormat,
    MovFormat, Mp4Format, MpgFormat, MpegFormat, _3GPFormat
]
