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
    pass

def add_video(videos):
    pass

def update_video(videos):
    pass

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


