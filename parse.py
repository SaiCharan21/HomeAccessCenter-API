import re


grade = {}


def get_number(local_result):
    return re.findall("\d+\.\d+", local_result)[0]



def find_name(element):
    hm = str(element.findAll("a", {"class": "sg-header-heading"}))
    hm = hm[hm.index('>'):]
    hm = hm[hm.index('-'):]
    hm = hm[3:]
    ok = hm.replace("</a>]", "")




    return str(re.sub('\s+',' ',ok)) #a lot of bullshit to extract the name, should fix with regex 
   
    
    
def find_total_avg(element):
    #grade[total_average] = re.findall('(\d+)', str(element.findAll("span", {"class": "sg-header-heading"})))
    return re.findall('(\d+)', str(element.findAll("span", {"class": "sg-header-heading"}))) #extracts avg
    
    
    
def get_grid(element, name):

    results = re.findall('(?s)(?<=\<td)(.*?)(?=\<\/td\>)', str(element))


    date_due = results[0]
    date_assigned = results[1]
    
    various_things = list(filter(None, results[2].split("\n")))            
    title_of_assignment = str(re.findall('(?<=Classwork\: ).*', str(various_things[2])))
    type_of_grade = re.findall('(?<=Category\: ).*', str(various_things[3]))
    due_date = re.findall('(?<=Due Date\: ).*', str(various_things[4]))
    max_points = re.findall('(?<=Max Points\: ).*', str(various_things[5]))
    can_be_dropped = re.findall('(?<=Can Be Dropped\: ).*', str(various_things[6])) #dunno what this does, but kept it for completions sake
    
    score = get_number(results[4]) #actual grade
    total_points = get_number(results[5])
    weight = get_number(results[6])
    weighted_score = get_number(results[7])
    weighted_total_points = get_number(results[8])
    percentage = get_number(results[9]) 
     
    li = date_due, date_assigned, title_of_assignment, type_of_grade, due_date, max_points, can_be_dropped, score, total_points, weight, weighted_score, weighted_total_points, percentage


    
    

    grade[title_of_assignment] = {'score': score,
                                      'date_due': date_due,
                                      'date_assigned': date_assigned,
                                      'title_of_assignment': title_of_assignment,
                                      'type_of_grade': type_of_grade,
                                      'due_date': due_date,
                                      'max_points': max_points, 
                                      'can_be_dropped': can_be_dropped,
                                      'total_points': total_points, #pretty sure this is the same as 'score' 
                                      'weight': weight,
                                      'weighted_score': weighted_score,
                                      'weighted_total_points': weighted_total_points,
                                      'percentage': percentage                                  
                                      }
    return grade
            
            


def main(element, dict):
    
    name = find_name(element)
    grid = element.findAll("table", {"class": "sg-asp-table"})
    a = []

    for grades in grid:
        gamer = grades.findAll("tr", {"class": "sg-asp-table-data-row"})
        assignments = gamer[: len(gamer) - 3]
        
    

        for assignment in assignments:
            try:
                a = get_grid(assignment, name)
            except IndexError: #it tries to parse the major minor and other averages, that dont match the normal logic, so it errors out, i need to fix this
                pass
            dict[name] = a
            print("\n")
            
            
     
    #return dict[' SPAN 2 (KVA) A ']["['MAJOR Written: My last trip (Mi viaje a ...) - past tense/trip vocab']"]
    return dict.keys()
    




# def main(element):
    # date_due, date_assigned, title_of_assignment, type_of_grade, due_date, max_points, can_be_dropped, score, total_points, weight, weighted_score, weighted_total_points, percentage = get_grid(element)
    # grade[find_name(element)] = {'reference_number': find_total_avg(element)[0], 
                                  # 'total_average': find_total_avg(element)[1],
                                  # 'date_due': date_due,
                                  # 'date_assigned': date_assigned,
                                  # 'title_of_assignment': title_of_assignment,
                                  # 'type_of_grade': type_of_grade,
                                  # 'due_date': due_date,
                                  # 'max_points': max_points, 
                                  # 'can_be_dropped': can_be_dropped,
                                  # 'score': score,
                                  # 'total_points': total_points,
                                  # 'weight': weight,
                                  # 'weighted_score': weighted_score,
                                  # 'weighted_total_points': weighted_total_points,
                                  # 'percentage': percentage                                  
                                  # }
    # return grade