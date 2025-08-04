# -*- coding: utf-8 -*-
from odoo import fields, models
import logging

_logger = logging.getLogger(__name__)

class ProductLabelLayout(models.TransientModel):
    _inherit = 'product.label.layout'

    # Добавляем наш собственный формат в список выбора
    print_format = fields.Selection(
        selection_add=[
            ('dtn_40x58_name_reliable', 'Этикетка с атрибутами (40х58мм)')
        ],
        ondelete={'dtn_40x58_name_reliable': 'cascade'}
    )

    def process(self):
        # Если выбран наш формат, используем нашу логику
        if self.print_format == 'dtn_40x58_name_reliable':
            # Получаем ID товаров, выбранных для печати
            product_ids = self.env.context.get('active_ids', [])
            _logger.info(f"DTN Attribute Label: Обрабатываются product_ids: {product_ids}")

            products = self.env['product.product'].browse(product_ids)
            
            # Принудительная загрузка всех наших "надежных" полей для эффективности.
            # Это гарантирует, что все вычисляемые поля будут рассчитаны перед отправкой в шаблон.
            products.read([
                'x_reliable_name',
                'x_reliable_active',
                'x_reliable_default_code',
                'x_reliable_lst_price',
                'x_reliable_currency_symbol',
                'x_reliable_barcode',
                'x_reliable_attribute_values',
            ])

            _logger.info(f"DTN Attribute Label: Данные для {len(products)} продуктов загружены.")
            
            if not products:
                _logger.warning("DTN Attribute Label: Нет продуктов для печати или они не найдены.")

            # Вызываем действие отчета, которое мы определили в XML
            report_action = self.env.ref('dtn_attribute_label.action_report_dtn_attribute_label_new')
            _logger.info(f"DTN Attribute Label: Вызывается отчет: {report_action.name}")
            
            return report_action.report_action(products)
        
        # Для всех остальных форматов используем стандартную логику Odoo
        return super().process()