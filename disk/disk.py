''' The following tools are used:
- Sleuthkit
- binwalk
'''

class Disk():
    def __init__(self, filename):
        print "Hello, I am disk"
        self.filename = filename
        self.diskType = self.identifyFileType()
                
        print "The first tool we will use is binwalk\n"
        self.runBinWalk()
        print "Now we will use Sleuthkit\n"
        self.runSleuthkit()
        
    def identifyFileType(self):
        print "What is the filetype of your file?\n"
        print "1) RAW disk image"
        print "2) ext2 disk image"
        print "3) ext3 disk image"
        print "4) ext4 disk image"
        print "5) Fat32 disk image"
        print "6) NTFS disk image"
        print "7) HFS disk image"
        print "8) Unknown"
        types = {1: "raw", 2: "ext2", 3: "ext3", 4: "ext4", 5 : "fat32", 6: "ntfs", 7: "hfs", 8: "unknown" }
        t = raw_input("")
        try:
            t = int(t)
            if t > 0 and t < 8:
                return types[t]
            if t == 8:
                print "Ok, let me figure it out for you..."
                #TODO: disk type analysis tool will run 
                
        
