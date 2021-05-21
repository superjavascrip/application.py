# -*- coding: utf-8 -*-
from typing import List

import requests
from pydub import AudioSegment
import execjs
from urllib.parse import quote


class GoogleVoice(object):

    def __init__(
            self,
            service_url: str = "translate.google.cn"
    ):
        from Constants import SERVICE_URLS
        if service_url in SERVICE_URLS:
            self.service_url = service_url
        else:
            self.service_url = "translate.google.cn"

    @staticmethod
    def splicing_audio(
            file_list: List[str],
            output_file
    ) -> None:
        try:
            output_music = AudioSegment.empty()
            for i in file_list:
                output_music += AudioSegment.from_file(i, "mp3")
            output_music += AudioSegment.silent(duration=1000)
            output_music.export(output_file, format="mp3")
        except BaseException as Error:
            raise Error

    @staticmethod
    def get_token(
            text: str
    ) -> str:
        return execjs.compile("""
function TL(a) {
    var k = "";
    var b = 406644;
    var b1 = 3293161072;
    
    var jd = ".";
    var $b = "+-a^+6";
    var Zb = "+-3^+b+-f";

    for (var e = [], f = 0, g = 0; g < a.length; g++) {
        var m = a.charCodeAt(g);
        128 > m ? e[f++] = m : (2048 > m ? e[f++] = m >> 6 | 192 : (55296 == (m & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? (m = 65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023),
        e[f++] = m >> 18 | 240,
        e[f++] = m >> 12 & 63 | 128) : e[f++] = m >> 12 | 224,
        e[f++] = m >> 6 & 63 | 128),
        e[f++] = m & 63 | 128)
    }
    a = b;
    for (f = 0; f < e.length; f++) a += e[f],
    a = RL(a, $b);
    a = RL(a, Zb);
    a ^= b1 || 0;
    0 > a && (a = (a & 2147483647) + 2147483648);
    a %= 1E6;
    return a.toString() + jd + (a ^ b)
};

function RL(a, b) {
    var t = "a";
    var Yb = "+";
    for (var c = 0; c < b.length - 2; c += 3) {
        var d = b.charAt(c + 2),
        d = d >= t ? d.charCodeAt(0) - 87 : Number(d),
        d = b.charAt(c + 1) == Yb ? a >>> d: a << d;
        a = b.charAt(c) == Yb ? a + d & 4294967295 : a ^ d
    }
    return a
}
        """).call("TL", text)

    def output_voice(
            self,
            text: str,
            output_file: str = "Output/Output.mp3",
            language: str = "zh-cn"
    ) -> None:
        try:
            url = f"https://{self.service_url}/translate_tts?ie=UTF-8&q={quote(text, 'utf-8')}&tl={language}" \
                  f"&total=1&idx=0&textlen={quote(str(len(text)), 'utf-8')}&tk={self.get_token(text)}&client=webapp "
            context = requests.get(url, timeout=3000)
            with open(output_file, "wb") as output_file_write:
                for data in context.iter_content(chunk_size=1024):
                    if data:
                        output_file_write.write(data)
        except ConnectionError:
            raise ConnectionError("请求失败")
