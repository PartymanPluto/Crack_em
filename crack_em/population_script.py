import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'crack_em.settings')

import django
django.setup()
from crack_app.models import Egg, Recipe
from django.contrib.auth.models import User

def populate():
    #EGG_TYPES = ['omlette', 'fried', 'scrambled', 'poached', 'sauce', 'other']
    recipes = [
            {"title": "Olly's omlette for 1", 
             "author": "Jolly Olly",
             "egg_type": "omlette",
             "ing": """Eggs : 2 , water : 2 tbsp , salt : 1/8 tsp ,
             pepper : a dash, butter : 1 tsp , filling of choice : 1/3 cup""",
             "inst": """ Beat the eggs, water, salt and pepper in a 
             small bowl until blended.; Heat butter in 6 to 8-inch omelette pan
             or skillet over medium-high heat until hot. Tilt the pan to coat
             the bottom before pouring in the egg mixture.; Using a spatula or
             otherwise, keep the cooked parts of the omlette from the edges of
             the pan towards the center and turn the pan so that uncooked parts
             can reach the pan surface. Continue doing this as needed.; When
             no liquid egg is visible and the cooked egg is thickened, place
             the filling on one side of the omlette before folding the omlette
             in half and sliding the omlette onto a plate.; Enjoy your omlette,
             bon appetit!"""},
            {"title": "Spaceman's spectacular spanish omlette for 4",
             "author": "Spaceman2156",
             "egg_type": "omlette",
             "ing": """eggs : 6, potatoes : 500g, white onion : 1, 
             olive oil(extra-virgin) : 150ml, flat-leaf parsley : 3 tbsp""",
             "inst":"""Prep: Peel all 500g of potatoes and then cut 
             them up into thick slices. Chop your onion and heat the olive
             oil in a (preferably large) frying pan.; 
             Once the pan has been heating for a minute or 2, add the potatoes 
             and onion before stewing gently until the potatoes are softened 
             (roughly half an hour). Make sure the pan is partially covered 
             whilst stewing and give it the ocassional stir.;
             Once the stewing is finished, strain the potatoes and onion 
             through either into a large bowl (leaving the strained oil to 
             one side for now). ;
             Beat 6 eggs separately, then stir them all into the potatoes with 
             the parsley and plenty of seasoning.;
             Take the strained oil from earlier and heat just little bit of it 
             in a smaller pan before tipping everything into the pan and 
             cooking it at a moderate heat. Whilst this is cooking, make sure
             to use a spatula to keep the omlette in a cushion-like shape. ;
             When the omlette is almost set, invert it onto a plate and slide 
             it back onto the pan and cook for a few more minutes. ; 
             Repeat the previous two steps another two times before sliding 
             the omlette onto a plate and leaving it to cool for 10 minutes."""
             },
            {"title":"Fried eggs 'sunny side on Leith' up",
             "author": "Poached proclaimer",
             "egg_type": "fried",
             "ing": """eggs: as many as needed, Plenty of olive oil 
             and butter: """,
             "inst": """Add enough oil to the pan so that it just 
             thinly coats the bottom. Turn the heat to high and get the pan 
             and the oil really hot, so that the oil shimmers and flickers. 
             When it does, crack an egg into the pan. When the edges begin to 
             hold their shape, even beginning to brown slightly, wet your 
             fingers and flick a few drops of water into the frying pan around 
             the egg, and cover the egg with a lid. Keep an eye on the egg and 
             after 20 to 30 seconds, the white will be slightly puffed and 
             just-cooked through, the yolk still shiny and runny."""
             },
            {"title": "Mama's homemade cheesy scrambled eggs",
             "author": "Tutankhamun",
             "egg_type": "scrambled",
             "ing": """eggs: two, milk: a splash, cheese: way too much,
             salt & pepper: a pinch each""",
             "inst": """Beat the two eggs in a small bowl until they 
             are of a uniform consistency whilst pre-heating a small pot or 
             frying pan. ; 
             Put the milk and cheese in the pot/pan, gently stirring the 
             cheese as it melts. ;
             When the cheese has melted and the milk starts to curd, pour the 
             egg mixture in and mix with the milk and cheese. ;
             Add the salt & pepper to the mix and cook for a few minutes, 
             keeping the mixture form sticking to the bottom/sides of the 
             pot/pan by using a spatula. ; 
             Once the mixture is sufficiently fluffy, turn off the heat and 
             move the newly made eggs onto a plate, ready to serve!""" },
            {"title": "Green eggs and ham",
             "author": "Sam I am",
             "egg_type" : "poached",
             "ing": """Free-range eggs : 12, English muffins : 6, 
             white vinegar : 2 Tbsp, Oil : a splash, Spinach : 6 handfuls, 
             High quality ham : 12 slices, Pesto sauce/hollandaise : as needed 
             but roughly 500g""",
             "inst": """Heat an oven to 100C. ;
             Place a saucepan of salted water on the heat and bring to the 
             boil, then add the white vinegar. ;
             Toast the english muffins and then keep them warm in the oven 
             thereafter.;
             Heat a skillet to medium/high heat. Add the oil, and fry the ham 
             until golden brown and crispy around the edges. Keep warm in the 
             oven alongside the muffins. ;
             Using the same skillet as before, wilt the spinach - adding a 
             tablespoon of water to aid the process. ;
             Cook until the leaves just become soft. Hold in the pan, season 
             with a little salt and freshly ground black pepper. ;
             Turn the pan water down to a gentle simmer. Poach the eggs to 
             your desired doneness. ;
             Place the english muffins on warrm plates. Top with the hame, 
             spinach and poached eggs before finally covering everything with 
             as much pesto hollandaise as your heart desires. """
             },
            {"title": "The 'Why so serious' side egg salad",
             "author": "ThE YoKEr42069",
             "egg_type": "sauce",
             "ing": """peeled, hard-boiled eggs : 12, chopped green 
             onion : 1/4 cup, chopped celery : 1/2 cup, chopped red bell 
             pepper : 1/2 cup, Djon mustard : 2 Tbsp, mayonaise : 1/3 cup, 
             cider(preferably dark fruits) : 1 Tbsp, Tabasco : 1/4 tsp, 
             paprika : 1/2 tsp, black pepper : 1/2 tsp, slat : 1/4 tsp""",
             "inst": """Prep: To hard boil eggs, place them a saucepan 
             or small pot and cover with water. Bring to boil, then remove from
             heat, cover with cold water for a minute and leave for 5 minutes.;
             Chop the eggs coarsely and put them into a large bowl. Add the 
             green onion, celery and red bell pepper. ;
             In a small bowl, mix together the mayo, mustard, cider (it better 
             be dark fruits!) and Tabasco. Gently stir the mayo dressing into 
             the bowl with the eggs and vegetables and add the paprika, salt 
             and black pepper to taste."""
             },
            {"title": "Killer Queen's 'sheer heart attack inducing' scotch eggs",
             "author": "Hand lover99",
             "egg_type": "other",
             "ing": """eggs : 8 , plain sausage meat : 450g, mixed 
             herbs (chopped) : 3 tbsp, ground mace: a pinch, mustard : 1 tbsp,
             milk : a splash, flour : 50g, breadcrumbs : 100g, vegitable oil : 
             as needed""", 
             "inst":"""Put six of the eggs into a pan, cover with cold
             water and bring to the boil . Turn down the heat and simmer for 
             five minutes, then put straight into a large bowl of iced water 
             for at least ten minutes. ;
             Put the meat, herbs, mace and mustard into a bowl, season and mix 
             well with your hands before dividing them into six. ;
             Carefully peel the eggs. Beat the two raw eggs together in a bowl 
             with a splash of milk. Put the flour in a second bowl and season, 
             then tip the breadcrumbs into a third bowl. Arrange in an assembly 
             line. ;
             Put a square of clingfilm on the worksurface, and flour lightly. 
             Put one of the meatballs in the centre, encase an egg and remove 
             the top sheet of clingfilm. ;
             To assemble the egg, roll one peeled egg in flour, then put it in 
             the centre of the meat. Bring up the sides of the film to encase 
             it, and smooth it into an egg shape with your hands. Dip each egg 
             in flour, then egg, then breadcrumbs, then egg and then 
             breadcrumbs. ;
             Fill a large pan a third full of vegetable oil, and heat to 170 
             degrees celsius. Cook the eggs a couple at a time, for seven 
             minutes, until crisp and golden, then drain on kitchen paper 
             before serving."""
             }]
    
    #for egg in EGG_TYPES:
        #add_egg(egg)
    for rec in recipes:
        author = add_user(rec["author"])
        add_recipe(rec["title"], author, rec["egg_type"], 
                   rec["ing"], rec["inst"])
        print("- {0} - [1]".format(rec["title"]))

#def add_egg(t):
 #   e = Egg.objects.get_or_create(title=t)
  #  return e

def add_recipe(t, a, et, ing, inst):
    r = Recipe.objects.get_or_create(title=t, author=a, egg_type=et, 
                                     ingrediants=ing, instructions=inst)[0]
    r.views = 0
    r.likes = 0
    r.average_rating = 0
    r.save()
    return r

def add_user(name):
    user = User.objects.get_or_create(username=name, password = None, email=None)[0]
    return user

if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()













