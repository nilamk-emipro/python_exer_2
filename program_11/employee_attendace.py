emp_dict = {
            101: {'name': 'Anupriya Roy',
                  'depart_id':1,
                  'attendances':[{'date':1, 'hours':[3.5,4.5]},{'date':2, 'hours':[3.2,4.5]},{'date':3, 'hours':[3.2,4.6]},
                                 {'date':4, 'hours':[3.0,4.5]},{'date':5, 'hours':[2.5,4.5]},{'date':6, 'hours':[1.5,4.5]},
                                 {'date':7, 'hours':[2,3]},{'date':8, 'hours':[0,4.5]},{'date':9, 'hours':[2,3.5]},
                                 {'date':10, 'hours':[4,3.5]}],
                 'leaves':[{'date':7, 'no_of_hours':1.5},{'date':7, 'no_of_hours':1.5},{'date':8, 'no_of_hours':3}]
                },
            102:
             {'name': 'Kadambari Sharma',
              'depart_id': 1,
              'attendances': [{'date':1, 'hours': [0,4.5]},{'date':2, 'hours':[3.2,0]},{'date':3, 'hours':[3.2,4.6]},
                                {'date':4, 'hours':[1,4.5]},{'date':5, 'hours':[2.5,2]},{'date':6, 'hours':[1.5,1]},
                                {'date':7, 'hours':[2,4]},{'date':8, 'hours':[1,4.5]},{'date':9, 'hours':[2,2]},
                                {'date':10, 'hours':[2,3.5]}],
              'leaves': [{'date':1, 'no_of_hours':3.5},{'date':2, 'no_of_hours':2},{'date':2, 'no_of_hours':2}]
             },
            103:
            {'name': 'Abhishek Verma',
             'depart_id':1,
             'attendances':[{'date':3, 'hours':[3.2,4.6]},{'date':4, 'hours':[1,4.5]},{'date':5, 'hours':[2.5,2]},
                            {'date':6, 'hours':[1.5,1]},{'date':7, 'hours':[2,4]},{'date':8, 'hours':[1,4.5]},
                            {'date':9, 'hours':[2,2]},{'date':10, 'hours':[2,3.5]}
                ],
             'leaves':[{'date':1, 'no_of_hours':3},{'date':2, 'no_of_hours':2},{'date':2, 'no_of_hours':3}]
            }
}

for key ,values in emp_dict.items():
    #print(key,values)
    print('{employee_id :',key,',employee_name:',values['name'],',total_attendance_hours:',
          sum([sum(values['attendances'][index]['hours']) for index in range(len(values['attendances']))]),
          ',total_leave_days'
        ,sum(list(values['leaves'][index]['no_of_hours'] for index in range(len(values['leaves'])))),'}')

    print('[{',key ,':{ date :',
    (list(values['attendances'][index]['date'] for index in range(len(values['attendances'])))),
    ',total_hrs :',
    (list(sum(values['attendances'][index]['hours']) for index in range(len(values['attendances'])))),
    ',remaining_hrs :',
    (list(round(8- sum(values['attendances'][index]['hours']), 2) for index in range(len(values['attendances']))))
    ,'}}]'
    )