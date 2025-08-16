from tabulate import tabulate
import sys
import csv

def main():
    
    try:
        #if len(sys.argv) < 2:
        #    sys.exit("Too few command-line arguments")
        #if len(sys.argv) >= 4:
        #    sys.exit("Too many command-line arguments")

        data = []
        with open(sys.argv[1]) as readcsv_file:
            for line in readcsv_file:
                if "name" in line:
                    continue
                else:
                    data.append(line.rstrip().split(","))
        
        with open(sys.argv[2], "w") as sys.argv[2]:
            csv_writer = csv.writer(sys.argv[2])
            csv_writer.writerow(['first', 'last', 'house'])
            for student in data:
                studentInfo = [student[1].strip('"').strip(" "),student[0].strip('"').strip(" "), student[2]]
                csv_writer.writerow(studentInfo)


    except FileNotFoundError:
        sys.exit(f"could not read {sys.argv[1]}")



if __name__ == "__main__":
    main()
