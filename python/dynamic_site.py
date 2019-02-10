from bottle import route, run, template


######################################################
## Play with this function
######################################################
def string_fun(any_string):
    ''' Change this function to alter the string. '''

    # Try out the string manipulations below by
    # 'commenting out' and 'uncommenting' the
    # 'new_string =' statements below.
    
    # Change the string to all caps
    new_string = any_string.upper()
    
    # Change the string tall lowercase
    #new_string = any_string.lower()
    
    # Prepend your string
    #new_string = ' my best friend, ' + any_string
    
    # Multiply your string!
    #new_string = 4*any_string
    
    # Don't worry about totally understanding the
    # syntax. We are using Python to convert the
    # string to binary
    byte_array = bytearray(any_string,'utf-8')
    binary_string = ''
    for byte in byte_array:
        binary_string += ' ' + str(bin(byte))[2:]
    #new_string = binary_string
    
    # This is fancy syntax to reverse a string.
    #new_string = any_string[::-1]
    
    return new_string
######################################################



@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!',name=string_fun(name))
    
@route('/')
def index():
    return template('<b>Try the <a href="{{ hw }}">{{ hw }}</a> function.</b>',hw="hello/world")
    
run(host='localhost',port=8080)
