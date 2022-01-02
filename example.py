from def_switch import *


# ******************************#
#####Creator Bagishev Aslan##########
#####Creator Parvin Allahverdiev#####
# ******************************#

def main():
    # Below, I created a dictionary by keys, calls the functions that I placed in the def_switch file and each key calls the corresponding function, as opposed to the user's choice
    while True:  # Unlike the user's choice, a key is looked for in the dictionary and when the key is found, it calls the function from def_switch
        switcher = {
            0: quit,
            1: adduser,
            2: removeuser,
            3: User_Conclusion,
            4: Addingaworkshop,
            5: Carworkshopremoval,
            6: Conclusion_of_auto_repair_shops,
            7: Searchastomaster_workshops_by_city,
            8: car_workshop_meeting,
            9: Delete_appointment,
            10: change_meeting_time,
            11: conclusion_meetings,
        }

        def select(argument):
            func = switcher.get(argument, "nothing")
            return func()

        print(
            '\n 1) To add a user \t\t\t\t\t\t\t2) To delete a user\n 3) To display users \t\t\t\t\t\t4) To add a workshop\n'
            ' 5) To delete a workshop\t\t\t\t\t6) To display all workshops \n 7) To search for car services in the city\t8) Create an appointment with a car workshop\n 9) Delete appointment \t\t\t\t\t\t10) Change meeting time\n 11) View all meetings\t\t\t\t\t\t0) Exit\n')

        select(int(input(" Your choice: ")))  # The user selects the function he wants to use


if __name__ == '__main__':
    main()
