from odoo import http

class MyController(http.Controller):
    @http.route('/test', auth='public', website=True)
    def test_page(self, **kwargs):
        return http.request.render('my_module.test_template', {})