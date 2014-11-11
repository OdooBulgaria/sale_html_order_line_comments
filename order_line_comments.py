from openerp.osv import osv, fields

class theme_genesis(osv.Model):
    _inherit = 'sale.order.line'
    
    _columns = {
        'x_sale_order_line_comment_1': fields.html('O_line Comment #1'),
  
    }
