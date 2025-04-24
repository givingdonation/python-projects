def letterCombinations(digits):
    dict = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}

    output = []
    if len(digits) == 0:
        return ""
    for i in dict[int(digits[0])]:
        output.append(i)
    digits = digits[1:]
    print(digits)
    print(output)
    while (len(digits) > 1):
        newout = []
        for i in output:
            newout.append([i + x for x in dict[int(digits[0])]])
        output = []
        for i in newout:
            output.append(i) 
        digits = digits[1:]

    return output
print(letterCombinations("2"))
