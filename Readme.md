When modifying the config file, do not change order or line number.


Planned features:

-cumulative plots
-save plots
-formidability
-black
-white as variant on green
-rework config.txt to work on .split()
-stats of average gain per morph
-tool to analyse actual gain per morph + choices
-Random population distribution - colours not being intrinsically liniked


Adding new morphs

This will be complicated. Firstly, create a new morph in the morphs folder and make sure it inherits from the abstract Morph class for the sake of OOP. Go into config.txt, and add a population parameter for the new colour; then update the Config class in config.py to include this. 
    After doing this, go to game.py and add in a for loop in the __init__ section to make sure that the new morphs are initialised if 
they need to be. Do the same for the genMorph() function. This should then be enough for it to work. Remember also to update the dictionary mappings in config to include the new colour.