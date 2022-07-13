from .models import *

# Return all products from the products table:
all_products = Product.objects.all()

# Return the product and the user that created it
user = User.objects.filter(username='admin5')
productsByUser = Product.objects.all().filter(user_id=5).count()

# Return a summary of the products by user
summary = Product.objects.all().filter(user_id=3).count()


