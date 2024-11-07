def hello():
    print("Hello")  # This will print "Hello"

def main(hello):
    hello()  # Calls the passed function

if __name__ == "__main__":
    main(hello)  # Passes the greet function to run