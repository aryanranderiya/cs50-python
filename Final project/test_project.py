import pytest
import project
import tkinter as tk

def test_get_base64_encoded_credentials():
    client_id = "test"
    client_secret = "test"

    result = project.get_base64_encoded_credentials(client_id, client_secret)

    assert result != ""

def test_display_progress_dialog():
    project.window = tk.Tk()

    project.display_progress_dialog("Test Progress")

    assert project.progress_dialog is not None

def test_print():
    assert project.print_app_name() == "Welcome to AryanSpotifyTools!"

if __name__ == "__main__":
    pytest.main()
