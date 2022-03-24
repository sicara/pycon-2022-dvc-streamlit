from functools import partial
from typing import Literal, Optional

import streamlit as st
from bs4 import BeautifulSoup

TAG = Literal["div", "a", "span"]


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


def make_tag(
    name: TAG, style: Optional[CSSStyle] = None, text: Optional[str] = None
) -> BeautifulSoup:
    new_tag = (
        BeautifulSoup().new_tag(name, style=str(style))
        if style
        else BeautifulSoup().new_tag(name)
    )

    if text:
        new_tag.append(text)

    return new_tag


make_div = partial(make_tag, name="div")


def st_write_bf4(soup: BeautifulSoup):
    st.write(soup.__repr__(), unsafe_allow_html=True)
