# import #
def main():
    try:
        n1, n2 = eval(input("Enter two numbers, separated by a comma:"))
        result = n1 / n2
    except ZeroDivisionError:
        print("Division by zero!")
    except SyntaxError:
        print("A comma may be missing in the input!")
    except:
        print("Something wrong in the input!")
    else:
        print("The result is:", result)
    finally:
        print("executing the final clause!")
main()