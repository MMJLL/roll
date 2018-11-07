"""
版本：1.0
作者：MJL
功能：掷骰子
"""

import random
import matplotlib.pyplot as plt


roll1_list = []
roll_count = [0,0,0,0,0,0]
roll_rate = []

def main():
    roll_times = 10000
    for i in range(1,roll_times + 1):
        roll1 = random.randint(1,6)
        roll_count[roll1 -1] +=1
        roll1_list.append(roll1)
    for j in range(1,7):
        roll_rate.append(roll_count[j - 1]/roll_times)

    print(roll1_list,'\n',len(roll1_list),'\n',roll_count,'\n',roll_rate)

    plt.hist(roll1_list,[1,2,3,4,5,6,7],rwidth=0.4,color='blue')
    plt.show()

if __name__ == '__main__':
    main()
