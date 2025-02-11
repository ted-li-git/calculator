import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("多功能计算器")
        self.master.geometry("450x500")  # 调整窗口大小为450x500

        self.equation = tk.StringVar()  # 用于显示计算表达式的字符串变量
        self.equation.set("0")  # 初始化显示为0

        self.display = tk.Entry(self.master, textvariable=self.equation, font=("Arial", 24), bd=10, insertwidth=4,
                                width=14, borderwidth=4, justify="right")
        self.display.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        # 创建按钮
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            "(", ")", "C", "CE", "/",
            "7", "8", "9", "+", "-",
            "4", "5", "6", "*", "1/x",
            "1", "2", "3", "%", "sqrt",
            "+/-", "0", ".", "="
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            command = lambda x=button: self.handle_click(x)
            tk.Button(self.master, text=button, command=command, font=("Arial", 18),
                      width=5, height=2).grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 4:
                col_val = 0
                row_val += 1

    def handle_click(self, button):
        current_equation = self.equation.get()

        if button == "C":  # 清除全部
            self.equation.set("0")
        elif button == "CE":  # 清除最后一个字符
            if len(current_equation) == 1:
                self.equation.set("0")
            else:
                self.equation.set(current_equation[:-1])
        elif button == "=":  # 等号按钮
            try:
                result = str(eval(current_equation))
                self.equation.set(result)
            except Exception as e:
                self.equation.set("error")
        elif button == "+/-":  # 正负号切换
            if current_equation.startswith("-"):
                self.equation.set(current_equation[1:])
            elif current_equation != "0":
                self.equation.set("-" + current_equation)
        elif button == "1/x":  # 倒数
            try:
                result = str(1 / float(current_equation))
                self.equation.set(result)
            except Exception as e:
                self.equation.set("error")
        elif button == "sqrt":  # 平方根
            try:
                result = str(float(current_equation) ** 0.5)
                self.equation.set(result)
            except Exception as e:
                self.equation.set("error")
        elif button == "%":  # 百分比
            try:
                result = str(float(current_equation) / 100)
                self.equation.set(result)
            except Exception as e:
                self.equation.set("error")
        elif button == ".":
            if "." not in current_equation:  # 防止重复添加小数点
                if current_equation == "0":
                    self.equation.set("0.")
                else:
                    self.equation.set(current_equation + ".")
        else:
            if current_equation == "0":
                self.equation.set(button)
            else:
                self.equation.set(current_equation + button)

# 创建主窗口并运行
if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()