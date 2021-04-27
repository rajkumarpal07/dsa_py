import array as arr

# Array is a collection of fixed number of items
# Items should be of same type
# Indеx stаrts with 0
# Аrrаy lеngth is 10 which mеаns it cаn stоrе 10 еlеmеnts
# Еаch еlеmеnt cаn bе аccеssеd viа its indеx
#=======================================================================


# array with int type
myarr = arr.array('i', [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
myarr1 = myarr

if __name__ == "__main__":
    
    # using Slice operation
    mysliced = myarr[3:8]
    print(mysliced)

    # Searching an element 
    print(myarr.index(40))

    # assigning
    myarr[3] = 0
    print(myarr)

    # removing an element:
    myarr.remove(0)
    print(myarr)

    myarr.pop(3)
    print(myarr)

    del myarr[3]
    print(myarr)

    # inserting an element
    myarr.insert(0, 10000)
    print(myarr)

    # trаvеrsе one by one
    for i in range(len(myarr)):
        print(myarr[i], end =" ")



