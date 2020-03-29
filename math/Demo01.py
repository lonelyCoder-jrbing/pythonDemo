import matplotlib.pyplot as plt
import random


# 线段中两点的坐标如示例中
# x=[[1,1],...] y=[[3.5,0],...]
# 即标了点(1,3,5)与点(1,0)，之后使用plot()函数连接两点


class graph:
    def __init__(self):
        self.xlen = 100
        self.ylen = 100
        self.x11 = random.randint(0, self.xlen)
        self.x12 = random.randint(0, self.xlen)

        self.x21 = random.randint(0, self.xlen)
        self.x22 = random.randint(0, self.xlen)

        self.x31 = random.randint(0, self.xlen)
        self.x32 = random.randint(0, self.xlen)

        self.x41 = random.randint(0, self.xlen)
        self.x42 = random.randint(0, self.xlen)

        self.y11 = random.randint(0, self.xlen)
        self.y12 = random.randint(0, self.xlen)

        self.y21 = random.randint(0, self.xlen)
        self.y22 = random.randint(0, self.xlen)

        self.y31 = random.randint(0, self.xlen)
        self.y32 = random.randint(0, self.xlen)

        self.y41 = random.randint(0, self.xlen)
        self.y42 = random.randint(0, self.xlen)
        self.x = [[self.x11, self.x12], [self.x21, self.x22], [self.x31, self.x32], [self.x41, self.x42]]
        self.y = [[self.y11, self.y12], [self.y21, self.y22], [self.y31, self.y32], [self.y41, self.y42]]

    def draw(self, x, y):
        for i in range(len(x)):
            plt.scatter(x[i], y[i], color='black', s=5)
            # plt.annotate("y="+str(y[i][0]), xy=(x[i][0], y[i][0]), xytext=(+15, -15), textcoords='offset points', fontsize=10,arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2'))
            # plt.annotate("y="+str(y[i][1]), xy=(x[i][1], y[i][1]), xytext=(+15, -15), textcoords='offset points', fontsize=10,arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2'))
            plt.plot(x[i], y[i], label='sin')
            plt.xlim(0, self.xlen)
            plt.ylim(0, self.ylen)
        plt.show()

    def cross(self, p1, p2, p3):  # 叉积判定
        x1 = p2[0] - p1[0]
        y1 = p2[1] - p1[1]
        x2 = p3[0] - p1[0]
        y2 = p3[1] - p1[1]
        return x1 * y2 - x2 * y1


if __name__ == '__main__':
    graph = graph()
    # graph.__init__()
    graph.draw(graph.x, graph.y)
