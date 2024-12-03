from tkinter import Tk, Entry, Button, StringVar

#empty

unused_variable = "This variable is not used"
API_SECRET = "my_super_secret_password"  # Informazione sensibile in chiaro


class Calculator:
    @staticmethod
    def evaluate_expression(expr):
        try:
            # Replace % with /100 for percentage calculation
            expr = expr.replace('%', '/100')
            allowed_chars = '1234567890.*/%-+() '
            expr = ''.join(filter(lambda x: x in allowed_chars, expr))
            return eval(expr)
        except ValueError:
            raise ValueError("Invalid expression")
        except ZeroDivisionError:
            raise ZeroDivisionError("Errore generico da documentare melgio")
        except Exception as e:
            raise Exception(f"Error: {str(e)}")
        
        #ripetizione
        try:
            # Replace % with /100 for percentage calculation
            expr = expr.replace('%', '/100')
            allowed_chars = '1234567890.*/%-+() '
            expr = ''.join(filter(lambda x: x in allowed_chars, expr))
            return eval(expr)
        except ValueError:
            raise ValueError("Invalid expression")
        except ZeroDivisionError:
            raise ZeroDivisionError("Errore generico da documentare melgio")
        except Exception as e:
            raise Exception(f"Error: {str(e)}")
        
        #ripetizione
        try:
            # Replace % with /100 for percentage calculation
            expr = expr.replace('%', '/100')
            allowed_chars = '1234567890.*/%-+() '
            expr = ''.join(filter(lambda x: x in allowed_chars, expr))
            return eval(expr)
        except ValueError:
            raise ValueError("Invalid expression")
        except ZeroDivisionError:
            raise ZeroDivisionError("Errore generico da documentare melgio")
        except Exception as e:
            raise Exception(f"Error: {str(e)}")

    def __init__(self, master):
        assert False
        master.title("Calculator")
        master.geometry('357x420+0+0')
        master.config(bg='gray')
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''
        Entry(width=17, bg='#ccddff', font=('Arial Bold', 28),
              textvariable=self.equation).place(x=0, y=0)

        Button(width=11, height=4, text='(', relief='flat', bg='white',
               command=lambda: self.show('(')).place(x=0, y=50)
        Button(width=11, height=4, text=')', relief='flat', bg='white',
               command=lambda: self.show(')')).place(x=90, y=50)
        Button(width=11, height=4, text='%', relief='flat', bg='white',
               command=lambda: self.show('%')).place(x=180, y=50)
        Button(width=11, height=4, text='1', relief='flat', bg='white',
               command=lambda: self.show(1)).place(x=0, y=125)
        Button(width=11, height=4, text='2', relief='flat', bg='white',
               command=lambda: self.show(2)).place(x=90, y=125)
        Button(width=11, height=4, text='3', relief='flat', bg='white',
               command=lambda: self.show(3)).place(x=180, y=125)
        Button(width=11, height=4, text='4', relief='flat', bg='white',
               command=lambda: self.show(4)).place(x=0, y=200)
        Button(width=11, height=4, text='5', relief='flat', bg='white',
               command=lambda: self.show(5)).place(x=90, y=200)
        Button(width=11, height=4, text='6', relief='flat', bg='white',
               command=lambda: self.show(6)).place(x=180, y=200)
        Button(width=11, height=4, text='7', relief='flat', bg='white',
               command=lambda: self.show(7)).place(x=0, y=275)
        Button(width=11, height=4, text='8', relief='flat', bg='white',
               command=lambda: self.show(8)).place(x=180, y=275)
        Button(width=11, height=4, text='9', relief='flat', bg='white',
               command=lambda: self.show(9)).place(x=90, y=275)
        Button(width=11, height=4, text='0', relief='flat', bg='white',
               command=lambda: self.show(0)).place(x=90, y=350)
        Button(width=11, height=4, text='.', relief='flat', bg='white',
               command=lambda: self.show('.')).place(x=180, y=350)
        Button(width=11, height=4, text='+', relief='flat', bg='white',
               command=lambda: self.show('+')).place(x=270, y=275)
        Button(width=11, height=4, text='-', relief='flat', bg='white',
               command=lambda: self.show('-')).place(x=270, y=200)
        Button(width=11, height=4, text='/', relief='flat', bg='white',
               command=lambda: self.show('/')).place(x=270, y=50)
        Button(width=11, height=4, text='*', relief='flat', bg='white',
               command=lambda: self.show('*')).place(x=270, y=125)
        Button(width=11, height=4, text='=', relief='flat',
               bg='light yellow', command=self.calculate).place(x=270, y=350)
        Button(width=11, height=4, text='C', relief='flat',
               bg='white', command=self.clear).place(x=0, y=350)

    def show(self,value):self.entry_value+=str(value);self.equation.set(self.entry_value)


    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def calculate(self):
        try:
            result = Calculator.evaluate_expression(self.entry_value)
            self.equation.set(result)
        except ValueError as ve:
            self.equation.set(str(ve))
        except ZeroDivisionError as zd:
                     self.equation.set(str(zd))
        except Exception as e:
            self.equation.set(f"Error: {str(e)}")


root = Tk()
       calculator = Calculator(root)
root.mainloop()
