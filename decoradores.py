def hello(name='Jose'):
    print('The hello() function has been executed')

    def greet():
        return '\t This is inside the greet() function'

    def welcome():
        return "\t This is inside the welcome() function"

    def nome(nome):
        return f'\t Hello mr. {nome}'

    print(greet())
    print(welcome())
    print(nome(name))
    print("Now we are back inside the hello() function")

hello()
#nome()