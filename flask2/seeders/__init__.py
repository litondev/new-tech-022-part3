from seeders.user_seeder import UserSeeder
from seeders.product_seeder import ProductSeeder

def RunSeeder(db,**model):
	user_seeder = UserSeeder()
	user_seeder.run(db,model['user'])

	product_seeder = ProductSeeder()
	product_seeder.run(db,model['product'])