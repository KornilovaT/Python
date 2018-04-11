def sort_fruits():
    #Open input and output files. If they are not in the same directory as the source code then
    #we should add a path. For example, 'C:\...\unsorted_fruits.txt'
    infile = open('unsorted_fruits.txt', 'r')
    outfile = open('sorted_fruits.txt', 'w')
    # read the input file
    fruits = infile.readlines()
    #Sort the items in the list
    fruits.sort()
    for fruit in fruits:
        outfile.write(fruit)
    #Close the input and output files
    infile.close()
    outfile.close()


sort_fruits()
