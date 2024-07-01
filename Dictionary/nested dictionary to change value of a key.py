dic={
    'emp1':{
        'name':'vikas',
        'age' : '25',
        'job':'developer'

    },
    'emp2':{
        'name':'arivu',
        'age' : '26',
        'job' : 'analyst'
        }
}
dic['emp2']['name']="arivu"
print(dic)
def check_key_exists(d, key):
    if key in d:
        print(f"The key '{key}' exists in the dictionary.")
    else:
        print(f"The key '{key}' does not exist in the dictionary.")

# Example usage
check_key_exists(dic, 'emp1')
check_key_exists(dic, 'emp3')