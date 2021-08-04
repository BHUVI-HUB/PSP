# Harmful

result_list = ['True', 'False', 'File not found']
result_string = ''
for result in result_list:
result_string += result


# Idiomatic

result_list = ['True', 'False', 'File not found']
result_string = ''.join(result_list)
