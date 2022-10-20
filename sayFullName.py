import random

def power(power):
    firstTen = ['', 'Thousand', 'Million', 'Billion', 'Trillion', 'Quadrillion', 'Quintillion', 'Sextillion', 'Septillion', 'Octillion', 'Nonillion']
    ones = ['','Un','Duo','Tre','Quattuor','Quinqua','Se','Septe','Octo','Nove']
    tens = ['', 'Deci', 'Viginti', 'Triginta', 'Quadraginta', 'Quinquaginta', 'Sexaginta', 'Septuaginta', 'Octoginta', 'Nonaginta']
    hundreds = ['','Centi','Ducenti','Trecenti','Quadringenti','Quingenti','Sescenti','Septingenti','Octingenti','Nongenti']
    if power < 11:
        return firstTen[power]
    if power < 100:
        base = tens[int(power//10)][:-1] + 'illion' 
        if power%10 == 1:
           return base 
        else:
            return ones[(power - 1)%10] + base.lower()
    if power < 1000:
        base = hundreds[int(power//100)][:-1] + 'illion' 
        if power%100 == 1:
            return base
        base = tens[int((power//100)//10)] + base.lower()
        if power%10 == 1:
            return base
        last = ones[(power - 1)%10]
        if base.lower()[0] in 'aeiou' and last[-1] in 'aeiou':
            return ones[(power - 1)%10][:-1] + base.lower()
        return ones[(power - 1)%10] + base.lower()
    return ''

def sayRhs(rhs):
    toReturn = ''
    ones = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
    digitList = [char for char in rhs]
    digitList.reverse()
    for digit in digitList:
        toReturn = ones[eval(digit)] + ' ' + toReturn
    return toReturn[:-1]

def sayGroup(group):
    toReturn = ''
    ones = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
    tens = ['','Ten','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
    teens = ['Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
    digits = str(group)
    while len(digits) < 3:
        digits = '0' + digits
    if digits[0] != '0':
        if digits[1] == '0' and digits[2] == '0':
            toReturn += ones[int(digits[0])] + ' Hundred'
        else:
            toReturn += ones[int(digits[0])] + ' Hundred '
    if digits[1] != '1':
        if digits[1] != '0':
            toReturn += tens[int(digits[1])] 
            if digits[2] != '0':
                toReturn += ' ' + ones[int(digits[2])]
        else:
            if digits[2] != '0':
                toReturn += ones[int(digits[2])]
    else:
        toReturn += teens[int(digits[2])]
    return toReturn

def commaNumber(num):
    'This function takes a numeric type (int/float) and returns a striing representation with commas seperating groups of three digits starting with the ones, tens, and hundreds place in the first (right-most) group'
    fullNumberStr = str(num)
    strList = []
    numList = fullNumberStr.split('.')
    intStr = numList[0]
    while len(intStr) > 0:
        strList.append(intStr[-3:]) # Builds a list with groups of three digits on the lhs of the .
        intStr = intStr[:-3]
    fStr = ''
    for i in range(len(strList)):
        fStr += strList.pop()
        if len(strList) > 0:
            fStr += ','
    for elem in numList[1:]:
        fStr += '.' + elem # Adds the rhs of the . to the string
    return fStr

def sayFullName(num):
    'Does say name with words for groups of three digits'
    if not num:
        return 'Zero'
    name = ''
    cStr = commaNumber(num)
    cLst = cStr.split(',')
    i = 0
    while len(cLst) and i < 1000:
        if '.' not in cLst[-1] and i != 0:
            group = int(cLst.pop())
            if group:
                name = sayGroup(group) + ' ' + power(i) + ' ' + name
        else:
            if '.' not in cLst[-1]:
                name = sayGroup(cLst.pop()) + name
            else:
                group = cLst.pop()
                lhs = eval(group.split('.')[0])
                rhs = group.split('.')[1]
                name = sayGroup(lhs) + ' Point ' + sayRhs(rhs) + name
        i += 1
    if cLst:
        name = cLst.pop() + ' ' + name
    while cLst:
        name = cLst.pop() + ',' + name
    return name

# print(sayFullName(2**60))
