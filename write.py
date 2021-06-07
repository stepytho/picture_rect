from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, colors, Alignment,Border,Side

#判断某一列最最大行
def rect_row(old_wb,column):
    sheet = old_wb.active
    try:
        max_row_B = max((bb.row for bb in sheet[column] if bb.value))
        print("此时，%s列最大行为%d" %(column,max_row_B))
        return max_row_B
    except ValueError:
        print("此时，%s列最大行为空,从第1行开始写" %column)
        return 0
    

#向某一列写入列表里的数据
def write_in(old_wb, column, first_row, list1):
    sheet = old_wb.active
    border = Border(left=Side(border_style='thin',color='000000'),
                right=Side(border_style='thin',color='000000'),
                top=Side(border_style='thin',color='000000'),
                bottom=Side(border_style='thin',color='000000'))
    for i in range(len(list1)):
        if i == 0:
            sheet[column+str(i+first_row)] = list1[i]
            # 设置B1中的数据垂直居中和水平居中，除了center，还可以使用right、left等等参数
            sheet[column+str(i+first_row)].alignment = Alignment(horizontal='center', vertical='center')
            sheet[column+str(i+first_row)].border = border
        else:
            sheet[column+str(i+first_row)] = int(list1[i])
            # 设置B1中的数据垂直居中和水平居中，除了center，还可以使用right、left等等参数
            sheet[column+str(i+first_row)].alignment = Alignment(horizontal='center', vertical='center')
            sheet[column+str(i+first_row)].border = border

            
    print("--数据%s写入完成--" %list1[0])




if __name__ == "__main__":
    old_wb = load_workbook('预应力钢筋.xlsx')
    numbers = ["竖弯","32","23","23","7654"]
    #first_row = rect_row(old_wb, "A") + 2
    #write_in(old_wb, "A", first_row,numbers)
    rect_row(old_wb, "a")

    old_wb.save('预应力钢筋.xlsx')
