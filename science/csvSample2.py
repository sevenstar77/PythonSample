import csv, codecs



#csv reader
file_name = 'test1.csv'
csvData = codecs.open(file_name, "r", "euc-kr")

reader = csv.reader(csvData, delimiter=",", quotechar='"')

for cell in reader:
   print(cell[0] + "  |  "+ cell[1] + "  |  "+ cell[2] + "  |  "+ cell[3])


#csv writer
file_nameV1 = 'writerCsv.csv'

with codecs.open(file_nameV1, "w", "utf-8") as wr:
       writer = csv.writer(wr, delimiter=",", quotechar='"')
       writer.writerow(["NO", "NAME", "menufacturer"])
       writer.writerow(["1", "Tv", "samsung"])
       writer.writerow(["2", "mobile", "apple"])
       writer.writerow(["3", "aircorn", "LG"])
       writer.writerow(["4", "camera", "nikon"])
