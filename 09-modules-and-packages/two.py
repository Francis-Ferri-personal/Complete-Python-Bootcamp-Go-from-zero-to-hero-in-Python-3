import one
print("Top level en two.py")

one.func()

if __name__ == "__main__":
    print("two.py esta corriendo directamente")
else:
    print("two.py ha sido importado")
