import csv

def spread_to_government_bond_curve(corporate, government):
    """Calculate spread to the government bond curve after calculating linear interpolation"""

    print("bond,spread_to_curve")
    for bond in corporate:
        term = float(bond[2])
        bond_yield = float(bond[3])
        lower_bond_index = find_the_closest_value_index_low(term, government)
        higher_bond_index = lower_bond_index + 1 
        lower_yield = float(government[lower_bond_index][3])
        higher_yield = float(government[higher_bond_index][3])
        lower_term = float(government[lower_bond_index][2])
        higher_term = float(government[higher_bond_index][2])
        linear_interpolation = lower_yield + (higher_yield - lower_yield)*(term - lower_term)/(higher_term - lower_term)
        spread_to_curve = round(bond_yield - linear_interpolation,2)

        print(bond[0] + "," +"{:.2f}".format(spread_to_curve) + "%")

def find_the_closest_value_index_low(term, government):
    """Finds the index of closest government bond to a given corporate bond in terms of years to maturity (term) that has term lower than the given term"""
    
    count = 0
    for bond in government:
        if float(bond[2]) < term:
            count += 1
        else: 
            break

    return count - 1

if __name__ == "__main__":

    corporate = [] #global list variable for storing corporate bonds
    government = [] #global list variable for storing government bonds

    with open('Book2.csv', newline='') as csvfile:
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

    government.sort(key=lambda government: float(government[2])) 
    #sorted the list on the basis of term to make it easier to check the government bonds with maturity term higher and lower than a given coporate bond
  
    spread_to_government_bond_curve(corporate, government)
