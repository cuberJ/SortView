import random
from tkinter import *
WIDTH, POSITION = 5, 2000
CWIDTH = 1500
CHEIGHT = 700
import time

Size = 70
Data_main = random.sample(range(0, Size), Size)  # 生成随机数据集，使用各种算法将其从小到大排序

def BubbleSort(tk, canvas):
    data = Data_main.copy()
    for i in range(0, len(data)):
        for j in range(0, len(data) - i - 1):
            if data[j] >= data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                canvas.delete("all")
                Draw(j, j+1, data, tk, canvas)
    print(data)

def DoubleBubbleSort(tk, canvas):
    data = Data_main.copy()
    left, right = 0, len(data)
    j = left
    while left < right:
        while j < right-1:
            if data[j] >= data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                canvas.delete("all")
                Draw(j, j + 1, data, tk, canvas)
            j += 1
        right -= 1
        while j > left:
            if data[j-1] >= data[j]:
                data[j], data[j-1] = data[j-1], data[j]
                canvas.delete("all")
                Draw(j, j - 1, data, tk, canvas)
            j -= 1
        left += 1
    print(data)

def ChooseSort(tk, canvas):
    data = Data_main.copy()
    for i in range(0, len(data)):
        min_num = i
        for j in range(i+1, len(data)):
            if data[min_num] >= data[j]:
                min_num = j
            canvas.delete("all")
            Draw(min_num, j, data, tk, canvas)
        data[min_num], data[i] = data[i], data[min_num]
    print(data)

def InsertSort(tk, canvas):
    data = Data_main.copy()
    for i in range(1, len(data)):
        for j in range(i, 0, -1):
            if data[j] < data[j-1]:
                data[j], data[j-1] = data[j-1], data[j]
                canvas.delete("all")
                Draw(j, j - 1, data, tk, canvas)
    print(data)

def QuickSort(left, right, data, tk, canvas, nums):
    low = left
    high = right
    if low > high:
        return
    temp = data[left]
    while low < high:
        while data[high] > temp and low < high:
            high -= 1
        data[low] = data[high]
        canvas.delete('all')
        Draw(low, high, data, tk, canvas)
        while data[low] < temp and low < high:
            low += 1
        data[high] = data[low]
        canvas.delete('all')
        Draw(low, high, data, tk, canvas)
    data[low] = temp
    QuickSort(left, low-1, data, tk, canvas, nums+1)
    QuickSort(low+1, right, data, tk, canvas, nums+1)

def ShellSort(tk, canvas):
    data = random.sample(range(0, 300), 300)
    d = int(len(data)/2)
    while d >= 1:
        for i in range(d, len(data)):
            temp = data[i]
            j = i
            while j >= d:
                if data[j-d] > temp:
                    data[j] = data[j-d]
                    Draw(j, i, data, tk, canvas)
                    canvas.delete("all")
                else:
                    break
                j -= d
            data[j] = temp
        d = int(d/2)
    print(data)

def MergeSort(low, high, data, tk, canvas):
    if low < high:
        mid = int((low + high) / 2)
        MergeSort(low, mid, data, tk, canvas)
        MergeSort(mid+1, high, data, tk, canvas)
        Merge(low, high, int((low + high)/2), data, tk, canvas)

def Merge(low, high, mid, data, tk, canvas):
    B = []
    i, j = low, mid + 1
    while i <= mid and j <= high:
        if data[i] < data[j]:
            B.append(data[i])
            i += 1
        else:
            B.append(data[j])
            j += 1
    while i <= mid:
        B.append(data[i])
        i += 1
    while j <= high:
        B.append(data[j])
        j += 1
    for i in range(len(B)):
        data[low + i] = B[i]
        canvas.delete("all")
        Draw(low+1, mid, data, tk, canvas)

def HeapSort(data, tk, canvas):
    HeapBuild(data, tk, canvas)
    for i in range(len(data)-1, 0, -1):
        data[i], data[1] = data[1], data[i]
        canvas.delete('all')
        Draw(i, 1, data, tk, canvas)
        HeapAdjust(1, data, i, tk, canvas)

def HeapBuild(data, tk, canvas): # 构建小根堆
    for i in range(int(len(data)/2), 0, -1):
        HeapAdjust(i, data, len(data), tk, canvas)

def HeapAdjust(pos, data, lens, tk, canvas):
    temp = data[pos]
    i = pos*2
    while i < lens:
        if i+1 < lens and data[i] > data[i+1]:
            i += 1
        if temp <= data[i]:
            break
        else:
            data[pos] = data[i]
            pos = i
        canvas.delete('all')
        Draw(pos, i, data, tk, canvas)
        i *= 2
    data[pos] = temp

def radix_sort(s, tk, canvas):
    """基数排序"""
    i = 0  # 记录当前正在排拿一位，最低位为1
    max_num = max(s)  # 最大值
    j = len(str(max_num))  # 记录最大值的位数
    while i < j:
        bucket_list =[[] for _ in range(10)]  # 初始化桶数组
        for x in s:
            bucket_list[int(x / (10**i)) % 10].append(x)  # 找到位置放入桶数组

        s.clear()
        for x in bucket_list:   # 放回原序列
            for y in x:
                s.append(y)
                canvas.delete('all')
                Draw(0, y, s, tk, canvas)
        i += 1

def Draw(pos1, pos2, data, tk, canvas):  # pos1,pos2表示需要交换的两个数据的位置
    lens = len(data)
    for i in range(lens):
        if i != pos1 and i != pos2:
            canvas.create_rectangle(i * int(CWIDTH/lens), POSITION, (i + 1) * int(CWIDTH/lens), data[i]*int(CHEIGHT/lens), fill='blue')
        else:
            canvas.create_rectangle(i * int(CWIDTH/lens), POSITION, (i + 1) * int(CWIDTH/lens), data[i]*int(CHEIGHT/lens), fill='yellow')

    tk.update()

tk = Tk()
canvas = Canvas(tk, width=CWIDTH, height=CHEIGHT)
canvas.pack()
# Draw(0, 1, Data_main, tk, canvas)

BubbleSort(tk, canvas)
DoubleBubbleSort(tk, canvas)
ChooseSort(tk, canvas)
InsertSort(tk, canvas)

data = random.sample(range(0, 300), 300)
QuickSort(0, len(data)-1, data, tk, canvas, 0)
print(data)

ShellSort(tk, canvas)

data = random.sample(range(0, 300), 300)
MergeSort(0, len(data)-1, data, tk, canvas)
print(data)


data = random.sample(range(0, 300), 300)
data.insert(0, 0)
HeapSort(data, tk, canvas)
print(data)

data = random.sample(range(0, 300), 300)
radix_sort(data, tk, canvas)
print(data)
