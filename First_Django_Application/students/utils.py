def qs2html(qs_list):
    s = '<table>'
    for record in qs_list:
        s += f'<tr><td>{record.first_name}</td>' \
             f'<td>{record.last_name} </td>' \
             f'<td>{record.email}</td>' \
             f'<td><a href="update/{record.pk}">Edit</a>' \
             f'</tr>'
    s += '</table>'

    return s
