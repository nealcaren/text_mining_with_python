# Using Jupyter Notebooks

```{note}
This is a modified version of "[Introduction to Jupyter Notebooks](https://programminghistorian.org/en/lessons/jupyter-notebooks)" by 
Quinn Dombrowski, Tassie Gniady, and David Kloster originally published at [The Programming Historian](https://programminghistorian.org/en/). 
```

## Launching Jupyter Notebook

Assuming you've already installed Anaconda as described above, you can launch Anaconda Navigator like any other software application. (You can close the prompt about creating an Anaconda Cloud account; you don't need an account to work with Anaconda.) On the home screen, you should see a set of icons and brief blurbs about each application included with Anaconda.

Click on the "Launch" button under the *Jupyter Notebook* icon.

![Anaconda Navigator interface](https://programminghistorian.org/images/jupyter-notebooks/anaconda-navigator.png)



If you prefer to use the command line instead of Anaconda Navigator, once you have Anaconda installed, you should be able to open a new Terminal window (Mac) or Command Prompt (Win) and run <code>jupyter notebook</code> to launch the web browser with the Jupyter Notebook application. If you are using the command line to launch Jupyter Notebook, pay attention to the directory you are in when you launch it. That folder becomes the home directory that will appear immediately in the Jupyter Notebook interface, as described below.

Either approach will open up a new window or tab in your default browser with the Jupyter Notebook interface. Jupyter Notebook is browser-based: you only interact with it through your browser, even when Jupyter Notebook is running on your own computer.


## Navigating the Jupyter Notebook interface

The Jupyter Notebook file browser interface is the main way to open a Jupyter notebook (.ipynb) file. If you try to open one in a plain text editor, the notebook will be displayed as a JSON file, not with interactive code blocks. To view a notebook through the Jupyter interface, you have to launch Jupyter Notebook first (which will display in a browser window), and open the file from within Jupyter Notebook. Unfortunately, there is no way to set Jupyter Notebook as the default software application to open .ipynb files when you double-click on them.

When you launch Jupyter Notebook from Anaconda Navigator, it automatically displays your home directory. This is usually the directory with your username on a Mac (/Users/*your-user-name*). On a PC it is usually C:\\. If you launch Jupyter Notebook from the command line, it will display the contents of the folder you were in when you launched it. (Using the command line, you can also directly launch a specific notebook, e.g. `jupyter notebook example.ipynb`.)

To avoid cluttering this folder, you can make a new folder within this directory for your notebooks. You can either do this in your usual file management interface (Finder on Mac, or File Explorer on Windows), or within Jupyter Notebook itself, since Jupyter Notebook, much like Google Drive, provides a file management interface within a browser, as well as a menu-and-toolbar UI for authoring files. To add a new folder within Jupyter Notebook, click on *New* in the upper right, and choose *Folder*. This will create a new folder called "Untitled Folder". To change the name, click the checkbox to the left of the "Untitled Folder", then click on the "Rename" button that appears under the "Files" tab. Name the folder *notebooks*. Click on it to open that folder.

## Moving in Files

If you want to add data files or notebooks, you can do that directly from within the Jupyter Notebook file browser. Towards the upper right, click the "Upload" button and upload your file. It is convient to have all related files in the same directory or sets of subdirectories.

![Uploading files in the Jupyter Notebook interface](https://programminghistorian.org/images/jupyter-notebooks/jupyter-upload.png)

Note that this isn't the only way to make files appear in the Jupyter Notebook file browser. The *notebooks* folder you created is a regular directory on your computer, and so you can also use your usual file management interface (e.g. Finder on Mac, or File Explorer on Windows) to put .ipynb and/or data files in this directory. Jupyter notebooks use the location of the notebook file itself (the .ipynb file) as the default starting path. For workshops and courses, it may make sense to create a folder where you can store the notebook, any attached images, and the data you're going to work with, all together. If everything isn't in the same folder, you'll have to include the path when referencing it, or use Python code within the notebook to change the working directory.


## Creating a new notebook

Inside the *notebooks* folder, create a new Jupyter notebook to use to convert the dates for your research project. Click the "New" button in the upper right of the Jupyter Notebook file browser interface. If you've just installed Anaconda as described above, your only option will be to create a Jupyter notebook using the Python 3 *kernel* (the backend component that actually runs the code written in the notebook), but we'll discuss below how to add kernels for other languages. Click on "Python 3", and Jupyter Notebook will open a new tab with the interface for Jupyter notebooks themselves. By default, the notebook will be named "Untitled"; you can click on that text at the top of the screen to rename it.

![Creating a new Jupyter notebook](https://programminghistorian.org/images/jupyter-notebooks/jupyter-createnew.png)

### Working in Jupyter notebooks

A notebook is made up of *cells*: boxes that contain code or human-readable text. Every cell has a type, which can be selected from the drop-down options in the menu. The default option is "Code"; human-readable text boxes should use the "Markdown" type, and will need to be written using Markdown formatting conventions. To learn more about Markdown, see the ["Getting Started With Markdown"](/en/lessons/getting-started-with-markdown) Programming Historian lesson.

When you create a new Jupyter notebook, the first cell will be a code cell. At the top of the Jupyter Notebook interface is a toolbar with functions that apply to the currently-selected cell. One of the functions is a dropdown that reads "Code" by default. Click on this dropdown and select "Markdown". (You can also use a keyboard shortcut, *esc + m*, to change the current cell to Markdown, and *esc + y* changes it back to a code cell.) We'll start this notebook with a title and a brief explanation of what the notebook is doing. For the moment, this is just for your own memory and reference; you don't want to invest too much in prose and formatting at this stage of the project, when you don't know whether you'll end up using this code as part of your final project, or if you'll use a different tool or method. But it can still be helpful to include some markdown cells with notes to help you reconstruct your process.

Paste the following into the first cell. If it doesn't appear with the first line in a large font (as a header), make sure you've selected "Markdown" from the dropdown at the top.

```
# First Notebook
Playing around with a Juypter notebook
```


## First Notebook
Playing around with a Juypter notebook

When you're editing a cell, you can use Ctrl + Z (Win) or Command + Z (Mac) to undo changes that you've made. Each cell retains its own edit history; even if you move to a different cell and make edits there, you can subsequently click back on the first cell and undo your earlier changes there, without losing the changes to the second cell.

To leave editing mode and "run" this cell (for a Markdown cell, this doesn't *do* anything, just moves you further down the notebook), you can click <i class="fa-step-forward fa"></i> in the toolbar or press Ctrl+Enter (Ctrl+Return on Mac). If you want to resume editing it later, you can either double-click it, or select the cell (which will show a vertical blue line on the left once it's selected) by clicking it once, and then hitting the Enter (Win) or Return (Mac) key. To leave editing mode, you can click <i class="fa-step-forward fa"></i> in the toolbar or press Ctrl+Enter (Ctrl+Return on Mac). If you want to run your current cell and add a new cell (by default, a code cell) immediately below it, you can press Alt+Enter (Option+Enter on Mac).


To add a new cell, click the plus button <i class="fa fa-plus"></i> in the toolbar (or use the *esc + b* keyboard shortcut). This will create a new code cell below the cell that's currently selected. Create a new code cell, to print 'hello'.

``` py
print("Hello")
```


Clicking the <i class="fa-step-forward fa"></i> button in the toolbar when you have a Code cell selected executes the code inside the cell. 

After you run a code cell, a number will appear in brackets to the left of the cell. This number indicates the order in which the cell was run. If you go back and run the cell again, the number is updated.

If a number doesn’t immediately appear next to the cell, you’ll see an asterisk in brackets. This means that the code cell hasn’t finished running. This is common for computationally-intensive code (e.g. natural language processing) or long-running tasks like web scraping. Whenever a code cell is running, the favicon in the notebook’s browser tab changes to an hourglass . If you want to change tabs and do something else while the code is running, you can tell that it’s done when the hourglass changes back to the notebook icon .

Jupyter notebooks work best if you run the cells sequentially. Sometimes you can get errors or incorrect outputs if you run the cells out of order or attempt to iteratively edit and run different parts of the notebook. If you've made lots of changes and run code blocks in a non-linear fashion and find that you're getting strange output, you can reset Jupyter Notebook by clicking on Kernel in the menu and choosing Restart & Clear Output. Even if you don't notice anything strange, it's a good idea to do Restart & Clear Output and re-run your code once you've finished writing it, to make sure the output is accurate.

## Saving, exporting, and publishing Jupyter notebooks

Jupyter autosaves your work periodically by creating "checkpoints". If something goes wrong with your notebook, you can revert to a previous checkpoint by going to "File", then "Revert to Checkpoint", and choosing a timestamp. That said, it's still important to save your notebook (using the save button <i class="fa fa-floppy-o"></i>), because if you close and shut down the notebook kernel (including restarting the kernel), the checkpoints will be lost.

You can also download the notebook (*File > Download as*) in several different file formats. Downloading the Notebook format (.ipynb) is useful if you want to share your code in its full notebook format. You can also download it as code in whatever language your notebook is in (e.g. .r if in R or .py if Python or .js if JavaScript), as an .html file, as a markdown (.md) file, or as a PDF via LaTeX. If you download it as code, the Markdown cells become comments. (If you want to convert an .ipynb file to another format after you've downloaded it, you can use the [nbconvert utility](https://github.com/jupyter/nbconvert).)

If you're working on a research project, you can use a Jupyter notebook, or a series of notebooks, along the way to keep track of your workflow. Some scholars post these notebooks on GitHub, along with slides or poster PDFs, and source data (or metadata, copyright permitting), to accompany presentations and talks. GitHub renders non-interactive versions of notebook files, so they can be previewed within a repo. Alternately, you can paste the URL of a GitHub repo that has Jupyter notebooks into [nbviewer](https://nbviewer.jupyter.org/), which can sometimes a faster and more reliable preview. You may want to include a Markdown cell with a recommended citation for your Jupyter notebook, and a pointer to the GitHub repo where it is stored, especially if your notebook includes code that others might be able to reuse for similar analyses.

The code you just developed as part of this lesson belongs somewhere in the middle of a real project. If you're using notebooks to document your workflow, you might choose to add the new code cell to an existing notebook, rather than downloading it as a separate, stand-alone notebook. Jupyter notebooks can be particularly helpful for documenting project workflows when you're working with collaborators who may only be involved for a short period of time (such as summer undergraduate interns). With short-term collaborators, it's important to help them understand and start using the project's workflows without a lot of start-up time, and Jupyter notebooks can lay out these workflows step-by-step, explain where and how files are stored, and provide pointers to external tutorials and training materials to help collaborators who are less familiar with the project's technical underpinnings get started. 

As your project progresses, if you're publishing through open-access channels, and your data sets can be freely redistributed, Jupyter notebooks can provide an ideal format for making the code underpinning your scholarly argument visible, testable, and reusable. While journals and presses may not accept Jupyter notebooks as a submission format, you could develop a notebook "version" of your paper that includes the full text (as Markdown cells), with code cells integrated into the flow of the scholarly narrative as an immediately accessable illustration of the analysis you're describing. You could also include the code cells that make up the data preparation workflows as an appendix, either in the same notebook, or in a separate one. Integrating the code with the text of a scholarly article makes it far more likely that readers will actually engage with the code, since they can simply run it within the same notebook where they're reading the argument. Some scholars, particularly in Europe, also post their notebooks to [Zenodo](https://zenodo.org/), an archive for research regardless of the country of origin, funder, or discipline. Zenodo supports data sets up to 50 GB (vs. the 100 MB file size limit on Github), and provides DOIs for uploaded material, including notebooks. Some scholars combine archiving on Zenodo for sustainability with publishing on GitHub for findability, by including the Zenodo DOI as part of the readme.md file in the GitHub repository that includes the notebooks. As an example, Giovanni Colavizza and Matteo Romanello's ["Applied Data Analytics" workshop notebook for DHOxSS 2019](https://github.com/mromanello/ADA-DHOxSS2019) is published on GitHub but includes a Zenodo DOI.

## Jupyter Notebooks for other programming languages

Jupyter Notebooks allow you to use many different programming languages including R, Julia, JavaScript, PHP, or Ruby. A current list of available languages can be found on the [Jupyter Kernels](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels) GitHub page.

While Python is supported by default when you install Jupyter Notebook through Anaconda, the other programming languages need to have their language kernels installed before they can be run in Jupyter Notebook. The installation instructions are different for each language kernel, so it is best to just find and follow the instructions for your preferred language. At least for R, this is relatively straightforward. The [Jupyter Kernels](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels) GitHub page has links to instructions for all available language kernels.

Once you have the kernel for your desired language(s) installed, you can run notebooks written in that programming language, or you can create your own notebooks that execute that language. Each language with a kernel installed on your computer will be available as an option when you create a new notebook as described above.

As an example of an R notebook, see [this Jupyter adaptation of Andrew Piper's R code from "Enumerations"](https://github.com/quinnanya/enumerations).


This work is licensed under a [Creative Commons Attribution License CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

