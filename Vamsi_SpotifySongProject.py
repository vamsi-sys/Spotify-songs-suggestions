import tkinter as tk
import pandas as pd

def load_data(file_path):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    return df

def get_unique_values(column_name):
    # Get unique values from the specified column
    unique_values = df[column_name].unique()
    return unique_values

def get_sorted_tracks(playlist_name, playlist_genre, playlist_subgenre):
    # Filter the DataFrame based on the selected values
    filtered_df = df[
        (df['playlist_name'] == playlist_name) &
        (df['playlist_genre'] == playlist_genre) &
        (df['playlist_subgenre'] == playlist_subgenre)
    ]
    tracks = filtered_df['track_name'].tolist()
    tracks.sort()
    return tracks

def search_songs():
    # Get the selected values from the dropdowns
    selected_playlist = playlist_var.get()
    selected_genre = genre_var.get()
    selected_subgenre = subgenre_var.get()

    # Get the sorted tracks based on the selected values
    tracks = get_sorted_tracks(selected_playlist, selected_genre, selected_subgenre)

    # Clear the current items in the list box
    list_box.delete(0, 'end')

    # Display the sorted tracks in the list box
    for track in tracks:
        list_box.insert('end', track)

# Create the main window
window = tk.Tk()
window.title("Spotify Songs Project by Vamsi")

# Load the data from the CSV file
df = load_data("E:\Spotify Songs Project\Spotify Songs Project\spotify_dataset.csv")

# Create the playlist_name dropdown
playlist_var = tk.StringVar(window)
playlist_label = tk.Label(window, text="Playlist Name:")
playlist_label.pack(anchor='w', padx=10, pady=5)
playlist_dropdown = tk.OptionMenu(window, playlist_var, *get_unique_values('playlist_name'))
playlist_dropdown.config(width=20)
playlist_dropdown.pack(anchor='w', padx=10)

# Create the playlist_genre dropdown
genre_var = tk.StringVar(window)
genre_label = tk.Label(window, text="Playlist Genre:")
genre_label.pack(anchor='w', padx=10, pady=5)
genre_dropdown = tk.OptionMenu(window, genre_var, *get_unique_values('playlist_genre'))
genre_dropdown.config(width=20)
genre_dropdown.pack(anchor='w', padx=10)

# Create the playlist_subgenre dropdown
subgenre_var = tk.StringVar(window)
subgenre_label = tk.Label(window, text="Playlist Subgenre:")
subgenre_label.pack(anchor='w', padx=10, pady=5)
subgenre_dropdown = tk.OptionMenu(window, subgenre_var, *get_unique_values('playlist_subgenre'))
subgenre_dropdown.config(width=20)
subgenre_dropdown.pack(anchor='w', padx=10)

# Create the search button
search_button = tk.Button(window, text="Search My Song", command=search_songs)
search_button.pack(anchor='w', padx=10, pady=10)

# Create the empty list box
list_box = tk.Listbox(window, width=40)
list_box.pack(fill='both', expand=True, padx=10)

# Start the GUI event loop
window.mainloop()
