# Youtube video manager Project
import json
file_name = "Youtube_manager.txt"
def load_data():
    try:
        with open(file_name,"r") as f:
           return json.load(f)
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open(file_name,"w") as f:
        json.dump(videos,f) # data, file name

def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index,video in enumerate(videos,start=1):
        print(f"{index}.video : {video["name"]} , Duration : {video["time"]} ")

    print("\n")
    print("*" * 70)


def add_video(videos):
    name = input("Enter youtube video name : ")
    time = input("Enter video duration : ")
    videos.append({"name" : name, "time" : time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    print(len(videos))
    index = int(input("Enter the video number to be update: " ))
    if 1 <= index <= len(videos):
            name = input("Enter youtube video name : ")
            time = input("Enter video duration : ")
            videos[index - 1] = {'name' : name , "time" : time}
            save_data_helper(videos)
            print("Video Success Fully Update!!")
    else:
        print("You Enter invalid video number.")   

def delete_video(videos):
    pass




def main():
    videos = load_data()
    while True:
        print("\nYoutube Manager || Choose an option.")
        print("1.List All Videos.")
        print("2.Add a Youtube video.")
        print("3.Update a Youtube video.")
        print("4.Delete a Youtube video.")
        print("5.Exit The App.")
        chioce = input("Enter Your Chioce : ")

        match chioce:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case'3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _ :
                print("\nInvaild Choice!!")
        



if __name__ == "__main__":
    main()


