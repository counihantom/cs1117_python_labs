dnaFile = open("./dna.txt", "r")
dnaString = dnaFile.read()

"""
 First use the DOUBLE newline to seperate the long string
 into patent records.
 I can see that double newline is the unique seperator between
 each patient record - i.e. not single line sepertor.

 Note, each patent record (patient in PatientStrings) will 
 be poluted with their own new lines which need removing later.
"""
patentStrings = dnaString.split("\n\n")

"""
 Found this replace function online that can now be used to clean
 up each individual patient's string removing the poluting
 newlines in each.
 
 Need a loop to print each patient.
 and in that loop clean up before I print them out.
"""

patientCount = int(0)
for patent in patentStrings:
    print("Count ", patientCount, ": ", patent.replace("\n",""))
    patientCount +=1

"""
 Close the file so my program is tidy
"""

dnaFile.close()
