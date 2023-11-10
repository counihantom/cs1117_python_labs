poem = open("./debanks.txt", "r")

"""
 readline does the job of reading 1 line only.
 So I need to iterate over the file to read each
 next line.

 I'll use a counter to track what line I'm on
 and use that also to print it as an index.

 When I call readline, it sticks in a newline.
 So when I ran this without, I had extra newlines
 so I neded to strip these out before printing.
"""

line = poem.readline()
lineCount = int(1)
while line:
    print("Line Number ", lineCount, ":", line.strip("\n"))
    line = poem.readline()
    lineCount +=1

poem.close()

"""
 readlines is more advanced, cos I now get an array of the 
 entire file lines. So I can iterate over that.

 I still have the same strip problem which I need to address.
"""

poem = open("./debanks.txt", "r")

lineList = poem.readlines()
lineCount = int(1)

for line in lineList:
    print("Line Number ", lineCount, ":", line.strip("\n"))
    lineCount +=1

poem.close()

"""
 The read function is the most basic.
 It chewes up the whole file into 1 string. So I need to work
 on it.
 Because I need to put in a line number, I need to get it in 
 a list type, and then use what i learned earlier to iterate and
 print the count.
 Used the split() function to give me a list of strings.
 then the printing is exactly the same as readlines.

"""
poem = open("./debanks.txt", "r")

bigLine = poem.read()
lineList = bigLine.split("\n")

lineCount = int(1)
for line in lineList:
    print("Line Number ", lineCount, ":", line.strip("\n"))
    lineCount +=1

poem.close()


