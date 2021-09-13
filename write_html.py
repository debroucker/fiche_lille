from datetime import datetime, timedelta
import cal
import files

def get_decalage(month) :
    if month in [9, 10] :
        return 2
    else :
        return 1

def get_table_html(month, grp_english):
    #all events
    html = ''
    now = datetime.now()
    total = now
    all_events = cal.get_all_dates(month, grp_english)
    #cours
    for event in all_events:
        html += '<tr style="border-style:solid;"><td width="40">'
        html += str(event.begin.day) + '/' + str(event.begin.month)
        html += '</td>'
        html += '<td width="150">' + event.name + '</td>'
        minute = event.begin.minute
        if minute == 0:
            minute = '00'
        html += '<td>' + str(event.begin.hour + get_decalage(month)) + 'h' + str(minute) + '</td>'
        duration = str(event.end - event.begin).split(':')
        html += '<td>' + duration[0] + 'h' + duration[1] + '</td>'
        if 'TPA' in event.name:  # TPA
            html += '<td>TPA</td>'
        else:  # cours
            total += (event.end - event.begin)
            html += '<td>P</td>'
        html += '<td></td>'
        html += '<td><br><br><br></td></tr>'
    #repeat 42 max
    for i in range(42-len(all_events)):
        html += '<tr style="border-style:solid;"><td width="40"></td><td width="150"></td>'
        for j in range(4):
            html += '<td></td>'
        html += '<td><br><br><br></td></tr>'
    #total
    total = total - now
    td = str(timedelta(seconds=total.seconds)).split(':')
    hour = int(td[0])
    minute = int(td[1])
    if minute == 0:
        minute = '00'
    gloab_total = str(total.days*24+hour)+'h'+str(minute)
    return html, gloab_total


def write_in_html(name, first_name, month, grp_english):
    months = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novembre', 'Decembre']
    res = ''
    html, global_total = get_table_html(month, grp_english)
    for line in files.read_file('model.html'):
        if line.strip() == '__NAME__':
            res += name
        elif line.strip() == '__FIRSTNAME__':
            res += first_name
        elif line.strip() == '__ALL_DATES__':
            res += html
        elif line.strip() == '__HOURS__':
            res += global_total
        elif line.strip() == '__MONTH__' :
            res += months[month-1]
            if month in [9,10,11,12] :
                res += ' 2021'
            else :
                res += ' 2022'
        else:
            res += line
    files.write_in_file('res.html', res)
