#gif-hook
========

A pre-commit hook for Git that creates GIFs showing the evolution of any image files.

##Usage
Copy `pre-commit` into the `.git/hooks/` folder of your project.

Each time you make a commit, the hook will check whether there are any staged image files. If the image file is being added for the first time, the hook will create a new, single frame GIF. This GIF is created in a folder called `gifs` that is located in the same directory as the image file. If the image has been modified, the hook will add the current version of the image as a new frame in the previously created GIF.

##Future Plans
There is much that can be added to improve the hook. Here are some of those plans:

* Make more configurable
* Specify exclusion/inclusion paths
* Image scaling
* User-specified GIF storage location
* Option to delete gifs of any images that get deleted
* Overlay datetime / commit message (or generate a web page showing the evolution with the commit message side-by-side)

Please feel free to suggest ideas, or contribute :)

##Example
Here's the evolution of a landscape painting that I created earlier.

![](https://github.com/jrwilliams/gif-hook/blob/master/example/gifs/landscape.gif)