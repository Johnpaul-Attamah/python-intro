"""
      (Q1)  Write a program to find the eligibility of admission for a professional 
      course based on the following criteria:
        Eligibility Criteria : 
        Marks in Maths >=65 and Marks in Phy >=55 and Marks in Chem>=50 
        and Total in all three subject >=190 or Total in Maths and Physics >=140
        --------------------------Format-------------------------
        Input the marks obtained in Physics :65 Input the marks obtained in Chemistry :51 
        Input the marks obtained in Mathematics :72 
        Total marks of Maths, Physics and Chemistry : 188
         Total marks of Maths and Physics : 137 
         The candidate is not eligible.
        Expected Output :
        The candidate is not eligible for admission.
    """


#math >= 65
#chem >= 50
#phy  >= 55
#all_subjects >= 190
#total_maths_&_physic >= 140


physics = int(input('Input the marks obtained in Physics: '))
chem = int(input('Input the marks obtained in Chemistry: '))
maths = int(input('Input the marks obtained in Mathematics: '))

if ((maths + physics >= 140 or chem + maths + physics >= 190) and 
(maths >= 65 and chem >= 50 and physics >= 55)):
    message = "The candidate is eligible for admission."
else:
    message = "The candidate is not eligible for admission."

print(message)
