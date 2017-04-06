# -*- coding: utf-8 -*-

from odoo import models, fields, api

class zy_zhenshi(models.Model):
    _name = 'zy.zhenshi'

    name = fields.Char(string="名称")
