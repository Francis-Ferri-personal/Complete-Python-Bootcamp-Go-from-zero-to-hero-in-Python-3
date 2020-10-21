def func():
    print("func() en one.PY")

def function():
    pass

def function2():
    pass

print("Top level en one.py")

if __name__ == "__main__":
    print("one.py esta siendo ejecuutado directamente")
    # Correr el script
    function()
    function2()
else:
    print("one.py ha sido importado")


