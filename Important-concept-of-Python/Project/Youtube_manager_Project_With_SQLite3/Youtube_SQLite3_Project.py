# Youtube Manager Project With SQLite3 Database

import sqlite3

conn = sqlite3.connect("Youtube_video.db")

cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS videos(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
        )""")



def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)


def add_video(name,time):
    cursor.execute("INSERT INTO videos(name,time) VALUES (?,?)",(name,time))
    print("Video add success Fully!!")
    conn.commit()


def update_video(new_name,new_time,video_id):
    cursor.execute("UPDATE videos SET name = ? , time = ? WHERE id = ?",(new_name,new_time,video_id))
    print("Video update success Fully!!")
    conn.commit()


def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?",(video_id,))
    print("Video delete success Fully!!")
    conn.commit()


def main():
    while True:

        print("\nYoutube Manager Project || Choose an option!!")
        print("1. List Videos")
        print("2. Add video")
        print("3. Update video")
        print("4. Delete video")
        print("5. Exit an App")
        chioce = input("Enter Your choice : ")

        match chioce:
            case '1':
                list_videos()

            case '2':
                name = input("Enter video name : ")
                time = input("Enter video time : ")
                add_video(name,time)
            case '3':
                video_id = input("Enter video ID to update : ")
                name = input("Enter video name : ")
                time = input("Enter video time : ")
                update_video(name,time,video_id)
            case '4':
                video_id = input("Enter video ID to delete : ")
                delete_video(video_id)
            case '5':
                break
            case _ :
                print("Enter a valid chioce!!")

    conn.close()




if __name__ == "__main__":
    main()



    