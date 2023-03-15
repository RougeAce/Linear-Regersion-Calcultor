def linear_regression_equation(x, y, Check = None, round_constant = 5):
    if (len(x) != len(y)):
        return 3
    a1 = []
    a2 = []
    n = len(x)


    # Finds needed varibles
    sumX = round(sum(x), round_constant)
    sumY = round(sum(y), round_constant)
    for i in range(n):
        a1.append(round(x[i]*y[i], round_constant))
        a2.append(round(x[i]*x[i], round_constant))



    a1 = sum(a1)
    a2 = sum(a2)


    # Find Top of Equation
    top = (n*a1)-(sumX*sumY)
    top = round(top, round_constant)
    # Find Bottom of Equation
    bottom = (n*a2)-(sumX ** 2)
    bottom = round(bottom, round_constant)


    m = round(top/bottom, 2)


    mx = m * x[1]
    b = (sumY - ((m) * sum(x)))/n

    b = round(b, 2)

    total = f"y = {m}x + {b}"

    if (Check == "MSE"):
        MSSE = MSE(x, y, m, b)

        print(MSSE)
        return(total)
    elif (Check == "r^2"):

        print(RSqaured(x, y, m, b))
        return(total )
        RSqaured(x, y, m, b)
    elif (Check == None):
        return(total)

def Predicted_Terms(x, m, b):
    Predictions = []
    for i in x:
        Predictions.append((m * i) + b)
    return Predictions

def MSE(x, y, m, b):
    N = len(x)
    Predticed = Predicted_Terms(x, m, b)
    sum = 0
    C = 1 / N

    for i in range(len(x)):
        O = y[i] - Predticed[i]
        O = O ** 2
        sum += O

    return(C * sum)


def RSqaured(x, y, m, b):
    # Find the components for the top MSE
    MT = sum(y)/len(y)
    Predticed = Predicted_Terms(x, MT, 0)
    top = TSS(y, Predticed)
    bottom = TSS(y, Predicted_Terms(x, m, b))
    RR = top/bottom
    RSQUARED = 1 - RR

    return (RSQUARED)

def TSS(y, Y):
    total = 0
    for x in range(len(y)):
        a = (Y[x] - y[x])
        a = a ** a
        total += a

    return(total)





x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 5, 6]

print(linear_regression_equation(x, y, "r^2"))





















