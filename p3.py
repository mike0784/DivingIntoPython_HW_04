def printAccount(i):
    print("Ваш баланс: " + str(i))

def verificationAdd(i):
    if i % cratnost == 0:
        return True
    else:
        return False

def nalog():
    global summa
    if summa > limit:
        summa -= summa * wealthTax

def percentageForWithdrawal(i):
    temp = i * 0.015
    if temp < minPop:
        return minPop
    elif temp > maxPop:
        return maxPop
    else:
        return temp
    
def Procent():
    global summa, count
    count += 1
    if count == countSize:
        summa += summa * procent
        count = 0

def addOperation(a, b):
    global operation
    size = len(operation)
    operation[size] = [a, b]

def printOperation():
    global operation
    if len(operation) == 0:
        print("Вы ещё не произвели ни одной операции")
    else:
        for item in operation.values():
            print("Операция: {0:12}  Сумма: {1}".format(item[0], item[1]))

def printMenu(a):
    for k, v in a.items():
        print("{0} - {1}".format(k, v))

def addCash():
    global summa
    while True:
            add = int(input("На какую сумму вы хотите пополнить: "))
            nalog()
            if verificationAdd(add):
                summa += add
                Procent()
                printAccount(summa)
                addOperation("Пополнение", add)                
                break
            else:
                print("Вводимая вами сумма должна быть кратна {!s}\nПопробуйте ещё раз".format(cratnost))

def delCash():
    global summa
    while True:
            pop = int(input("Какую сумму вы хотите снять: "))
            nalog()
            if pop +  percentageForWithdrawal(pop) > summa:
                print("Запрашиваемая вами сумма превышает сумму на счете\nПопробуйте ещё раз")
            else:
                summa -= pop +  percentageForWithdrawal(pop)
                Procent()
                printAccount(summa)
                addOperation("Снятие", pop)
                break


summa = 0
minPop = 30
maxPop = 600
cratnost = 50
procent = 0.03
count = 0
countSize = 3
limit = 5000000
wealthTax = 0.1
operation = {}
menu = {1: "Внести деньги", 2: "Снять деньги", 3: "Просмотр опреций", 4: "Выход"}
while True:
    printMenu(menu)
    action = int(input("Выберите операцию: "))
    if action == 1:
        addCash()
    elif action == 2:
        delCash()
    elif action == 3:
        printOperation()
    elif action == 4:
        nalog()
        printAccount(summa)
        break

print("Досвидание")