import time
voter_id =[1,2,3,4,5,6,7,8,9,10,11,12]
while True:
    time.sleep(5)
    run=True
    while run:
        try:
            id=int(input("Enter voter id number : "))
            run=False
        except:
            print("Enter valid voter id")
    if(id in voter_id):
        vote =input("Modi or Rahul ? ")

        normalized_vote = vote.upper()

        votes_file = open('votes.txt','a')
        if("MODI" == normalized_vote):
            voter_id.remove(id)
            print("Thanks for your vote")
            votes_file.write(f'{id} Modi \n')
        elif("RAHUL" == normalized_vote):
            voter_id.remove(id)
            print("Thanks for your vote")
            votes_file.write(f'{id} Rahul \n')
        else:
            print("That is not valid choice.")
        votes_file.close()
    else:
        print("you are voted already / you are not eligible")
