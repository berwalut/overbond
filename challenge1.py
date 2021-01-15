import csv

def corporate_bond_spread(corporate, government):
    """Calculate the yield spread (return) between a corporate bond and its government bond benchmark."""

    print("bond,benchmark,spread_to_benchmark")
    for bond in corporate:
      
        closest_bond = government[find_the_closest_value_index(float(bond[2]), government)]
        spread = round(float(bond[3]) - float(closest_bond[3]),2)
        print(bond[0] + "," + closest_bond[0] + "," + "{:.2f}".format(spread) + "%")

def find_the_closest_value_index(term, government):
    """Finds the index of closest government bond to a given corporate bond in terms of years to maturity (term)."""

    absolute_difference = []
    for bond in government:
        absolute_difference.append(abs(term-float(bond[2])))
    return absolute_difference.index(min(absolute_difference))


if __name__ == "__main__":

    corporate = [] #global list variable for storing corporate bonds
    government = [] #global list variable for storing government bonds

    with open('Book1.csv', newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        line_count = 0
        
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t{row[0]} is a {row[1]} bond with a term of {row[2]} years and yield is {row[3]}.')
                line_count += 1
            if row[1] == "corporate":
                corporate.append(row)
            elif row[1] == "government":
                government.append(row)
    print(f'Processed {line_count} lines.')
    print() 
 
    corporate_bond_spread(corporate, government)
