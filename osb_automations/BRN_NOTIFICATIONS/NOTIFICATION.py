
infile=open("FINAL_ERROR",'rt')
lines=infile.readlines()
print(lines)
for line in lines:
    print("============")
    row=line.split(",")
    error=row[0]

    count=row[1]

    #print("<tr>")
    print("Error :{}".format(error))
    print("Count :{}".format(count))
    #print("<td>{}</td>".format(error))
    #print("<td>{}</td>".format(count))
infile.close()





