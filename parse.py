import re


grade = {}







def find_name(element):
    hm = str(element.findAll("a", {"class": "sg-header-heading"}))
    hm = hm[hm.index('>'):]
    hm = hm[hm.index('-'):]
    hm = hm[3:]
    ok = hm.replace("</a>]", "")

    return re.sub('\s+',' ',ok) #a lot of bullshit to extract the name, should fix with regex 
   
    
    
def find_total_avg(element):
    #grade[total_average] = re.findall('(\d+)', str(element.findAll("span", {"class": "sg-header-heading"})))
    return re.findall('(\d+)', str(element.findAll("span", {"class": "sg-header-heading"}))) #extracts avg
    
def read_grid(element):
    
    grids = element.findAll("div", {"class": "sg-content-grid"})
    for grades in grids:

        assignments = grades.findAll("tr", {"class": "sg-asp-table-data-row"})
       
        
        results = re.findall('(?s)(?<=\<td)(.*?)(?=\<\/td\>)', str(assignments[0]))
        
        
        
        date_due = results[0]
        date_assigned = results[1]
        various_things = list(filter(None, results[2].split("\n")))
        
        
        title_of_assignment = re.findall('(?<=Classwork\: ).*', str(various_things[1]))
        type_of_grade = re.findall('(?<=Classwork\: ).*', str(various_things[2]))
        due_date = re.findall('(?<=Due Date\: ).*', str(various_things[3]))
        max_points = re.findall('(?<=Max Points\: ).*', str(various_things[4]))
        can_be_dropped = re.findall('(?<=Can Be Dropped\: ).*', str(various_things[5])) #dunno what this does, but kept it for completions sake
        
        
        score = results[4]
        total_points = results[5]
        weight = results[6]
        weighted_score = results[7]
        weighted_total_points = results[8]
        percentage = results[9].strip('%')
         
        
        
        return date_due, date_assigned, title_of_assignment, type_of_grade, due_date, max_points, can_be_dropped, score, total_points, weight, weighted_score, weighted_total_points, percentage #LMAO
        
    
    
    
def main(element):
    # date_due, date_assigned, title_of_assignment, type_of_grade, due_date, max_points, can_be_dropped, score, total_points, weight, weighted_score, weighted_total_points, percentage = read_grid(element)
    # grade[find_name(element)] = {'reference_number': find_total_avg(element)[0], 
    #                               'total_average': find_total_avg(element)[1],
    #                               'date_due': date_due,
    #                               'date_assigned': date_assigned,
    #                               'title_of_assignment': title_of_assignment,
    #                               'type_of_grade': type_of_grade,
    #                               'due_date': due_date,
    #                               'max_points': max_points, 
    #                               'can_be_dropped': can_be_dropped,
    #                               'score': score,
    #                               'total_points': total_points,
    #                               'weight': weight,
    #                               'weighted_score': weighted_score,
    #                               'weighted_total_points': weighted_total_points,
    #                               'percentage': percentage                                  
    #                               }
    print(read_grid(element))
    