from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Cuisine, Base, Recipe, User

engine = create_engine('sqlite:///cuisinerecipewithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create a user
User1 = User(name = "Emma Johnson", email = "candycrush0803@gmail.com", picture = "http://onelittleproject.com/wp-content/uploads/2013/12/DSC_4446.jpg")
session.add(User1)
session.commit()

# American Cuisine Recipes
cuisine1 = Cuisine(user_id=1, name = "American")
session.add(cuisine1)
session.commit()

recipe1 = Recipe(user_id=1, name = "Pepper Poppers", description = "Creamy stuffed jalapenos", preptime = "40 mins", course = "Appetizers", cuisine = cuisine1)
session.add(recipe1)
session.commit()

recipe2 = Recipe(user_id=1, name = "Glazed Chicken Wings", description = "Saucy dipped chicken wings", preptime = "1 hour", course = "Appetizers", cuisine = cuisine1)
session.add(recipe2)
session.commit()

recipe3 = Recipe(user_id=1, name = "Buffalo Wings", description = "Fried chicken tenders coated in spicy Nashville Hot seasoning with lettuce, tomatoes and pickles; served on a brioche bun", preptime = "2 hours", course = "Entrees", cuisine = cuisine1)
session.add(recipe3)
session.commit()

recipe4 = Recipe(user_id=1, name = "Meatloaf", description = "Meatloaf, made with savory seasonings, onions, tomato puree, and toasted breadcrumbs.", preptime = "1 hour", course = "Entrees", cuisine = cuisine1)
session.add(recipe4)
session.commit()

recipe5 = Recipe(user_id=1, name = "Chicken fried steak", description = "A dinner-sized, golden-fried chopped beef steak smothered in rich country gravy.", preptime = "1 hour", course = "Entrees", cuisine = cuisine1)
session.add(recipe5)
session.commit()

recipe6 = Recipe(user_id=1, name = "Cheese Cake", description = "Cheesecake recipe featuring a traditional graham crust and rich creamy filling all baked to perfection", preptime = "2 hours", course = "Desserts", cuisine = cuisine1)
session.add(recipe5)
session.commit()

recipe7 = Recipe(user_id=1, name = "Fudge", description = "Brownies with a fudgy foundation with the addition of decadent choclate chip morsels", preptime = "20 mins", course = "Desserts", cuisine = cuisine1)
session.add(recipe7)
session.commit()

recipe8 = Recipe(user_id=1, name = "Apple Pie", description = "Pie filled with crisp, tart apples and cinnamon and fragrant spices", preptime = "3 hours", course = "Desserts", cuisine = cuisine1)
session.add(recipe8)
session.commit()

recipe9 = Recipe(user_id=1, name = "Soft Drinks", description = "Quench your thirst with a variety of soft drinks", preptime = "2 mins", course = "Beverages", cuisine = cuisine1)
session.add(recipe9)
session.commit()

recipe10 = Recipe(user_id=1, name = "Alcholic Beverages", description = "Sip on one of the best beverages", preptime = "5 mins", course = "Beverages", cuisine = cuisine1)
session.add(recipe10)
session.commit()

# Chinese Cuisine Recipes
cuisine2 =  Cuisine(user_id=1, name = "Chinese")
session.add(cuisine2)
session.commit()

recipe1 = Recipe(user_id=1, name = "Shrimp Toast", description = "A savory seasoned paste of shrimp, herbs and spices, and crunchy water chestnuts spread on a lightly toasted bread and fried until crisp", preptime = "15 mins", course = "Appetizers", cuisine = cuisine2)
session.add(recipe1)
session.commit()

recipe2 = Recipe(user_id=1, name = "Egg Roll", description = "Lightly breaded chicken breast cooked to a crisp, deliciously dressed egg roll", preptime = "30 mins", course = "Appetizers", cuisine = cuisine2)
session.add(recipe2)
session.commit()

recipe3 = Recipe(user_id=1, name = "Dumpling", description = "Dumplings filled with pork, crab meat and broth.", preptime = "20 mins", course = "Appetizers", cuisine = cuisine2)
session.add(recipe3)
session.commit()

recipe4 = Recipe(user_id=1, name = "Kung Pao Chicken", description = "A Szechwan-inspired dish with chicken, peanuts and vegetables, finished with chili peppers.", preptime = "2 hours", course = "Entrees", cuisine = cuisine2)
session.add(recipe4)
session.commit()

recipe5 = Recipe(user_id=1, name = "Mapo Tofu", description = "Spicy, numbing, hot, aromatic and tender Mapo Tofu", preptime = "20 mins", course = "Entrees", cuisine = cuisine2)
session.add(recipe5)
session.commit()

recipe6 = Recipe(user_id=1, name = "Chow Mein", description = "Deep-fried crunchy golden egg noodles, green peppers, pea pods, bok choy, bamboo shoots, water chestnuts, shrimp, Chinese roast pork (char siu), chicken, and beef, and is served in a thick sauce.", preptime = "15 mins", course = "Entrees", cuisine = cuisine2)
session.add(recipe6)
session.commit()

recipe7 = Recipe(user_id=1, name = "Moon Cake", description = "Cake-like crust topped with a creamy vanilla, cream cheese pudding and smothered in whipped topping with just a hint of chocolate syrup", preptime = "2 hours", course = "Desserts", cuisine = cuisine2)
session.add(recipe7)
session.commit()

recipe8 = Recipe(user_id=1, name = "Lo Mai Chi", description = "Soft, peanut-filled mochi balls", preptime = "40 mins", course = "Desserts", cuisine = cuisine2)
session.add(recipe8)
session.commit()

recipe9 = Recipe(user_id=1, name = "Rice Wine", description = "Fermented rice starch converted into sugars", course = "Beverages", cuisine = cuisine2)
session.add(recipe9)
session.commit()

recipe10 = Recipe(user_id=1, name = "Bubble Tea", description = "Ice-blended versions are usually mixed with more ice, resulting in a slushy consistency with small chewy tapioca balls", course = "Beverages", cuisine = cuisine2)
session.add(recipe10)
session.commit()

# Italian Cuisine Recipes

cuisine3 =  Cuisine(user_id=1, name = "Italian")
session.add(cuisine3)
session.commit()

recipe1 = Recipe(user_id=1, name = "Meatball", description = "Three seasoned meatballs atop a bed of pasta covered in a rich, meaty tomato sauce", preptime = "40 mins", course = "Appetizers", cuisine = cuisine3)
session.add(recipe1)
session.commit()

recipe2 = Recipe(user_id=1, name = "Italian Sausage", description = "Pork sausage with some fennel seeds and chilli", preptime = "30 mins", course = "Appetizers", cuisine = cuisine3)
session.add(recipe2)
session.commit()

recipe3 = Recipe(user_id=1, name = "Antipasto", description = "A course of appetizers consisting of an assortment of foods, as olives, anchovies, sliced sausage, peppers, and artichoke hearts", preptime = "30 mins", course = "Appetizers", cuisine = cuisine3)
session.add(recipe3)
session.commit()

recipe4 = Recipe(user_id=1, name = "Sausage and Rice Timbale", description = "Savory sausage filling tucked inside a cheesy arborio rice shell", preptime = "2 hours", course = "Entrees", cuisine = cuisine3)
session.add(recipe4)
session.commit()

recipe5 = Recipe(user_id=1, name = "Cranberry Bean Pasta Fagioli", description = "Healthy soup is packed with plant-based protein, kale, noodles, spices and tomatoes", preptime = "3 hours", course = "Entrees", cuisine = cuisine3)
session.add(recipe5)
session.commit()

recipe6 = Recipe(user_id=1, name = "Roasted Cauliflower Risotto", description = "Cauliflower with roasted almonds and rice with some parsley and fontina", preptime = "40 mins", course = "Entrees", cuisine = cuisine3)
session.add(recipe6)
session.commit()

recipe7 = Recipe(user_id=1, name = "Tiramisu", description = "Coffee-flavoured Italian Dessert made of ladyfingers dipped in coffee, layered with a whipped mixture of eggs, sugar, and mascarpone cheese, flavoured with cocoa", preptime = "2 hours", course = "Desserts", cuisine = cuisine3)
session.add(recipe7)
session.commit()

recipe8 = Recipe(user_id=1, name = "Cannoli", description = "Tube-shaped Italian pastry filled with sweet cream and ricotta cheese, sometimes with candied fruit or chocolate sprinkles", preptime = "2 hours", course = "Desserts", cuisine = cuisine3)
session.add(recipe8)
session.commit()

recipe9 = Recipe(user_id=1, name = "Aperol", description = "Wine-based cocktail made with bitter liquor and a splash of soda.", course = "Beverages", cuisine = cuisine3)
session.add(recipe9)
session.commit()

recipe10 = Recipe(user_id=1, name = "Campari", description = "Alcholic liquor obtained from the infusion of herbs and fruits", course = "Beverages", cuisine = cuisine3)
session.add(recipe10)
session.commit()

# Indian Cuisine Recipes

cuisine4 =  Cuisine(user_id=1, name = "Indian")
session.add(cuisine4)
session.commit()

recipe1 = Recipe(user_id=1, name = "Chilli Chicken", description = " Indo-Chinese style chicken appetizer with a lot of spicy gravy", preptime = "3 hours", course = "Appetizers", cuisine = cuisine4)
session.add(recipe1)
session.commit()

recipe2 = Recipe(user_id=1, name = "Paneer Tikka", description = "Chunks of Indian cottage cheese marinated in spices and grilled in a tandoor", preptime = "30 mins", course = "Appetizers", cuisine = cuisine4)
session.add(recipe2)
session.commit()

recipe3 = Recipe(user_id=1, name = "Tangri Kebabs", description = "Delicious mouth melting appetizer prepared by soft, moist chicken marinated in aromatic Indian spices", preptime = "30 mins", course = "Appetizers", cuisine = cuisine4)
session.add(recipe3)
session.commit()

recipe4 = Recipe(user_id=1, name = "Chicken Biriyani", description = "Basmati rice flavored with cloves, cinnamon, cardamon, bay leaf, coriander, mint, ginger, garlic and onions and chicken meat cubes", preptime = "2 hours", course = "Entrees", cuisine = cuisine4)
session.add(recipe4)
session.commit()

recipe5 = Recipe(user_id=1, name = "Palak Paneer", description = "Indian cottage cheese in spinach gravy", preptime = "30 mins", course = "Entrees", cuisine = cuisine4)
session.add(recipe5)
session.commit()

recipe6 = Recipe(user_id=1, name = "Masala Dosa", description = "Stuffed dosa with a lightly cooked filling of potatoes, fried onions and spices", preptime = "10 hours", course = "Entrees", cuisine = cuisine4)
session.add(recipe6)
session.commit()

recipe7 = Recipe(user_id=1, name = "Gulab Jamun", description = "Deep fried balls made of milk powder, flour, butter and cream or milk, soaked in sugar syrup", preptime = "50 mins", course = "Desserts", cuisine = cuisine4)
session.add(recipe7)
session.commit()

recipe8 = Recipe(user_id=1, name = "Falooda", description = "Cold dessert made from mixing rose syrup, vermicelli, sweet basil seeds, and pieces of jelly with milk, often topped off with a scoop of ice cream", preptime = "20 mins", course = "Desserts", cuisine = cuisine4)
session.add(recipe8)
session.commit()

recipe9 = Recipe(user_id=1, name = "Lassi", description = "Savoury drink, flavoured with ground and roasted cumin.", course = "Beverages", cuisine = cuisine4)
session.add(recipe9)
session.commit()

recipe10 = Recipe(user_id=1, name = "Chaas", description = "Flavoured and seasoned buttermilk", course = "Beverages", cuisine = cuisine4)
session.add(recipe10)
session.commit()

# Mexican Cuisine Recipes

cuisine5 =  Cuisine(user_id=1, name = "Mexican")
session.add(cuisine5)
session.commit()

recipe1 = Recipe(user_id=1, name = "Guacamole", description = "A dip made of ripe mashed avocados & sea salt", preptime = "10 mins", course = "Appetizers", cuisine = cuisine5)
session.add(recipe1)
session.commit()

recipe2 = Recipe(user_id=1, name = "Salsa", description = "Plum tomatoes blended with onions, cilantro and serrano peppers into a smooth sauce", preptime = "40 mins", course = "Appetizers", cuisine = cuisine5)
session.add(recipe2)
session.commit()

recipe3 = Recipe(user_id=1, name = "Nachos", description = "Tortilla chips covered with cheese or a cheese-based sauce", preptime = "20 mins", course = "Appetizers", cuisine = cuisine5)
session.add(recipe3)
session.commit()

recipe4 = Recipe(user_id=1, name = "Enchiladas suizas", description = "Enchiladas suizas are topped with a white, milk or cream-based sauce, such as bechamel", preptime = "1 hour", course = "Entrees", cuisine = cuisine5)
session.add(recipe4)
session.commit()

recipe5 = Recipe(user_id=1, name = "Chicken in salsa verde tamales", description = "Tamales are made from delicate corn dough, wrapped in corn husks or banana leaves, and then steamed", preptime = "3 hours 30 mins", course = "Entrees", cuisine = cuisine5)
session.add(recipe5)
session.commit()

recipe6 = Recipe(user_id=1, name = "Chiles rellenos de puerco", description = "Poblano chiles that are stuffed with pork, beef or cheese and then are battered and fried and served covered in salsa roja", preptime = "50 mins", course = "Entrees", cuisine = cuisine5)
session.add(recipe6)
session.commit()

recipe7 = Recipe(user_id=1, name = "Rice Pudding", description = "Rice mixed with water or milk and other ingredients such as cinnamon and raisins", preptime = "35 mins", course = "Desserts", cuisine = cuisine5)
session.add(recipe7)
session.commit()

recipe8 = Recipe(user_id=1, name = "Flan", description = "A dessert of sweetened egg custard with a caramel topping", preptime = "1 hour 20 mins", course = "Desserts", cuisine = cuisine5)
session.add(recipe8)
session.commit()

recipe9 = Recipe(user_id=1, name = "Atole", description = "Masa toasting on a griddle with cinnamon flavored water", course = "Beverages", cuisine = cuisine5)
session.add(recipe9)
session.commit()

recipe10 = Recipe(user_id=1, name = "Sangria", description = "Red wine mixed with fruits, such as pineapple, peaches, nectarines, berries, apples, pears, or melon, sweetened with sugar and orange juice", course = "Beverages", cuisine = cuisine5)
session.add(recipe10)
session.commit()

# Caribbean Cuisine Recipes

cuisine6 =  Cuisine(user_id=1, name = "Caribbean")
session.add(cuisine6)
session.commit()

recipe1 = Recipe(user_id=1, name = "Tostones", description = "A  thick slice of green plantain that is fried, flattened, and then fried again", preptime = "10 mins", course = "Appetizers", cuisine = cuisine6)
session.add(recipe1)
session.commit()

recipe2 = Recipe(user_id=1, name = "Pionono", description = "Peruvian dessert made with a soft and light sponge cake", preptime = "3 hours 10 mins", course = "Appetizers", cuisine = cuisine6)
session.add(recipe2)
session.commit()

recipe3 = Recipe(user_id=1, name = "Alcapurria", description = "Scrumptious fritters made with a batter of taro and green bananas stuffed with a meat", preptime = "1 hour", course = "Appetizers", cuisine = cuisine6)
session.add(recipe3)
session.commit()

recipe4 = Recipe(user_id=1, name = "Caribbean Jerk Stir-Fry", description = "Chicken is marinated with spices, lime juice, sugar and Jalapeno pepper and then stir-fried", preptime = "30 mins", course = "Entrees", cuisine = cuisine6)
session.add(recipe4)
session.commit()

recipe5 = Recipe(user_id=1, name = "Caribbean Grilled crab cakes", description = "A golden crisp mixture of crabmeat, bread crumbs, mayonnaise, egg, green onions and hot sauce", preptime = "1 hour", course = "Entrees", cuisine = cuisine6)
session.add(recipe5)
session.commit()

recipe6 = Recipe(user_id=1, name = "Grilled Caribbean chicken breasts", description = "Marinated chicken with a combination of orange juice, orange peel, olive oil, lime juice, ginger, garlic, hot pepper sauce and oregano", preptime = "20 mins", course = "Entrees", cuisine = cuisine6)
session.add(recipe6)
session.commit()

recipe7 = Recipe(user_id=1, name = "Far Breton", description = "Classic French dessert, a rich, dense custard with dried fruit imbibed with Armagnac, brandy or rum", preptime = "35 mins", course = "Desserts", cuisine = cuisine6)
session.add(recipe7)
session.commit()

recipe8 = Recipe(user_id=1, name = "Coconut Macaroon", description = "Small round biscuits, typically made from ground almonds, coconut with the sweetened condensed milk and vanilla", preptime = "45 mins", course = "Desserts", cuisine = cuisine6)
session.add(recipe8)
session.commit()

recipe9 = Recipe(user_id=1, name = "Peach Mango smoothie", description = "Mango chunks, sliced peach, vanilla yogurt and crushed ice into a thick smoothie", course = "Beverages", cuisine = cuisine6)
session.add(recipe9)
session.commit()

recipe10 = Recipe(user_id=1, name = "Citrus Punch", description = "Combination of orange, tangerine and lemon flavors into one lethal dose", course = "Beverages", cuisine = cuisine6)
session.add(recipe10)
session.commit()






print "Added recipes for all the cuisines"