#Ultimate
This tool will be developed in my free time to handle forensics-related challenges that occur repeatedly in CTFs and wargames. Such examples of repetitive challenges include recursive compression, file header repairs, LSB Stego, hidden files, and much more. 


## Installation
   - Download ZIP
   - Unzip in working directory
   - Run the following: `python ultimate.py`
   - ???
   - Profit

## Dependencies
To use all utilities included in this tool, you need the following installed:
NOTE: Tested with apt-get/yum packages unless otherwise specified
   - Volatility
   - Yara --> Install from here (http://yara.readthedocs.org/en/latest/gettingstarted.html#compiling-and-installing-yara), not through apt or pip.
   - autoconf
   - automake
   - libtool
   - sleuthkit
   - 

## Notes
   - When entering the full path, do not backslash-escape spaces:
   - `/mnt/hgfs/Mint\ Shared/mem_capt.mem` <-- NO
   - `/mnt/hgfs/Mint Shared/mem_capt.mem` <-- YES

## Working Components
   - ~~Disk~~
   - Memory
   - ~~Network~~
   - ~~Picvideo~~
   - ~~Archive~~
   - ~~Unknown~~

## To Do
   - Make environmental variables for profile and file for Volatility
   - Create tool_dependencies.sh file that will auto-install all dependencies (assuming up-to-date Ubuntu 15.04 OS)
   - Incorporate registry hive extraction into memory toolset
