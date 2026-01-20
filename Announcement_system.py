announcements = []

def post_announcement():
    title = input("Enter announcement title: ")
    message = input("Enter announcement message: ")
    announcements.append({"title": title, "message": message})
    print("Announcement posted")

def view_announcements():
    if not announcements:
        print("No announcements available")
    else:
        for ann in announcements:
            print("Title:", ann["title"])
            print("Message:", ann["message"])
            print("----------------")

def main():
    while True:
        print("1. Post Announcement")
        print("2. View Announcements")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            post_announcement()
        elif choice == "2":
            view_announcements()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
