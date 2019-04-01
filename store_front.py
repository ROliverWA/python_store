import store
import products


our_store = store.Store()
cloths = products.Products('cloths', 10, 0, 12)
home = products.Products('home', 20, 1, 8)
shoes = products.Products('shoes', 50, 2, 9)

our_store.add_product(cloths)
our_store.add_product(home)
our_store.add_product(shoes)

our_store.list_products()


