# -*- coding: utf-8 -*-
from odoo import models, fields
from odoo.exceptions import ValidationError
class LibraryBook(models.Model): 
 # ... 
 short_name = fields.Char('Short Title') 
 notes = fields.Text('Internal Notes') 
 state = fields.Selection( 
 [('draft', 'Not Available'), 
 ('available', 'Available'), 
 ('lost', 'Lost')], 
 'State') 
 description = fields.Html('Description') 
 cover = fields.Binary('Book Cover') 
 out_of_print = fields.Boolean('Out of Print?') 
 date_release = fields.Date('Release Date') 
 date_updated = fields.Datetime('Last Updated') 
 pages = fields.Integer('Number of Pages') 
 reader_rating = fields.Float('Reader Average Rating', digits=(14, 4), # Optional precision decimals,
 ) 
 

def name_get(self):
 result = []
 for record in self:
    rec_name = "%s (%s)" % (record.name, record.date_release)
    result.append((record.id, rec_name))
    return result

# def count_author(self):
#     for book in self:
#         book.author_count = len(book.author_ids)