Rmath-python
============

This is a slightly modified version of the [standalone Rmath library from
R][Rmath], built to be used from Python. It is based on the [Rmath-julia]
library but does not alter the random number generation.


Updating
--------

To update to the latest version of R, bump the `RVERSION` file, and run `make
update`. Some additional manual changes to the headers may be necessary: these
should go in `include/Rconfig.h`.


[Rmath]: https://cran.r-project.org/doc/manuals/r-release/R-admin.html#The-standalone-Rmath-library
[Rmath-julia]: https://github.com/JuliaStats/Rmath-julia
