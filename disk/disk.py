import subprocess
import sys
import os

''' The following tools are used:
- Sleuthkit
- binwalk
'''

class Disk():
    def __init__(self, filename):
        print "Hello, I am disk"
        self.filename = filename
        self.diskType = self.setFileType()
                
        print "The first tool we will use is binwalk\n"
        self.runBinwalk()
        sys.exit(0)
        print "Now we will use Sleuthkit\n"
        self.runSleuthkit()
        
    def setFileType(self):
        print "What is the filetype of your file?\n"
        print "1) RAW disk image"
        print "2) ext2 disk image"
        print "3) ext3 disk image"
        print "4) ext4 disk image"
        print "5) Fat32 disk image"
        print "6) NTFS disk image"
        print "7) HFS disk image"
        print "8) Unknown"
        print "9) QUIT"
        types = {1: "raw", 2: "ext2", 3: "ext3", 4: "ext4", 5 : "fat32", 6: "ntfs", 7: "hfs", 8: "unknown" }
        t = raw_input("")
        try:
            t = int(t)
            if t > 0 and t < 8:
                self.type = types[t]
            elif t == 8:
                print "Ok, let me figure it out for you..."
                self.identifyFileType()
                print "\n\n\n"
                self.setFileType()
            elif t == 9:
                sys.exit(0)
            else:
                print "Not a valid option. Please try again."
                self.setFileType()
        except ValueError:
            print "Not a valid option. Please try again."
            self.setFileType()
    def identifyFileType(self):
        subprocess.call(["fdisk", "-l", self.filename])
        
    def runBinwalk(self):
        print "Running Binwalk on file to show contents of disk (this may take a while...)\n"
        o = subprocess.check_output(["binwalk", self.filename])
        print o
        self.saveOutput("binwalk", o)
    def runSleuthkit(self):
        return 0
    
    def saveOutput(self, utility, output):
        #Takes in which utility wants to print so it can
        #name output file correctly, along with original output
        outFileName = "%s_out" % utility
        save_Option = raw_input("\nWould you like to save this output to a seperate file? (Y/n) ")
        if save_Option == "" or save_Option == "Y" or save_Option == "y":
            if os.path.isfile(outFileName):
                over_Option = raw_input("%s file already exists. Do you wish to overwrite? (y/N) " % outFileName)
                if(over_Option == "" or over_Option == "n" or over_Option == "N"):
                    newFileName = raw_input("Enter the name of the file you wish to write to: ")
                    out = open(newFileName, "wb")
                    out.write(output)
                    print "Output saved to %s" % newFileName
                    return 0
                elif over_Option == "y" or over_Option == "Y":
                    os.remove(outFileName)
                    out = open(outFileName, "wb")
                    out.write(output)
                    print "Overwrote binwalk_out file w/ new content"
                else:
                    print "Invalid option...try again"
                    self.saveOutput(utility)
            else:
                out = open(outFileName, "wb")
                out.write(output)
                print "Output saved in %s file" % outFileName
        elif save_Option == "n" or save_Option == "N":
            pass
        else:
            print "Invalid option. Please type y or n."
            self.saveOutput(utility)
  
            
        
