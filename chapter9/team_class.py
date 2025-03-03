class StackOverFlow:
    
    def __init__(self, member1, member2, member3, member4, member5, team_name="StackOverflowed"):
       
        self.member1 = member1
        self.member2 = member2
        self.member3 = member3
        self.member4 = member4
        self.member5 = member5
        self.team_name = team_name

    
    def change_member_name(self, member_num, new_name):
        if member_num == 1:
            self.member1 = new_name
        elif member_num == 2:
            self.member2 = new_name
        elif member_num == 3:
            self.member3 = new_name
        elif member_num == 4:
            self.member4 = new_name
        elif member_num == 5:
            self.member5 = new_name
        else:
            print("Invalid member number!")

    
    def display_team_info(self):
        print(f"Team Name: {self.team_name}")
        print(f"Member 1: {self.member1}")
        print(f"Member 2: {self.member2}")
        print(f"Member 3: {self.member3}")
        print(f"Member 4: {self.member4}")
        print(f"Member 5: {self.member5}")



team = StackOverFlow("Lindo", "Courteney", "Ulrich", "Tom", "Phomello")


team.display_team_info()

# Change the surname of the first member (Lindo → Yende)
team.change_member_name(2, "Cook")

# Display updated team details
team.display_team_info()




