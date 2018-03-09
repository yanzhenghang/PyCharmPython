
import random
import time
import xlwt as ExcelWrite

'''def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)'''

def gcd_ext(a, b):
    #a is bigger than b
    if a < b:
        tmp = a
        a = b
        b = tmp
    a_const = a
    eTable = []
    while b != 0:
        #  a = b * e + r
        e = a // b
        r = a % b
        eTable.append(e)
        a = b
        b = r
    eTable.pop()
    length = len(eTable)
    length_const = length
    if length < 1:
        print("gcd data error!")
        return

    bi_2 = 1
    bi_1 = eTable.pop(-1)
    bi = -1
    length = length - 1
    while length > 0:
        bi = eTable.pop(-1) * bi_1 + bi_2
        bi_2 = bi_1
        bi_1 = bi
        length = length - 1
    if length_const % 2 == 0:
        return bi
    else:
        return a_const - bi

def xlswrite(value_table):
    xls = ExcelWrite.Workbook(encoding='utf-8')
    # 指定file以utf-8的格式打开
    sheet = xls.add_sheet('aaa')
    # 指定打开的文件名
    sheet.write(0, 0, value_table)
    xls.save('aaa.xls')
    '''data = { \
        "1": ["张三", 150, 120, 100], \
        "2": ["wang", 90, 99, 95], \
        "3": ["wu", 60, 66, 68] \
        }
    # 字典数据

    ldata = []
    num = [a for a in data]
    # for循环指定取出key值存入num中
    num.sort()
    # 字典数据取出后无需，需要先排序

    for x in num:
        # for循环将data字典中的键和值分批的保存在ldata中
        t = [int(x)]
        for a in data[x]:
            t.append(a)
        ldata.append(t)

    for i, p in enumerate(ldata):
        # 将数据写入文件,i是enumerate()函数返回的序号数
        for j, q in enumerate(p):
            print(i, j, q)

            table.write(i, j, q)
    file.save('aaa')'''


def main():
    numofCCEs = 63   #numofCCEs>16

    aggrLevel =8
    valueTable = 39827, 63455, 50028, 9282, 45534, 8291, 30251, 39906, 64012, 16624
    subframe = 0 #subframe取值从0到9
    Ak_p = valueTable[subframe]
    D = 65537
    Y_1p = gcd_ext(D, Ak_p)

    for subframe_tmp in range(0,10):
        print('subframe = ',subframe_tmp,':  ',gcd_ext(D, valueTable[subframe_tmp]))

    Ak_p_table = 61772, 19233, 6140, 17461, 58483, 15825, 57545, 8397, 39666, 16333

    pdcchsPerAggr = numofCCEs // aggrLevel
    startLoc = 5
    #random.randint(0, pdcchsPerAggr - 1)

    xls = ExcelWrite.Workbook(encoding='utf-8')
    sheet = xls.add_sheet('aaa')
    for tmp in range(0, D-1):
        Yk = startLoc + tmp * pdcchsPerAggr
        Y_1 = (Y_1p * Yk) % D

        tmp1 = (Y_1p * startLoc) % D
        tmp2 = (Y_1p * pdcchsPerAggr) % D
        tmp3 = tmp % D
        Y_1_ = (tmp1 + (tmp3 * tmp2) % D) % D
        #Y_1 即RNTI
        print('tmp1=',tmp1,'  tmp2=',tmp2,'  tmp3=',tmp3)

        startLoc_checked = ((Y_1 * Ak_p) % D) % pdcchsPerAggr
        print('startLoc_checked=',startLoc_checked)

        print(Y_1)
        print(Y_1_)

        #if startLoc_checked != startLoc:
         #   break
        sheet.write(tmp, 0, Y_1)
        sheet.write(tmp, 1, startLoc_checked)

    xls.save('aaa.xls')







main()

