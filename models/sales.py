# -*- coding: utf-8 -*-

from odoo import models, fields, api

class zy_sale_order(models.Model):
    _inherit = 'sale.order'

    zy_zhenduan_jilu = fields.Html(string="诊断记录")