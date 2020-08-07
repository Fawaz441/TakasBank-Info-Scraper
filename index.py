html = '''
<table>
    <tr>
        <td>1</td>
        <td>2</td>
        <td>3</td>
        <td>4</td>
        <td>5</td>
    </tr>
    <tr>
        <td>6</td>
        <td>7</td>
        <td>8</td>
        <td>9</td>
        <td>10</td>
    </tr>
</table>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'html.parser')
rows = soup.find_all('tr')
new_list = []
for row in rows:
    row = row.contents
    row = list(filter(('\n').__ne__, row))
    new_row = []
    for stuff in row:
        new_row.append(stuff.text)
    new_list.append(new_row)
print(new_list)
