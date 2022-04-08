import base64
from functools import partial
from pathlib import Path
from typing import Literal, Optional

import streamlit as st
from bs4 import BeautifulSoup

TAG = Literal["div", "a", "span", "img"]


class CSSStyle:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, self._format_css_key(key), value)

    def _to_str(self):
        return "; ".join([f"{key}: {value}" for key, value in self.__dict__.items()])

    __str__ = __repr__ = _to_str

    @staticmethod
    def _format_css_key(key):
        return key.replace("_", "-")


def make_tag(name: TAG, style: Optional[CSSStyle] = None, text: Optional[str] = None) -> BeautifulSoup:
    new_tag = BeautifulSoup().new_tag(name, style=str(style)) if style else BeautifulSoup().new_tag(name)

    if text:
        new_tag.append(text)

    return new_tag


make_div = partial(make_tag, name="div")


def make_img(src: Path, style: Optional[CSSStyle] = None) -> BeautifulSoup:
    image_bs = make_tag("img", style=style)
    image_ext = src.suffix[1:]

    if image_ext == "svg":
        with open(src, "r") as f:
            lines = f.readlines()
            svg = "".join(lines)
        b64_image = base64.b64encode(svg.encode("utf-8")).decode("utf-8")
        image_ext = "svg+xml"
    else:
        with open(src, "rb") as image_file:
            b64_image = base64.b64encode(image_file.read()).decode("utf-8")

    image_bs["src"] = f"data:image/{image_ext};base64,{b64_image}"

    return image_bs


def st_write_bs4(soup: BeautifulSoup):
    st.write(soup.__repr__(), unsafe_allow_html=True)
