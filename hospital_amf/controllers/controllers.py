# -*- coding: utf-8 -*-
# from odoo import http


# class HospitalAmf(http.Controller):
#     @http.route('/hospital_amf/hospital_amf', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hospital_amf/hospital_amf/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hospital_amf.listing', {
#             'root': '/hospital_amf/hospital_amf',
#             'objects': http.request.env['hospital_amf.hospital_amf'].search([]),
#         })

#     @http.route('/hospital_amf/hospital_amf/objects/<model("hospital_amf.hospital_amf"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hospital_amf.object', {
#             'object': obj
#         })

