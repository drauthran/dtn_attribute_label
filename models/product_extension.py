# -*- coding: utf-8 -*-
from odoo import api, fields, models
import logging

_logger = logging.getLogger(__name__)

class ProductProduct(models.Model):
    _inherit = 'product.product'

    x_reliable_name = fields.Char(
        string="Надежное имя товара",
        compute='_compute_x_reliable_name',
        store=False,
    )

    x_reliable_active = fields.Boolean(
        string="Надежный статус активности",
        compute='_compute_x_reliable_active',
        store=False,
    )

    x_reliable_default_code = fields.Char(
        string="Надежный артикул",
        compute='_compute_x_reliable_default_code',
        store=False,
    )

    x_reliable_lst_price = fields.Float(
        string="Надежная цена продажи",
        compute='_compute_x_reliable_lst_price',
        digits='Product Price',
        store=False,
    )

    x_reliable_currency_symbol = fields.Char(
        string="Надежный символ валюты",
        compute='_compute_x_reliable_currency_symbol',
        store=False,
    )

    x_reliable_barcode = fields.Char(
        string="Надежный штрихкод",
        compute='_compute_x_reliable_barcode',
        store=False,
    )

    x_reliable_attribute_values = fields.Many2many(
        'product.template.attribute.value',
        string="Надежные атрибуты",
        compute='_compute_x_reliable_attribute_values',
        store=False,
    )

    @api.depends('name', 'display_name', 'product_tmpl_id.name', 'active', 'product_tmpl_id.active')
    def _compute_x_reliable_name(self):
        _logger.info(f"DTN Attr: Computing x_reliable_name for records: {self.ids}")
        for rec in self:
            reliable_name = False
            try:
                reliable_name = rec.display_name
                _logger.info(f"DTN Attr: x_reliable_name for {rec.id} via display_name: {reliable_name}")
            except Exception as e:
                _logger.error(f"DTN Attr: Error accessing display_name for {rec.id}: {e}")
                try:
                    template_record = self.env['product.template'].browse(rec.id)
                    reliable_name = template_record.name
                    _logger.info(f"DTN Attr: x_reliable_name for {rec.id} via template.name: {reliable_name}")
                except Exception as e_tmpl:
                    reliable_name = f"ОШИБКА ИМЕНИ (ID: {rec.id})"
                    _logger.error(f"DTN Attr: Error accessing template.name for {rec.id}: {e_tmpl}")
            rec.x_reliable_name = reliable_name

    @api.depends('active', 'product_tmpl_id.active')
    def _compute_x_reliable_active(self):
        _logger.info(f"DTN Attr: Computing x_reliable_active for records: {self.ids}")
        for rec in self:
            reliable_active = False
            try:
                reliable_active = rec.active
                _logger.info(f"DTN Attr: x_reliable_active for {rec.id} via active: {reliable_active}")
            except Exception as e:
                _logger.error(f"DTN Attr: Error accessing active for {rec.id}: {e}")
                try:
                    template_record = self.env['product.template'].browse(rec.id)
                    reliable_active = template_record.active
                    _logger.info(f"DTN Attr: x_reliable_active for {rec.id} via template.active: {reliable_active}")
                except Exception as e_tmpl:
                    reliable_active = False
                    _logger.error(f"DTN Attr: Error accessing template.active for {rec.id}: {e_tmpl}")
            rec.x_reliable_active = reliable_active

    @api.depends('default_code', 'product_tmpl_id.default_code')
    def _compute_x_reliable_default_code(self):
        _logger.info(f"DTN Attr: Computing x_reliable_default_code for records: {self.ids}")
        for rec in self:
            reliable_default_code = False
            try:
                reliable_default_code = rec.default_code
                _logger.info(f"DTN Attr: x_reliable_default_code for {rec.id} via default_code: {reliable_default_code}")
            except Exception as e:
                _logger.error(f"DTN Attr: Error accessing default_code for {rec.id}: {e}")
                try:
                    template_record = self.env['product.template'].browse(rec.id)
                    reliable_default_code = template_record.default_code
                    _logger.info(f"DTN Attr: x_reliable_default_code for {rec.id} via template.default_code: {reliable_default_code}")
                except Exception as e_tmpl:
                    reliable_default_code = f"ОШИБКА АРТИКУЛА (ID: {rec.id})"
                    _logger.error(f"DTN Attr: Error accessing template.default_code for {rec.id}: {e_tmpl}")
            rec.x_reliable_default_code = reliable_default_code

    @api.depends('lst_price', 'product_tmpl_id.list_price')
    def _compute_x_reliable_lst_price(self):
        _logger.info(f"DTN Attr: Computing x_reliable_lst_price for records: {self.ids}")
        for rec in self:
            reliable_price = 0.0
            try:
                reliable_price = rec.lst_price
                _logger.info(f"DTN Attr: x_reliable_lst_price for {rec.id} via lst_price: {reliable_price}")
            except Exception as e:
                _logger.error(f"DTN Attr: Error accessing lst_price for {rec.id}: {e}")
                try:
                    template_record = self.env['product.template'].browse(rec.id)
                    reliable_price = template_record.list_price
                    _logger.info(f"DTN Attr: x_reliable_lst_price for {rec.id} via template.list_price: {reliable_price}")
                except Exception as e_tmpl:
                    reliable_price = 0.0
                    _logger.error(f"DTN Attr: Error accessing template.list_price for {rec.id}: {e_tmpl}")
            rec.x_reliable_lst_price = reliable_price

    @api.depends('barcode', 'product_tmpl_id.barcode')
    def _compute_x_reliable_barcode(self):
        _logger.info(f"DTN Attr: Computing x_reliable_barcode for records: {self.ids}")
        for rec in self:
            reliable_barcode = False
            try:
                reliable_barcode = rec.barcode
                _logger.info(f"DTN Attr: x_reliable_barcode for {rec.id} via barcode: {reliable_barcode}")
            except Exception as e:
                _logger.error(f"DTN Attr: Error accessing barcode for {rec.id}: {e}")
                try:
                    template_record = self.env['product.template'].browse(rec.id)
                    reliable_barcode = template_record.barcode
                    _logger.info(f"DTN Attr: x_reliable_barcode for {rec.id} via template.barcode: {reliable_barcode}")
                except Exception as e_tmpl:
                    reliable_barcode = f"ОШИБКА ШТРИХКОДА (ID: {rec.id})"
                    _logger.error(f"DTN Attr: Error accessing template.barcode for {rec.id}: {e_tmpl}")
            rec.x_reliable_barcode = reliable_barcode

    @api.depends('currency_id', 'product_tmpl_id.currency_id')
    def _compute_x_reliable_currency_symbol(self):
        _logger.info(f"DTN Attr: Computing x_reliable_currency_symbol for records: {self.ids}")
        for rec in self:
            reliable_symbol = ''
            try:
                reliable_symbol = rec.currency_id.symbol
                _logger.info(f"DTN Attr: x_reliable_currency_symbol for {rec.id} via currency_id.symbol: {reliable_symbol}")
            except Exception as e:
                _logger.error(f"DTN Attr: Error accessing currency_id.symbol for {rec.id}: {e}")
                try:
                    template_record = self.env['product.template'].browse(rec.id)
                    if template_record and template_record.currency_id:
                        reliable_symbol = template_record.currency_id.symbol
                        _logger.info(f"DTN Attr: x_reliable_currency_symbol for {rec.id} via template.currency_id.symbol: {reliable_symbol}")
                    else:
                        reliable_symbol = self.env.company.currency_id.symbol
                        _logger.info(f"DTN Attr: x_reliable_currency_symbol for {rec.id} via company currency (fallback): {reliable_symbol}")
                except Exception as e_tmpl:
                    reliable_symbol = self.env.company.currency_id.symbol
                    _logger.error(f"DTN Attr: Error accessing template.currency_id.symbol for {rec.id}: {e_tmpl}")
            rec.x_reliable_currency_symbol = reliable_symbol

    @api.depends('product_template_attribute_value_ids', 'product_tmpl_id.attribute_line_ids')
    def _compute_x_reliable_attribute_values(self):
        _logger.info(f"DTN Attr: Computing x_reliable_attribute_values for records: {self.ids}")
        for rec in self:
            reliable_attributes = self.env['product.template.attribute.value']
            
            is_template_only = False
            try:
                # Определяем, работаем мы с шаблоном или с вариантом
                if rec.product_tmpl_id and rec.product_tmpl_id.id == rec.id:
                    is_template_only = True
                elif not rec.product_tmpl_id:
                    is_template_only = True
            except Exception as e:
                _logger.error(f"DTN Attr: Error checking product_tmpl_id for {rec.id}: {e}. Assuming template-only due to error.")
                is_template_only = True

            try:
                if is_template_only:
                    _logger.info(f"DTN Attr: {rec.id} is a template. Getting attributes via attribute_line_ids.")
                    template_record = self.env['product.template'].browse(rec.id)
                    if template_record and template_record.attribute_line_ids:
                        for attr_line in template_record.attribute_line_ids:
                            for attr_val in attr_line.value_ids:
                                # Ищем связующую запись product.template.attribute.value
                                ptav = self.env['product.template.attribute.value'].search([
                                    ('attribute_id', '=', attr_line.attribute_id.id),
                                    ('product_tmpl_id', '=', template_record.id),
                                    # --- ИСПРАВЛЕННАЯ СТРОКА ---
                                    ('product_attribute_value_id', '=', attr_val.id) 
                                    # Было: ('attribute_value_id', '=', attr_val.id)
                                ], limit=1)
                                if ptav:
                                    reliable_attributes |= ptav
                    _logger.info(f"DTN Attr: Found {len(reliable_attributes)} attributes via template.attribute_line_ids for {rec.id}.")
                else:
                    _logger.info(f"DTN Attr: {rec.id} is a variant. Getting attributes via product_template_attribute_value_ids.")
                    if rec.product_template_attribute_value_ids:
                        reliable_attributes = rec.product_template_attribute_value_ids
                        _logger.info(f"DTN Attr: Found {len(reliable_attributes)} attributes via product_template_attribute_value_ids for {rec.id}.")
                    elif rec.product_tmpl_id and rec.product_tmpl_id.attribute_line_ids:
                        # Запасной вариант для варианта, если прямая ссылка пуста
                        _logger.info(f"DTN Attr: Falling back to template's attributes for variant {rec.id}.")
                        for ptav in rec.product_tmpl_id.attribute_line_ids.mapped('product_template_value_ids'):
                             if ptav.product_attribute_value_id in rec.product_template_attribute_value_ids.mapped('product_attribute_value_id'):
                                reliable_attributes |= ptav
                        _logger.info(f"DTN Attr: Found {len(reliable_attributes)} attributes via template fallback for variant {rec.id}.")

            except Exception as e:
                _logger.error(f"DTN Attr: ORM error accessing attributes for {rec.id}: {e}. Falling back to empty RecordSet.")
                reliable_attributes = self.env['product.template.attribute.value']

            rec.x_reliable_attribute_values = reliable_attributes
            _logger.info(f"DTN Attr: Final x_reliable_attribute_values for {rec.id}: {len(rec.x_reliable_attribute_values)} records.")
            if len(rec.x_reliable_attribute_values) > 0:
                _logger.info(f"DTN Attr: Sample attribute IDs for {rec.id}: {[val.id for val in rec.x_reliable_attribute_values[:5]]}")

    # НОВИЙ МЕТОД ДЛЯ ГРУПУВАННЯ АТРИБУТІВ
    def get_grouped_attributes(self):
        """
        Цей метод групує значення атрибутів.
        Замість [('Стиль', 'Рок'), ('Стиль', 'Гранж')]
        він повертає [('Стиль', 'Рок, Гранж')]
        """
        self.ensure_one()
        
        # Словник для тимчасового зберігання згрупованих даних
        grouped_data = {}
        
        # Використовуємо наше надійне поле як джерело даних
        for attr_val in self.x_reliable_attribute_values:
            attribute_name = attr_val.attribute_id.name
            value_name = attr_val.name
            
            # Якщо ми ще не зустрічали такий атрибут, створюємо для нього новий список
            if attribute_name not in grouped_data:
                grouped_data[attribute_name] = []
            
            # Додаємо значення до списку відповідного атрибута
            grouped_data[attribute_name].append(value_name)
            
        # Тепер перетворюємо словник у фінальний список пар ('атрибут', 'значення, значення...')
        result = []
        for attribute, values in grouped_data.items():
            result.append((attribute, ', '.join(values)))
            
        return result