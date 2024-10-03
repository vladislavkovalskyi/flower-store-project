tools = [
    {
        "type": "function",
        "function": {
            "name": "get_user_city",
            "description": "Get the city of the user. Call this whenever you need to know the city of the user, e.g. for delivery purposes.",
            "parameters": {
                "type": "object",
                "properties": {"user_id": {"type": "integer"}},
                "required": ["user_id"],
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "update_city",
            "description": "Update the city of the user. Call this whenever you need to update the city of the user, e.g. when the user changes or appends their location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {"type": "integer"},
                    "city": {"type": "string"},
                },
                "required": ["user_id", "city"],
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "add_product_to_cart",
            "description": "Add a product to the user's cart. At first, you need to call get_product_list to know list of products, after you need to request the user to choose the product and quantity, then call this function to add the product to the user's cart.",
            "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {"type": "integer"},
                    "product_id": {"type": "integer"},
                    "quantity": {"type": "integer"},
                },
                "required": ["user_id", "product_id", "quantity"],
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_cart_products",
            "description": "Get the list of products in the user's cart. Call this whenever you need to know the list of products in the user's cart, e.g. for order confirmation.",
            "parameters": {
                "type": "object",
                "properties": {"user_id": {"type": "integer"}},
                "required": ["user_id"],
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "clear_cart",
            "description": "Clear the user's cart. Call this whenever you need to clear the user's cart, e.g. when the user cancels the order.",
            "parameters": {
                "type": "object",
                "properties": {"user_id": {"type": "integer"}},
                "required": ["user_id"],
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "remove_product_from_cart",
            "description": "Remove a product from the user's cart. Call this whenever you need to remove a product from the user's cart, e.g. when the user changes their mind.",
            "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {"type": "integer"},
                    "product_id": {"type": "integer"},
                },
                "required": ["user_id", "product_id"],
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_product_list",
            "description": "Check the list of products available. Call this whenever you need to know the list of products available for purchase.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": [],
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "check_stock",
            "description": "Check the stock of a product. Call this whenever you need to check the stock of a product, e.g. before adding it to the cart.",
            "parameters": {
                "type": "object",
                "properties": {"product_id": {"type": "integer"}},
                "required": ["product_id"],
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "make_order",
            "description": "Make an order for the products in the user's cart. Call this whenever you need to make an order for the products in the user's cart, e.g. after the user confirms the order. \"products_data\" it is a string with the text of the products, quantity and their price.",
            "parameters": {
                "type": "object",
                "properties": {
                    "products_data": {"type": "string"},
                    "user_id": {"type": "integer"},
                    "total_price": {"type": "number"},
                    "city": {"type": "string"},
                    "delivery_address": {"type": "string"},
                    "client_full_name": {"type": "string"},
                },
                "required": [
                    "products_data",
                    "user_id",
                    "total_price",
                    "city",
                    "delivery_address",
                    "client_full_name",
                ],
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculate_delivery_cost",
            "description": "Calculate the delivery cost based on the weather conditions. Call this whenever you need to calculate the delivery cost based on the weather conditions, e.g. for order confirmation.",
            "parameters": {
                "type": "object",
                "properties": {
                    "base_cost": {"type": "number", "default": 100.0},
                    "city": {"type": "string"},
                },
                "required": ["weather_code", "temperature"],
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_datetime",
            "description": "Get the current date and time. Call this whenever you need to know the current date and time, e.g. for order confirmation.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": [],
                "additionalProperties": False,
            },
        },
    },
]
