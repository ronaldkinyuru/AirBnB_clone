#!/usr/bin/python3
""" class City that inherit from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """inherit from BaseModel"""
    state_id = ""
    name = ""
        