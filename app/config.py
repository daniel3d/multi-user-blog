# coding: utf-8
"""Common configuration."""

import re

DEV = True
"""If the app is in devolepment."""

VERSION = '0.1.0'
"""The app version."""

APP_KEY = 'base64:VWRhY2l0eSBGdWxsIFN0YWNrIFdlYiBEZXZlbG9wZXIgTmFub2RlZ3JlZQ=='
"""Make sure this is updated when in production."""

COLOR_PALETTE = ["#f44336", "#e91e63", "#9c27b0", "#673ab7", "#3f51b5",
                 "#2196f3", "#00bcd4", "#009688", "#4caf50", "#8bc34a",
                 "#cddc39", "#ffeb3b", "#ffC107", "#ff9800", "#ff5722",
                 "#795548", "#9e9e9e", "#607d8b", "#2c3e50"]
"""The main colors we use to genarete ribbons for our posts."""

REGEXR_USERNAME = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
REGEXR_PASSWORD = re.compile(r"^.{3,20}$")
REGEXR_EMAIL = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
"""Regular expressions."""
