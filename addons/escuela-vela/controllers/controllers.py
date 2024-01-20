# -*- coding: utf-8 -*-
# from odoo import http


# class Escuela-vela(http.Controller):
#     @http.route('/escuela-vela/escuela-vela', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/escuela-vela/escuela-vela/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('escuela-vela.listing', {
#             'root': '/escuela-vela/escuela-vela',
#             'objects': http.request.env['escuela-vela.escuela-vela'].search([]),
#         })

#     @http.route('/escuela-vela/escuela-vela/objects/<model("escuela-vela.escuela-vela"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('escuela-vela.object', {
#             'object': obj
#         })
