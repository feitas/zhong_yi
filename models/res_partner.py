# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ZyResPartner(models.Model):
    _inherit = "res.partner"

    zy_kahao = fields.Char(string="卡号")


    @api.multi
    def name_get(self):
        result = []

        for record in self:
            result.append((record.id, "%s,%s" % (record.zy_kahao, record.name)))
        return result

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        if not args:
            args = []

        if not self._rec_name:
            _logger.warning("Cannot execute name_search, no _rec_name defined on %s", self._name)
        elif not (name == '' and operator == 'ilike'):
            args += ['|', (self._rec_name, operator, name), ('zy_kahao', operator, name)]

        access_rights_uid = self._uid
        ids = self._search(args, limit=limit, access_rights_uid=access_rights_uid)
        recs = self.browse(ids)
        return recs.sudo(access_rights_uid).name_get()
