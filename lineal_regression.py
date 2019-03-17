"""
    Lineal regression
    Try to find price from mileage
    (ADALINE batch)

    (Yeap i dont write comments)
    (Algo is pretty simple)
"""


import numpy as np
import pandas as pd

"""
    Yeap its only algo
    withot few exception
"""
class Linear_reg(object):
    def __init__(self,
                 learning_rate=0.01,
                 epoch=300):
        self.learning_rate = learning_rate
        self.weight = np.zeros(2)
        self.epoch = epoch

    def stantartization(self,
                        data):
        data.iloc[:, 0] = np.round((data.iloc[:, 0] - self.mean) / self.std, decimals=4)
        data.iloc[:, 1] = np.round((data.iloc[:, 1] - self.mean1) / self.std1, decimals=4)

    def prediction(self):
        mileage = input("Enter the number: ")
        try:
            mileage = int(mileage)
        except:
            print("Error!")
            self.prediction()
        mileage = (mileage - self.mean) / self.std
        cost = self.make_sum(mileage) * self.std1 + self.mean1
        print("car cost approximately - {}".format(int(cost)))
        ask = input("Again?(y/n): ")
        if ask == 'y':
            self.prediction()
        else:
            exit(0)

    def make_sum(self,
                 mileage):
        res = self.weight[0] + (self.weight[1] * mileage)
        return res

     # Can be while, but i dont want to do it :)
    def asking(self):
        ask = input("Save weight?(y/n):")
        if ask == 'y':
            np.savetxt("theta.csv", self.weight, delimiter=',')
        elif ask != 'n':
            self.asking()
        ask = input("Predict?(y/n): ")
        if ask == 'y':
            self.prediction()
        else:
            exit(0)

    def train(self,
              data):
        # Save mean and std for BD. Becuse when we will predict
        # we will needed use it to destandartization our data
        self.mean1 = np.mean(data.iloc[:, 1])
        self.std1 = np.std(data.iloc[:, 1])

        self.mean = np.mean(data.iloc[:, 0])
        self.std = np.std(data.iloc[:, 0])

        # Use standartization for our data
        # becuse its really big
        self.stantartization(data)
        for _ in range(self.epoch):
            error_sum = 0
            update = 0
            for i, val in data.iterrows():
                error = self.make_sum(val[0]) - val[1]
                error_sum += error
                update += error * val[0]
            self.weight[0] -= (self.learning_rate * error_sum) / data.shape[0]
            self.weight[1] -= (self.learning_rate * update) / data.shape[0]
        print("Model succeful train. Can predict")
        self.asking()


if __name__ == '__main__':
    df = pd.read_csv("data.csv")
    df_test = pd.read_csv("data.csv")
    l = Linear_reg()
    l.train(df)
