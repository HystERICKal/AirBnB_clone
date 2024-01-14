#!/usr/bin/python3
"""The user module"""

from models.base_model import BaseModel


class User(BaseModel):
    """The user class"""
    email = ""
    first_name = ""
    last_name = ""
    password = ""
