from .user_controller    import create_user_endpoints, create_admin_user_endpoints
from .order_controller   import create_admin_order_endpoints
from .product_controller import (
    service_product_endpoint,
    create_admin_product_endpoints
)

__all__ = [
    'create_user_endpoints',
    'create_admin_user_endpoints',
    'create_admin_order_endpoints',
    'service_product_endpoint'
    'create_admin_product_endpoints'
]
