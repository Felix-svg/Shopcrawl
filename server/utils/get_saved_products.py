from models.product import Product

def get_saved_products(product_name, source_domain):
    products = Product.query.filter(
        Product.name.ilike(f"%{product_name}%"),
        Product.source.ilike(f"%{source_domain}%")
    ).all()
    return [
        {
            "product_name": product.name,
            "product_price": product.price,
            "image_src": product.image_src,
            "product_rating": product.rating,
            "source": product.source,
        }
        for product in products
    ]