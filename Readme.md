# WelfareTradeoffs

When modifying the config file, do not change order or line number.

## Planned features

*cumulative plots
*formidability
*black
*white as variant on green
*rework config.txt to work on .split()
*stats of average gain per morph
*tool to analyse actual gain per morph + choices
*Random population distribution - colours not being intrinsically liniked

## Getting Started

### Prerequisites

```
python3
matplotlib
PySimpleGui
```

### Installing

Install python3.

Run 'make init' to install prerequisites.

## Running the program

If you want to interface with the program using the GUI, run:

```bash
python3 GUI/gui.py
```

from the root directory of the project. If you want to run it directly, manually modify the config.txt and then run:

```bash
python3 main.py
```

from the root directory of the project.

## Supported features

This will be a long list that needs subsections. Will could maybe work on this?

## Adding new morphs

Firstly, create a new morph in the morphs folder and make sure it inherits from the abstract Morph class for the sake of OOP. Go into config.txt, and add a population parameter for the new colour; then update the Config class in config.py to include this. 
    After doing this, go to game.py and add in a for loop in the __init__ section to make sure that the new morphs are initialised if 
they need to be. Do the same for the genMorph() function. This should then be enough for it to work. Remember also to update the dictionary mappings in config to include the new colour.

## Notes on implementation

* Uses an OOP Python approach
* Interfaces with a GUI via config.txt - this is not a fantastic system but ensures that the GUI remembers previous inputs even after being closed/reopened

## Built With

* [python3](https://www.python.org/download/releases/3.0/)
* [Visual Studio Code](https://code.visualstudio.com/) 

## Contributing

* This is a good template: [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) 

## Versioning

We can use [SemVer](http://semver.org/) for versioning. 

## Authors

* **Sebastian Fenton** - *Initial work* - [link to his github](https://github.com/seb-fenton)
* **William Adams**

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

No license

## Acknowledgments

* Put inspiration here 
* Research papers
* Friends who helped etc.
* The people who gave this github template 