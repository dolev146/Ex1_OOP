import pandas as pd
# reading csv file:
if __name__ == '__main__':
    a = pd.read_csv('Calls_a.csv', header=None)
    print(a)
    for i in a.loc[:, 1]:
        print(i)
    # 19.590869649656987

'''
c = pd.read_csv('Calls_a.csv' , header=None)
    print(c)
    #print(c.loc[:,1])
    for i in c.loc[:,1]:
        print(i)
'''

