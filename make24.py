# for puzzle10
# start = 0
# finish = 9+1
# target_num = 10

# for trump card
start = 1
finish = 13 + 1
target_num = 24

ops = {"+": lambda a,b: b + a,
       "-": lambda a,b: b - a,
       "*": lambda a,b: b * a,
       "/": lambda a,b: b / a,
}

def poland(array):
    stack = []
    try:
        for s in array:
            # print s
            if s in ops:
                stack.append(ops[s](stack.pop(), stack.pop()))
            else:
                stack.append(float(s))
        return stack[-1]
    except:
        return -1

def make_24(i,j,k,l):
    operator = ["+","-","*","/"]
    for a in operator:
        for b in operator:
            for c in operator:
                array = [[i, j, a, k, b, l, c],
                         [i, j, a, k, l, b, c],
                         [i, j, k, a, b, l, c],
                         [i, j, k, a, l, b, c],
                         [i, j, k, l, a, b, c]
                        ]
                for z in range(5):
                    answer = poland(array[z])
                    # print str(array[z]) + " "+ str(answer)
                    if answer == target_num:
                        return array[z]
    # print "not found!"

def test(array1):
    for x in range(4):
        array2 = array1[:]
        array2.pop(x)
        for y in range(3):
            array3 = array2[:]
            array3.pop(y)
            for z in range(2):
                array4 = array3[:]
                array4.pop(z)
                # print array1[x], array2[y], array3[z], array4[0]
                possible = make_24(array1[x], array2[y], array3[z], array4[0])
                if possible != None:
                    return possible




def main():
    count_possible = 0
    count_impossible = 0
    for i in range(start,finish):
        for j in range(i,finish):
            for k in range(j,finish):
                for l in range(k,finish):
                    # print "*"*10
                    # print i,j,k,l
                    example = test([i,j,k,l])
                    if  example == None:
                        count_impossible +=1
                        print i,j,k,l
                        # print "not found"
                    else:
                        count_possible +=1
                        # print "found like " + str(example)

    # print test([6, 8, 8, 9])
    # print make_24(8, 6, 9, 8)
    # print test([8, 8, 8, 9])
    # print make_24([0, 0, 0, 0])

    print "possible: " + str(count_possible)
    print "impossible: " + str(count_impossible)


if __name__ == "__main__":
    # execute only if run as a script
    main()
