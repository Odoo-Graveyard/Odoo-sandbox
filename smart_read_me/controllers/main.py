from odoo import http

class MyController(http.Controller):
    @http.route('/test', auth='public', website=True)
    def test_page(self, **kwargs):
        print('Rendering test template...')
        return http.request.render('smart_read_me.test_template', {})