# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ZyCrmLead(models.Model):
    _inherit = "crm.lead"


    zy_department = fields.Many2one("hr.department", string='科室')
    zy_employee = fields.Many2one("hr.employee", string="医师")
    zy_book_datetime = fields.Datetime(string="预约时间")

    @api.onchange("zy_department")
    def onchange_zy_department(self):
    	return {
    		'domain': {'zy_employee': [('department_id', '=', self.zy_department.id)]}
    	}
