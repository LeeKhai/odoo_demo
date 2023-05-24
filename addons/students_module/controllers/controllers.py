# -*- coding: utf-8 -*-
# from odoo import http


# class StudentsModule(http.Controller):
#     @http.route('/students_module/students_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/students_module/students_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('students_module.listing', {
#             'root': '/students_module/students_module',
#             'objects': http.request.env['students_module.students_module'].search([]),
#         })

#     @http.route('/students_module/students_module/objects/<model("students_module.students_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('students_module.object', {
#             'object': obj
#         })
