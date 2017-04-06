# -*- coding: utf-8 -*-
from odoo import http

# class ZhongYi(http.Controller):
#     @http.route('/zhong_yi/zhong_yi/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/zhong_yi/zhong_yi/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('zhong_yi.listing', {
#             'root': '/zhong_yi/zhong_yi',
#             'objects': http.request.env['zhong_yi.zhong_yi'].search([]),
#         })

#     @http.route('/zhong_yi/zhong_yi/objects/<model("zhong_yi.zhong_yi"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('zhong_yi.object', {
#             'object': obj
#         })