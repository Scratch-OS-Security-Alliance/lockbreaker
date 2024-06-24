# ![image](https://github.com/Scratch-OS-Security-Alliance/lockbreaker/assets/49661996/e9727a9a-0f50-47de-9617-4e8ca0b9cbf5) Lockbreaker
A Python utility for bypassing OpenMX password checking in the lockscreen.

# Usage
This is a command line tool. You can run it by entering the following command:

`python3 main.py -F /path/to/openmx.sb3`

### Parameters:
- **`-F`/`-filedir`** - Path to project file **(Required)**
- **`-T`/`-tmpdir`** - Path to temporary project folder (it'll wiped during use)
  - By default set to `<cwd>/tmp`.
