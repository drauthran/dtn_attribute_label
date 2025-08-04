# -*- coding: utf-8 -*-
from odoo import api, fields, models

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

    # НОВОЕ ПОЛЕ: Надежный артикул
    x_reliable_default_code = fields.Char(
        string="Надежный артикул",
        compute='_compute_x_reliable_default_code',
        store=False,
    )

    @api.depends('name', 'display_name', 'product_tmpl_id.name', 'active', 'product_tmpl_id.active')
    def _compute_x_reliable_name(self):
        for rec in self:
            reliable_name = False
            try:
                # Попытка 1: Получить display_name от product.product (наиболее общий случай)
                reliable_name = rec.display_name
            except Exception as e:
                # Если display_name вызывает ошибку (как MissingError),
                # значит, RecordSet product.product может быть поврежден для этой записи.
                # Попытка 2: Попробовать получить имя напрямую из product.template по ID
                try:
                    template_record = self.env['product.template'].browse(rec.id)
                    reliable_name = template_record.name # У template нет display_name в том же смысле, что у product.product
                except Exception:
                    # Если и template.name вызывает ошибку (что крайне маловероятно, учитывая логи search().read()),
                    # или если товар не является шаблоном, но все равно проблемный.
                    reliable_name = f"ОШИБКА ИМЕНИ (ID: {rec.id})"
            rec.x_reliable_name = reliable_name

    @api.depends('active', 'product_tmpl_id.active')
    def _compute_x_reliable_active(self):
        for rec in self:
            reliable_active = False
            try:
                # Попытка 1: Получить active от product.product
                reliable_active = rec.active
            except Exception as e:
                # Если active вызывает ошибку, попробовать получить active напрямую из product.template по ID
                try:
                    template_record = self.env['product.template'].browse(rec.id)
                    reliable_active = template_record.active
                except Exception:
                    reliable_active = False # По умолчанию False, если не удалось получить

            rec.x_reliable_active = reliable_active

    # НОВЫЙ МЕТОД: Вычисление надежного артикула
    @api.depends('default_code', 'product_tmpl_id.default_code')
    def _compute_x_reliable_default_code(self):
        for rec in self:
            reliable_default_code = False
            try:
                # Попытка 1: Получить default_code от product.product
                reliable_default_code = rec.default_code
            except Exception as e:
                # Если default_code вызывает ошибку, попробовать получить его напрямую из product.template по ID
                try:
                    template_record = self.env['product.template'].browse(rec.id)
                    reliable_default_code = template_record.default_code
                except Exception:
                    reliable_default_code = f"ОШИБКА АРТИКУЛА (ID: {rec.id})"
            rec.x_reliable_default_code = reliable_default_code