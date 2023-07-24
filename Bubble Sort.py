def bsort(lst1):

    m = len(lst1)

    for x in range(m-1):

        for i in range(0,m-1-x):

            if lst1[i] > lst1[i + 1]:
                lst1[i],lst1[i+1] = lst1[i+1],lst1[i]

    print(lst1)

lst1 = input("To be sorted: ").split(',')
lst1 = [int(x) for x in lst1]

bsort(lst1)