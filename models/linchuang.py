# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ZyLinChuang(models.Model):
	_name = "zy.lin.chuang"
	_order = "year DESC"

	name = fields.Char(string="标题", required=True)
	source = fields.Char(string="来源")
	year = fields.Char(string="年份")

	yao_fang_ids = fields.One2many("zy.lin.chuang.yao.fang", "lin_chuang_id")


class ZyLinChuangYaoFang(models.Model):
	_name = "zy.lin.chuang.yao.fang"

	name = fields.Many2one("product.template", string="药材")
	qty = fields.Float(string="重量")

	lin_chuang_id = fields.Many2one("zy.lin.chuang")
