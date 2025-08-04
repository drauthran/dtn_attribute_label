# -*- coding: utf-8 -*-
from odoo import fields, models
import logging

_logger = logging.getLogger(__name__)

class ProductLabelLayout(models.TransientModel):
    _inherit = 'product.label.layout'

    print_format = fields.Selection(
        selection_add=[
            ('dtn_40x58_name_reliable', 'Этикетка (Надежное Название) (40х58мм)') # Обновлен ID и имя
        ],
        ondelete={'dtn_40x58_name_reliable': 'cascade'}
    )

    def process(self):
        if self.print_format == 'dtn_40x58_name_reliable': # Проверяем наш новый ID формата
            product_ids = self.env.context.get('active_ids', [])
            _logger.info(f"DTN Attribute Label: Обрабатываются product_ids: {product_ids}")

            products = self.env['product.product'].browse(product_ids)
            _logger.info(f"DTN Attribute Label: Загруженные продукты (до принудительной загрузки): {products}")
            
            # Принудительная загрузка новых надежных полей
            products.read(['x_reliable_name', 'x_reliable_active'])

            _logger.info(f"DTN Attribute Label: Загруженные продукты (после принудительной загрузки): {products}")
            
            if not products:
                _logger.warning("DTN Attribute Label: Нет продуктов для печати или они не найдены.")

            report_action = self.env.ref('dtn_attribute_label.action_report_dtn_attribute_label_new')
            _logger.info(f"DTN Attribute Label: Вызывается наш новый отчет: {report_action.name}")
            
            return report_action.report_action(products)
        
        return super().process()