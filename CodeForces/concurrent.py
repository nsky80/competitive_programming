def find_maximum_activities(activity_list,start_time_list, finish_time_list):

    selected =[]


    activity_tmp_list = [x for _,x in sorted(zip(finish_time_list,activity_list))]

    #the first activity is always selected
    i=0
    #print(i)
    selected.append(activity_tmp_list[i])

    #consider rest of Activities
    for j in range(1,len(activity_list)):

        if start_time_list[j]>=finish_time_list[i]:
            print(j)
            selected.append(activity_tmp_list[j])
            i=j
    return selected

activity_list=[1, 2, 3, 4, 5, 6]
start_time_list=[5, 4, 8, 2, 3, 1]
finish_time_list=[13, 6, 16, 7, 5, 4]

print("Activities:",activity_list)
print("Start time of the activities:",start_time_list)
print("Finishing time of the activities:", finish_time_list)

result=find_maximum_activities(activity_list,start_time_list, finish_time_list)
print("The maximum set of activities that can be completed:",result)
