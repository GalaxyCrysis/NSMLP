import math
import sort
import numbers
import pandas as pd

#calculates the sum and returns it
def sum(x):
    result = 0
    for var in x:
        result = result + var

    return result

#calculates the mean and returns it
def mean(x):
    result = sum(x)/len(x)
    return result


# sorts the array,list or dict and returns the median
def median(x):
    #sort the array
    x = sort.combSort(x)

    #tests if the length of the array is even or odd
    if (len(x) % 2) == 1:
        result = x[int(len(x)/2)]
    else:
        Xo = x[int(len(x)/2)]
        Xu = x[int((len(x)/2) -1)]
        result = 0.5 * (Xu + Xo)

    return result

#returns the minimum of the dataset
def min(x):
    minimum = x[0]
    for var in x:
        if var < minimum:
            minimum = var
    return minimum



# returns the minimum of the dataset
def max(x):
    maximum = x[0]
    for var in x:
        if var > maximum:
            maximum = var

    return maximum

#calculates the variance of the dataset and returns it
def var(x,cor=False):
    #get mean of the dataset
    avg = mean(x)
    var_temp = 0
    for var in x:
        var_temp = var_temp + ((var - avg) ** 2)
    if cor:
        #variance with n
        return var_temp / (len(x) - 1)
    else:
        #variance with n-1
        return var_temp / len(x)



#calculates the standard deviation and returns it
def std(x,cor=False):
    #get variance
    if cor:
        #variance with n
        variance = var(x, cor=True)
    else:
        #variance with n-1
        variance = var(x,cor=False)
    return math.sqrt(variance)


#calculates the range of the dataset and returns it
def range(x):
    result = max(x) - min(x)
    return result


# calculates the quartile and returns it
def quar(x,p):
    #sort the dataset
    x = sort.combSort(x)
    q = p*len(x)
    if ".0" in str(q):
        q = int(q)
    if isinstance(q, numbers.Integral) == False:
        quar = x[math.ceil(q)-1]
    else:
        quar = 0.5 * (x[q]+x[q-1])


    return quar

#calculates the interquartile range and returns it
def iqr(x):
    return quar(x,p=0.75) - quar(x,p=0.25)

#summary method: Returns the main statistics of the dataset
def summary(x):
    df = pd.DataFrame(columns=("Min.", "1st Qu.", "Median", "Mean", "3rd Qu.", "Max."))
    if "DataFrame" in str(type(x)):
        for column in list(x.columns.values):
            df.loc[column] = (min(x[column]), quar(x[column], p=0.25),
                                   median(x[column]), round(mean(x[column]),3), quar(x[column], p=0.75), max(x[column]))
        return df

    else:
        result = "Min.  1st Qu.  Median  Mean  3rd Qu.  Max. \n"+ str(min(x)) + "     " + str(quar(x,p=0.25)) +\
                 "        " + str(median(x)) + "      " + str(round(mean(x),3)) + "    " + str(quar(x, p=0.75)) + "      " + str(max(x))
        return result

#calculates the covariance and returns it
def cov(x,y):
    if len(x) != len(y):
        raise Exception("X and Y must have same dimension")
    #calculate the mean
    x_avg = mean(x)
    y_avg = mean(y)
    result = 0
    i = 0
    while i < len(x):
        result = result + ((x[i]-x_avg) * (y[i] - y_avg))
        i = i+1
    result = 1/(len(x)-1) * result
    return round(result,3)

#calculates the correlation coefficient and returns it
def corr(x,y):
    if len(x) != len(y):
        raise Exception("X and Y must have same dimension")
    # calculate the mean
    x_avg = mean(x)
    y_avg = mean(y)
    result = 0
    x_result = 0
    y_result = 0
    i = 0
    while i < len(x):
        result = result + ((x[i] - x_avg) * (y[i] - y_avg))
        x_result = x_result + (x[i]-x_avg)**2
        y_result = y_result + (y[i]-y_avg)**2
        i = i + 1
    #sqrt the results for x and y
    x_result = math.sqrt(x_result)
    y_result = math.sqrt(y_result)
    #now calculate the correlation
    r = result/(x_result*y_result)
    return round(r,5)

#calculates the probability density and returns it
#std = standard deviation = σ, mean = mean of distributions = μ
def dnorm(x, mean=0,std = 1, log = False):
    if "list" in str(type(x)) or "set" in str(type(x)):
        prob_list = list()
        i = 0
        while i < len(x):
            if "list" in str(type(mean)) or "set" in str(type(mean)):
                mean = mean[i]
            if "list" in str(type(std)) or "set" in str(type(std)):
                std = std[i]
            prob = (1/math.sqrt(2*math.pi*std)) * math.exp(-((x[i]**2 -2*x[i]*mean + mean**2)/(2*(std**2))))
            if log:
                prob = math.log(prob)
            prob_list.append(prob)
            i = i + 1
        return prob_list

    else:
        prob = (1/math.sqrt(2*math.pi*std)) * math.exp(-((x**2 -2*x*mean + mean**2)/(2*(std**2))))
        if log:
            return math.log(prob)
        else:
            return prob

















