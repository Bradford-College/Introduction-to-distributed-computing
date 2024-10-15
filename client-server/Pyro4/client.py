import Pyro4

# Client (in a separate process)
calculator = Pyro4.Proxy("PYRO:obj_d9f284fba30042199387e5b521a013a5@localhost:9090")  # Use the URI displayed by the server
print(calculator.add(10, 5))
print(calculator.add(35, 20))