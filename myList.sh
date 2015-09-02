#!/bin/bash

echo "<h1 style="color:red"> Contents of $PWD:</h1>" >Contents.html
ls -1>> Contents.html
xdg-open Contents.html

