s1 = int(input("Enter marks 1 :"))
s2 = int(input("Enter marks 2 :"))
s3 = int(input("Enter marks 3 :"))

s1_pr = s1*100/100
s2_pr = s2*100/100
s3_pr = s3*100/100

chek_total_pr = (s1+s2+s3)/300*100

if (chek_total_pr >= 40 and s1_pr >= 33 and s2_pr >= 33 and s1_pr >= 33 ):
    print("Congratulations! You are pass!", chek_total_pr)

else:
    print("You are fail , try agian next year", chek_total_pr)
