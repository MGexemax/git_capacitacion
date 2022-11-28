# -*- coding: utf-8 -*-
# from odoo import http


# class GitCapacitacion(http.Controller):
#     @http.route('/git_capacitacion/git_capacitacion/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/git_capacitacion/git_capacitacion/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('git_capacitacion.listing', {
#             'root': '/git_capacitacion/git_capacitacion',
#             'objects': http.request.env['git_capacitacion.git_capacitacion'].search([]),
#         })

#     @http.route('/git_capacitacion/git_capacitacion/objects/<model("git_capacitacion.git_capacitacion"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('git_capacitacion.object', {
#             'object': obj
#         })
