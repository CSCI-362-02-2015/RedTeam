#!/bin/bash

echo "<h1 style="color:red"> Contents of $PWD:</h1>" >Contents.html
echo "<HTML>" >> Contents.html
echo "<body>" >> Contents.html
ls -1>> Contents.html
echo "</body>" >> Contents.html
echo "</HTML>"
xdg-open Contents.html

