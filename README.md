# excitation-source-subtraction
Subtract the light source component from frequency intensity graph.

<br />

The peak intensity without excitation source model value is written to output.

The excitation source model can also be subtracted from the original data series.  This allows an approximation of the excitation signal to be more clearly graphed on its own.

<br />

The excitation source is modeled by a single exponential equation that best fits two sections of the signal:
1. The steep drop of the excitation source (shorter wavelength), and
2. The flat tail of the data where both signals have a near-zero intensity (longer wavelength)

<br />

### Commands

Run the program from `src/` with one of the commands below:
* `python run.py`
* `python 37C_run.py`

<br />

### Tests

There are a small number of unit tests for the drop-finding function.

Run from `test/` with command:
* `python -m unittest`
