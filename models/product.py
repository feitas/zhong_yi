# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ZyZhongYao(models.Model):
	_inherit = "product.template"

	is_zy_zhongyao = fields.Boolean(string="中药")
	zy_pinyin = fields.Char("拼音")
	zy_wei = fields.Many2many("zy.zhongyao.wei", string="味")
	zy_qi = fields.Many2many("zy.zhongyao.qi", string="气")
	zy_jing = fields.Many2many("zy.zhongyao.jing", string="归经")


class ZyZhongYaoWei(models.Model):
	_name = "zy.zhongyao.wei"

	name = fields.Char("名称")


class ZyZhongYaoQi(models.Model):
	_name = "zy.zhongyao.qi"

	name = fields.Char("名称")


class ZyZhongYaoJing(models.Model):
	_name = "zy.zhongyao.jing"

	name = fields.Char("名称")