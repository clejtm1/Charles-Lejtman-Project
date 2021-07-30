#py PowerVerbs.py
#Find the power verbs listed in Towson that overlap with the verbs in the job description
def Overlap(powerVerbs_file,jobDescription_file, resume_file):
    with open(powerVerbs_file, 'r') as open_file:
       powerVerbs = open_file.read()
       powerVerbs=powerVerbs.split()
      
    with open(jobDescription_file, 'r') as open_file:
       jobDescription = open_file.read()
       jobDescription=jobDescription.split()
       power_job_overlapping_set=set(())
       #for x in nums2:
       #    nums2_set.add(int(x))
    for i in powerVerbs:
        for j in jobDescription:
            if i[:5].lower()==j[:5].lower():
                power_job_overlapping_set.add(i.lower())
    
    with open(resume_file, 'r') as open_file:
       resume = open_file.read()
       resume=resume.split()
       resume_set=set(())
    for i in power_job_overlapping_set:
        for j in resume:
            if i[:5].lower()==j[:5].lower():
                resume_set.add(i.lower())
    print("Power Verbs that are in the job description and the resume:")
    for x in resume_set:
        print(x)
    print("Power Verbs that are in the description but not the resume")
    power_verbs_needed=resume_set.symmetric_difference(power_job_overlapping_set)
    for x in power_verbs_needed:
        print(x)
    
   
if __name__=="__main__":
    Overlap('powerVerbs.txt','jobDescription.txt','Charles_Lejtman_Resume.txt')
