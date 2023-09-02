import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import requests
from spotipy import Spotify, SpotifyException
from spotipy.oauth2 import SpotifyOAuth
import base64
from PIL import ImageTk, Image, ImageDraw
from io import BytesIO
import cachetools
import random
import threading
import time

def revoke_access_token(access_token, client_id, client_secret):
    if access_token:
        revocation_url = "https://accounts.spotify.com/api/token"
        headers = {
            "Authorization": f"Basic {get_base64_encoded_credentials(client_id, client_secret)}"
        }
        data = {"token": access_token}
        response = requests.post(revocation_url, data=data, headers=headers)
        print(response.status_code)
        return True
    else:
        return False

def get_base64_encoded_credentials(client_id, client_secret):
    credentials = f"{client_id}:{client_secret}"
    return base64.b64encode(credentials.encode()).decode()

def fetch_all_songs(playlist_uri, sp, song_cache):
    if playlist_uri in song_cache:
        return len(song_cache[playlist_uri])

    all_tracks = []

    playlist_tracks = sp.playlist_tracks(playlist_uri)
    display_progress_dialog("Loading Songs...")
    progress_dialog.update_idletasks()

    while playlist_tracks:
        all_tracks.extend(playlist_tracks["items"])

        next_page = playlist_tracks["next"]
        if not next_page:
            close_progress_dialog()
            break

        playlist_tracks = sp.next(playlist_tracks)
        number_of_loaded_tracks = len(all_tracks)
        label_songs_loaded.config(text=f"Loading Songs... {number_of_loaded_tracks}")
        progress_dialog.update_idletasks()

    song_cache[playlist_uri] = all_tracks

    return all_tracks

def display_progress_dialog(title):
    global progress_dialog
    progress_dialog = tk.Toplevel(window)
    progress_dialog.title(title)
    progress_dialog.geometry("300x100")

    global label_songs_loaded
    label_songs_loaded = tk.Label(progress_dialog,text=title + " 0")
    global progress_bar
    progress_bar = ttk.Progressbar(progress_dialog,orient=tk.HORIZONTAL, length=220, mode="indeterminate")
    progress_bar.pack(pady=20)
    progress_bar.start
    label_songs_loaded.pack()

def close_progress_dialog():
    global progress_dialog
    if progress_dialog:
        progress_bar.stop
        progress_dialog.destroy()

class SpotifyToolsApp:
    def __init__(self, window):
        self.window = window
        window.title("Spotify Login")

        self.CLIENT_ID = "58817dcd8cc54baa9dd033ea9ef0f86f"
        self.CLIENT_SECRET = "8fe689bda9e64b3d8b4e111301cf6a44"
        self.REDIRECT_URI = "http://localhost:8888/callback"

        self.playlists = {}
        self.playlist_uris = {}
        self.text_num_song = ""
        self.song_cache = cachetools.LRUCache(maxsize=10000)

        self.frame_login = tk.Frame(self.window, width=500, height=400)
        self.frame_home = tk.Frame(self.window, width=500, height=400)
        self.frame_view_playlist = tk.Frame(self.window, width=500, height=400)
        self.frame_view_all_playlists = tk.Frame(self.window, width=500, height=300)
        self.frame_view_playlist_songs = tk.Frame(self.window, width=500, height=400)

        self.progress_dialog = None

        self.label_number_of_songs = tk.Label(self.frame_view_playlist)
        self.label_playlist_image = tk.Label(self.frame_view_playlist)
        self.label_playlist_name = tk.Label(self.frame_view_playlist)
        self.label_welcome_title = tk.Label(self.frame_login)
        self.label_user_profile_image = tk.Label(self.frame_home)
        self.label_user_profile_name = tk.Label(self.frame_home)
        self.label_image_logo = tk.Label(self.frame_login)

        self.listbox_playlists = tk.Listbox(self.frame_view_all_playlists)
        self.scrollbar_playlists = tk.Scrollbar(self.window, command=self.listbox_playlists.yview)
        self.listbox_playlists.config(yscrollcommand=self.scrollbar_playlists.set)

        self.listbox_view_songs = tk.Listbox(self.frame_view_playlist_songs)
        self.scrollbar_songs = tk.Scrollbar(self.window, command=self.listbox_view_songs.yview)
        self.listbox_view_songs.config(yscrollcommand=self.scrollbar_songs.set)

        self.button_login = tk.Button(self.frame_login, text="Login to Spotify")
        self.button_logout = tk.Button(self.frame_home)
        self.button_view_playlists = tk.Button(self.frame_home, text="View Playlists")
        self.button_back_home = tk.Button(self.frame_view_all_playlists, text="Home")
        self.button_back_view_playlists = tk.Button(self.frame_view_playlist, text="Back")
        self.button_back_view_playlist = tk.Button(self.frame_view_playlist_songs, text="Back to Playlist")
        self.button_shuffle_playlist = tk.Button(self.frame_view_playlist, text="Shuffle Playlist")
        self.button_view_songs = tk.Button(self.frame_view_playlist,text="View Songs")

        self.login_screen()

    # initialisation method ends here ^^^^^

    def login_screen(self):
        self.frame_login.pack_propagate(False)
        self.frame_login.pack(fill=tk.BOTH, expand=True)

        original_image = Image.open("spotify_logo.png")
        resized_image = original_image.resize((333, 100))
        spotify_logo = ImageTk.PhotoImage(resized_image)

        self.label_image_logo.config(image=spotify_logo)
        self.label_image_logo.image = spotify_logo
        self.label_image_logo.grid(row=0, column=0, pady=(40, 10), padx=50)

        self.label_welcome_title.config(
            text="Welcome to Aryan's SpotifyTools!",
            font=("Helvetica", 20, "bold"),
            foreground="#1ab26b")
        self.label_welcome_title.grid(row=1, column=0, pady=(10, 20), padx=30)

        self.button_login.config(command=self.login_to_spotify)
        self.button_login.grid(row=2, column=0, pady=(10, 40), padx=30)

    def login_to_spotify(self):
        self.sp_oauth = SpotifyOAuth(
            client_id=self.CLIENT_ID,
            client_secret=self.CLIENT_SECRET,
            redirect_uri=self.REDIRECT_URI,
            scope="playlist-modify-private playlist-modify-public",
            open_browser="true",
            show_dialog="true",
        )
        self.access_token = self.sp_oauth.get_access_token()
        self.sp = Spotify(auth=self.access_token["access_token"])
        self.user = self.sp.current_user()

        if self.access_token and "access_token" in self.access_token:
            print(f"Logged in as: {self.user['display_name']}")
            self.frame_login.pack_forget()
            self.home_screen()
        else:
            messagebox.showerror("Error", "Connection Unsuccessful")

    def logout(self):
        if self.access_token:
            if revoke_access_token(self.access_token["access_token"], self.CLIENT_ID, self.CLIENT_SECRET):
                print("Access token revoked successfully.")
                self.frame_home.pack_forget()
                self.frame_login.pack()
                messagebox.showinfo("Success", "Successfully logged out!")
            else:
                print("Failed to revoke access token.")

            self.user = None
            self.access_token = None
            self.sp = None

    def home_screen(self):
        self.window.title("Home")
        self.frame_home.grid_rowconfigure(0, weight=1)
        self.frame_home.grid_columnconfigure(0, weight=1)
        self.frame_home.pack_propagate(False)
        self.frame_home.pack(fill=tk.BOTH, expand=True)
        # self.button_back_home.pack_forget()
        logout_icon = Image.open("logout_icon.png")
        resized_logout_icon = logout_icon.resize((35, 35))
        self.logout_icon = ImageTk.PhotoImage(resized_logout_icon)

        self.button_logout.config(image=self.logout_icon, command=self.logout)
        self.button_logout.grid(row=1, column=3, pady=(50), padx=(10, 30))

        name, imageurl = self.fetch_user_details()
        self.display_user_profile(name, imageurl)

    def fetch_user_details(self):
        display_name = self.user["display_name"]
        profile_image_url = (
            self.user["images"][0]["url"] if self.user["images"] else None
        )

        return display_name, profile_image_url

    def display_user_profile(self, name, image_url):
        response = requests.get(image_url)
        profile_image = Image.open(BytesIO(response.content))

        width, height = profile_image.size
        mask = Image.new("L", (width, height), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, width, height), fill=255)

        circular_image = Image.new("RGBA", (width, height))
        circular_image.paste(profile_image, mask=mask)
        self.user_image = ImageTk.PhotoImage(circular_image)

        self.label_user_profile_image.config(image=self.user_image)
        self.label_user_profile_image.grid(row=1, column=0, pady=(50), padx=(30, 10))

        self.label_user_profile_name.config(
            text=name, font=("Helvetica", 25), foreground="#000"
        )
        self.label_user_profile_name.grid(row=1, column=1, pady=(50), padx=(10, 10))

        self.button_view_playlists.config(command=self.view_playlists)
        self.button_view_playlists.grid(row=2, column=0, pady=(10, 40), padx=30)

    def fetch_playlist_uri(self):
        selected_index = self.listbox_playlists.curselection()

        if selected_index:
            index = selected_index[0]
            selected_item = self.listbox_playlists.get(index)
            selected_playlist_uri = self.playlist_uris.get(selected_item, "")
            return selected_playlist_uri

    def view_playlists(self):
        self.window.title("View Playlists")
        self.frame_home.pack_forget()
        self.frame_view_all_playlists.pack(expand=True)
        self.listbox_playlists.pack(
            side="top", fill="both", expand=True, padx=20, pady=20
        )

        self.button_back_home.config(command=lambda: self.go_back_home())
        self.button_back_home.pack()

        if not self.playlists:
            display_progress_dialog("Loading Playlists...")
            self.fetch_playlists()

    def fetch_playlists(self):
        self.playlists = self.sp.current_user_playlists()

        for playlist in self.playlists["items"]:
            playlist_name = playlist["name"]
            playlist_uri = playlist["uri"]
            self.playlist_uris[playlist_name] = playlist_uri

        # self.listbox_playlists.delete(0, tk.END)

        for playlist_name in self.playlist_uris.keys():
            self.listbox_playlists.insert(tk.END, playlist_name)
            close_progress_dialog()

        self.scrollbar_playlists.pack(side="right", fill="y")
        self.scrollbar_songs.pack_forget()

        self.listbox_playlists.bind("<ButtonRelease-1>", self.on_item_selected)

        close_progress_dialog()

    def on_item_selected(self, event):
        self.frame_view_all_playlists.pack_forget()
        self.scrollbar_playlists.pack_forget()
        self.scrollbar_songs.pack_forget()

        selected_index = self.listbox_playlists.curselection()
        if selected_index:
            index = selected_index[0]
            playlist_name = self.listbox_playlists.get(index)
            # self.listbox_playlists.pack_forget()
            self.window.title(f"Playlist: {playlist_name}")
            self.frame_view_playlist.pack(fill=tk.BOTH, expand=True)
            self.frame_view_playlist.pack_propagate(False)

            self.playlist_uri = self.fetch_playlist_uri()

            self.fetch_and_display_playlist_data(playlist_name)


    def fetch_and_display_playlist_data(self, playlist_name):
        all_fetched_tracks = fetch_all_songs(self.playlist_uri, self.sp, self.song_cache)

        self.results = self.sp.playlist_tracks(self.playlist_uri)
        self.tracks = self.results["items"]
        self.track_uris = [self.track["track"]["uri"] for self.track in self.tracks]

        while self.results["next"]:
            self.results = self.sp.next(self.results)
            self.tracks = self.results["items"]
            self.track_uris.extend([self.track["track"]["uri"] for self.track in self.tracks])

        self.window.after(0, self.display_playlist_information, self.playlist_uri, playlist_name, all_fetched_tracks)

    def method_playlist_image(self):
        self.playlist_image_url = (
            self.playlist["images"][0]["url"] if self.playlist["images"] else None
        )

        response = requests.get(self.playlist_image_url)

        original_image = Image.open(BytesIO(response.content))
        resized_image = original_image.resize((100, 100))
        playlist_image = ImageTk.PhotoImage(resized_image)

        width = playlist_image.width()
        height = playlist_image.height()

        mask = Image.new("L", (width, height), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, width, height), fill=255)

        circular_image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        circular_image.paste(resized_image, mask=mask)

        self.playlist_image = ImageTk.PhotoImage(circular_image)

        self.label_playlist_image.config(image=self.playlist_image)


    def display_playlist_information(self, playlist_uri, playlist_name, num_of_tracks):

        self.playlist = self.sp.playlist(playlist_uri)

        self.method_playlist_image()

        self.playlist_name = playlist_name

        self.button_shuffle_playlist.config(command=lambda: self.shuffle_playlist_songs())
        self.button_back_view_playlists.config(command=lambda: self.go_back_view_playlists())
        self.button_view_songs.config(command=lambda: self.view_songs_in_playlist())

        self.text_num_songs = "Number of songs: " + str(len(self.track_uris))
        self.label_number_of_songs.config(text=self.text_num_songs)
        self.label_playlist_name.config(text=self.playlist_name,font=("Helvetica", 30), foreground="#000")

        self.label_playlist_image.pack(anchor="n", pady=(30, 10))
        self.label_playlist_name.pack(anchor="n")
        self.label_number_of_songs.pack(anchor="n", pady=(10, 20))
        self.button_shuffle_playlist.pack(anchor="n", pady=(0, 10))
        self.button_view_songs.pack(anchor="n", pady=(0, 10))

        self.button_back_view_playlists.pack(anchor="n", pady=(0, 20))

    def view_songs_in_playlist(self):
        self.frame_view_playlist_songs.pack()
        self.frame_view_playlist.pack_forget()
        self.listbox_view_songs.pack(anchor='n', padx=20, pady=20)

        self.scrollbar_songs.pack(side="right", fill="y")
        self.scrollbar_playlists.pack_forget()

        self.button_back_view_playlist.config(command=lambda: self.go_back_view_playlist_info())

        self.button_back_view_playlist.pack(anchor='n')

        self.listbox_view_songs.delete(0, tk.END)

        def fetch_songs():
            for track_uri in self.track_uris:
                track = self.sp.track(track_uri)
                track_name = track["name"]
                self.listbox_view_songs.insert(tk.END, track_name)

        song_thread = threading.Thread(target=fetch_songs)
        song_thread.start()

    def go_back_view_playlist_info(self):
        self.frame_view_playlist_songs.pack_forget()
        self.frame_view_playlist.pack()

    def shuffle_playlist_songs(self):

        batch_size = 100
        batches = [self.track_uris[i:i + batch_size] for i in range(0, len(self.track_uris), batch_size)]

        try:
            random.shuffle(batches[0])
            self.sp.playlist_replace_items(self.playlist_uri, batches[0])

            for batch in batches[1:]:
                random.shuffle(batch)
                self.sp.playlist_add_items(self.playlist_uri, batch)

            print("Playlist shuffled successfully.")

        except SpotifyException as e:
            print(f"Error updating playlist: {str(e)}")

        print(f"Playlist Image URL: {self.playlist_image_url}")
        time.sleep(2)
        self.method_playlist_image()
        print(f"Playlist Image URL: {self.playlist_image_url}")


    def go_back_view_playlists(self):
        self.frame_view_playlist.pack_forget()
        self.frame_view_all_playlists.pack()
        self.frame_view_all_playlists.pack_propagate(False)
        self.playlist_image_url = "https://upload.wikimedia.org/wikipedia/commons/a/ac/Default_pfp.jpg"
        self.playlist_name = None
        self.text_num_songs = None
        self.window.update_idletasks()
        self.view_playlists()

    def go_back_home(self):
        self.frame_view_all_playlists.pack_forget()
        self.home_screen()

def main():
    print(print_app_name)
    global window
    window = tk.Tk()
    SpotifyToolsApp(window)
    window.mainloop()

def print_app_name():
    return "Welcome to AryanSpotifyTools!"

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nKeyboard Interrupted Program Execution!")
