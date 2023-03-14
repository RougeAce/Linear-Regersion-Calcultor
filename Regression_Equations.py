def linear_regression_equation(x, y, round_constant = 5):
    if (len(x) != len(y)):
        return False
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

    return(total)





















