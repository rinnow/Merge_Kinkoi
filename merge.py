import os

dir = "merged"
if not os.path.exists(dir):
	os.makedirs(dir)

with open("vcglist.csv", "r", encoding='utf8') as cglist:
    content = cglist.read().split('\n')[:-1]
    for line in content:
        line = line.split(' ')
        merge = line[0]
        merge = merge+".png"
        base = line[1]
        base = base + ".png"
        print("merging "+base +" "+ merge)
        ret = os.system("composite -gravity northeast "+ merge + " " + base + " "+dir+"/"+ merge)
        if ret !=0:
            with open("failed.log", "a+") as log:
                log.write(merge + "\n")
        
