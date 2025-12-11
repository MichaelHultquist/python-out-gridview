
# Python Out-Gridview Overview

<p align = "center"><img src = "images/python-outgridview.jpg"><br/></p>

# Purpose

This module is designed to allow visualization of data contained in nested arrays in a tabular format. It is designed to emulate the functionality of the PowerShell Out-Gidview command by accepting arrays as input and sorting and displaying them on the screen in a GUI window.

This is helpful when creating data structures from returned API or query information to confirm the data structure is what is desired and is populated correctly.

# How to Use

To use this module copy to working directory containing your Python code and make sure file name matches the import command.
The module accepts three inputs:

> The columns for the grid to display. 
* Data Type: Array
* Example: columns = ["Name","Gender","Age","Hair Color"]


> The data to display. 
* Data Type: Array of Arrays 
* Example: InputArray = [["Tim","boy","16","blonde"],["Tina","girl","14","brown"]]

> A name for the grid.
* Data type: String
* Example: S3 Bucket Data

Example Usage:

```python
import outGridviewPy

columns    = ["Name","Gender","Age","Hair Color"]
InputArray = [["Tim","boy","16","blonde"],["Tina","girl","14","brown"]]
name       = "Kids in School"

outGridviewPy.outGridview(InputArray,columns,name)

```

