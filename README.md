![Logo](https://github.com/bambus80/freezerburn/blob/98591fd56af202f3ea8e7d2d3f9834ebb94c2afb/logo.png?raw=true "a title")

# Lockbreaker
A Python utility for bypassing OpenMX password checking in the lockscreen.

# Usage
This is a command line tool. You can run it by entering the following command:

`python3 main.py -F /path/to/openmx.sb3`

### Parameters:
- **`-F`/`-filedir`** - Path to project file **(Required)**
- **`-T`/`-tmpdir`** - Path to temporary project folder (it'll wiped during use)
  - By default set to `<cwd>/tmp`.
