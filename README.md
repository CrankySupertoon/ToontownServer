Open source Toontown server built using Toontown Stride source

Features:
- Custom launcher that allows content pack support
- Saving multiple IP addresses to favorites
- Available on Mac, Windows, and Linux
- Very modular

Updates
March 11th 2019
- Used XML in order to add configurations for Panda3D

March 28th 2019
- Moved over from .bat to a QT launcher, will come shortly.

Sepetember 11th, 2019
- Currently accomplished:
    - Basic functionality of the launcher is finished, has been recoded using Pyside2
    - UI for content pack selection is finished, needs to be programmed

- Bugs:
    - Server cannot be selected on launcher due to the signal from combobox, easy fix


- Left to do:
    - Finish the content pack menu so users may select content packs within the specified directory.
    - Pack the python files and directories into a singular .exe file to install
    - Cache the location of Panda3D into a local file
    - Finish writing Linux/Mac OSX installers
    - Pretty up UI, very barebones
    - Move the folder to appdata for Windows, and other directories for other operating systems
