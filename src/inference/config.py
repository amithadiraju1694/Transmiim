INSTRUCTION_PROMPT = """
The following text contains examples of three items and their corresponding explanations in the required format.\n

Item -> palak paneer.\n
Explanation -> Major Ingredients here: paneer ( a.k.a cottage cheese ) , palak ( spinach ).\n
How it is made: It's a savory item, made like a gravy; usually made by sauteing spices and mixing saute with boiled paneer and palak.\n
It goes well with: White basmati rice or Indian flat bread.\n
Allergens: Paneer may cause digestive discomfort and intolerance to some.\n
Food Category: Vegetarian, Vegans may not like it, as paneer is usually made from cow milk.


Item -> rumali roti.\n
Explanation -> Major Ingredients here: roti.\n
How it is made: A small soft bread, made to size of a napkin ( a.k.a 'rumal' in hindi ); usually made with a combination of whole wheat and all purpose flour.\n
It goes well with: Most indian gravies such as palak paneer, tomato curry etc.\n
Allergens: May contain gluten, which is known to cause digestive discomfort and intolerance to some.\n
Food Category: Vegetarian, Vegan.


Item -> nizami handi.\n
Explanation -> Major Ingredients here: Different veggies, makhani sauce (skimmed milk, tomato and cashew paste , indian spices), combination of nuts.\n
How it is made: Makhani sauce is added to onion-tomato based paste and bought to a boil; a Medley of veggies and gently flavored whole spices are added and boiled for small time.\n
It goes well with: Different kinds of indian flat breads, white basmati and sonamasoori rice.\n
Allergens: Presence of nuts, butter cream and makhani sauce are known to cause digestive discomfort and intolerance to some.\n
Food Category: Usually vegetarian, may include chicken or animal meat sometimes, please check with hotel.


Based on Item and explanation pairs provided above, provide similar explanation ('Major Ingredients', 'How is it made', 'It goes well with', 'Allergens' and 'Food Category') to the below item.\n
Item ->
"""

DEBUG_MODE = True

DEVICE = 'cpu'