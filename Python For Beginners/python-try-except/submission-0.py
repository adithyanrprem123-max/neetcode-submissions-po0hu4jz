def divide_numbers(a: int, b: int) -> None:
    try:
        result = a / b
        print(result)
    except:
        print("An error occurred!")


divide_numbers(5,1)
divide_numbers(4,1)
divide_numbers(5,0)