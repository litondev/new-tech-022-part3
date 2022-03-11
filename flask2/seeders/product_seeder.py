class ProductSeeder():
    def run(self,db,Product):
        print("Start Seeder")    

        i = 0;

        while(i < 30):
            db.session.add(Product('product '+str(i),10,10,None))
            db.session.commit() 
            i += 1
        
        print("Done Seeder")