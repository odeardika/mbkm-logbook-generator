import json


with open("logbook-data.json", "r") as file:
    data = json.load(file)


logbook = ''
# Opening
month = data['month']
mbkm_type = data['mbkm-type']
mbkm_agency = data['mbkm-agency']
logbook += f'Pada bulan {month} mengikuti {mbkm_type} di {mbkm_agency}'

if ('extra-opening' in data):
    extra =  data['extra-opening']
    logbook += f' {extra}.'
else :
    logbook += f' saya sudah mendapatkan beberapa materi yang berguna untuk saya.'

# About Mentoring
data_mentoring = data['mentoring-activity']
if (data_mentoring['dpp-mentoring'] and data_mentoring['mentor-mentoring']):
    mentor = f'Mentor DPP dan Mentor di {mbkm_agency}'
elif(data_mentoring['dpp-mentoring']):
    mentor = f'Mentor DPP'
else:
    mentor = f'Mentor di {mbkm_agency}'
logbook += f' Untuk kegiatan mentoring pada bulan ini sudah dilakukan oleh {mentor}'
mentoring_event = data_mentoring['mentoring-info']
event_detail = mentoring_event['event']
logbook += f' dengan {event_detail}'
if ('date' in mentoring_event):
    logbook += ' pada ' + mentoring_event['date']
logbook += '.'

#task section
data_task = data['task']
if("task-intro" in data_task):
    if(data_task['task-intro'] == ''):
        logbook += f' Selama satu bulan ini saya sudah mengerjakan beberapa tugas dari {mbkm_agency}.'
    else:
        logbook += data_task['task-intro']
else:
    logbook += f' Selama satu bulan ini saya sudah mengerjakan beberapa tugas dari {mbkm_agency}.'

for i in range(len(data_task['list-task'])):
    task = data_task['list-task'][i]
    if(i == 0):
        logbook += f' Tugas yang pertama adalah '
    elif(i+1 == len(data_task['list-task'])):
        logbook += f' Tugas yang terakhir bulan ini adalah '
    else :
        logbook += f' Tugas selanjutnya adalah '
    if(task['title'] != ''):
        title = task['title']
        logbook += f'{title}'
    if(task['detail'] != ''):
        task_detail = task['detail']
        logbook += f' yaitu {task_detail}'
    if(task['team-info'] != '' and task['deadline'] != ''):
        team = task['team-info']
        deadline = task['deadline']
        assigment_type = task['assignments-type'] if (task['assignments-type'] != '') else 'dikumpulkan'
        logbook += f' Tugas ini dikerjakan {team} dan {assigment_type} {deadline}.'

#course 
data_course = data['course']
if(data_course['task-intro'] == ''):
    logbook += f'Pada bulan ini saya mendapatkan beberapa materi dari {mbkm_agency}.'
else: 
    logbook += data_course['task-intro']

for i in range(len(data_course['list-course'])):
    course = data_course['list-course'][i]
    if(i == 0):
        logbook += f' Materi yang pertama adalah '
    elif(i+1 == len(data_course['list-course'])):
        logbook += f' Materi yang terakhir bulan ini adalah '
    else :
        logbook += f' Materi selanjutnya adalah '
    if(course['title'] != '' and course['detail']):
        title = course['title']
        detail = course['detail']
        logbook += f'{title} yang mengajarkan tentang {detail}'
        
#extra and outro
logbook += data['extra']
logbook += data['outro']

with open('logbook.txt','w') as f:
    f.write(logbook)

print(f'Yours Logbook length is {len(logbook.split(' '))} words')