from odoo import http

class MyWebsite(http.Controller):
    @http.route('/home2', type='http', auth="public", website=True)
    def my_page(self, **kw):
        return http.request.render('my_module.home', {})