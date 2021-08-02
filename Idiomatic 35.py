# Harmful

unique_surnames = []
for surname in employee_surnames:
if surname not in unique_surnames:
unique_surnames.append(surname)
def display(elements, output_format='html'):
if output_format == 'std_out':
for element in elements:
print(element)
elif output_format == 'html':
as_html = '<ul>'
for element in elements:
as_html += '<li>{}</li>'.format(element)
return as_html + '</ul>'
else:
raise RuntimeError('Unknown format
                   {}'.format(output_format))


# Idiomatic

                   unique_surnames = set(employee_surnames)
def display(elements, output_format='html'):
if output_format == 'std_out':
for element in elements:
print(element)
elif output_format == 'html':
as_html = '<ul>'
for element in elements:
as_html += '<li>{}</li>'.format(element)
return as_html + '</ul>'
else:
raise RuntimeError('Unknown format
                   {}'.format(output_format))
