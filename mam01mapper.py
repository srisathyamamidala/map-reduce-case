# Sri Sathya 
# This is an example mapper

import sys 

# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split(",")
  if (len(datalist) == 22) : 
    fema_declaration_string,disaster_number,state,declaration_type,declaration_date,fy_declared,incident_type,declaration_title,ih_program_declared,ia_program_declared,pa_program_declared,hm_program_declared,incident_begin_date,incident_end_date,disaster_closeout_date,fips,place_code,designated_area,declaration_request_number,hash,last_refresh,id= datalist

    # print intermediate key-value pairs to standard output
    print(state,"\t",1)