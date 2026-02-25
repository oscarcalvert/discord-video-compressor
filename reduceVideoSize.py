import sys
import os
import msvcrt
from moviepy import VideoFileClip


def compress_video(input_path):
    # defines 8mb limit to stay under discord/email attachment thresholds
    target_size_mb = 8.0

    print("\nanalysing video ...")
    try:
        clip = VideoFileClip(input_path)
    except Exception as e:
        print(
            f"\n couldnt find video. recommended video format: mp4.\n detailed error: {e}"
        )
        return

    duration = clip.duration
    print(f"duration: {duration:.2f} seconds.")

    # converts mb to bits and divides by seconds to get bits per second
    total_target_bps = (target_size_mb * 1024 * 1024 * 8) / duration

    audio_bps = 128000

    video_bps = total_target_bps - audio_bps

    if video_bps < 100000:
        print(
            "the video you uploaded is very long. the video quality may be greatly affected."
        )
    else:
        print(f"new video bitrate: ~{int(video_bps/1000)} kbps.")

    filename, _ = os.path.splitext(os.path.basename(input_path))

    output_path = f"compressed_{filename}.mp4"

    print("starting compression ...")
    print("-" * 50)

    # library function to encode video with calculated bitrate constraints
    clip.write_videofile(
        output_path,
        bitrate=f"{int(video_bps)}",
        audio_bitrate="128k",
        preset="medium",
        logger="bar",
    )

    print("-" * 50)

    final_size_mb = os.path.getsize(output_path) / (1024 * 1024)
    print(f"complete. your video is now ~ {final_size_mb:.2f} MB.")
    print(f"saved as: {output_path}\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        valid_extensions = (".mp4", ".mov", ".mkv", ".avi", ".webm", ".wmv")
        current_files = [
            f
            for f in os.listdir(".")
            if os.path.isfile(f) and f.lower().endswith(valid_extensions)
        ]

        if not current_files:
            print("\n no supported video files found in this folder.\n")
            sys.exit()

        selected_index = 0

        while True:
            os.system("cls" if os.name == "nt" else "clear")

            print("available videos (click enter to select):\n")

            for i, file in enumerate(current_files):
                if i == selected_index:
                    print(f"    -> [ {file} ]")
                else:
                    print(f"       [ {file} ]")

            # catch single keystroke without enter
            key = msvcrt.getch()

            # handles escape sequences for arrow keys on windows
            if key == b"\xe0":
                arrow = msvcrt.getch()
                # up arrow key
                if arrow == b"H":
                    selected_index = (selected_index - 1) % len(current_files)
                # down arrow key
                elif arrow == b"P":
                    selected_index = (selected_index + 1) % len(current_files)

            # up navigation with w key
            elif key.lower() == b"w":
                selected_index = (selected_index - 1) % len(current_files)

            # down navigation with s key
            elif key.lower() == b"s":
                selected_index = (selected_index + 1) % len(current_files)

            elif key in (b"\r", b"\n"):
                compress_video(current_files[selected_index])
                break

            # handles ctrl+c interrupt signal
            elif key == b"\x03":
                print("\n exiting...")
                break
    else:
        compress_video(sys.argv[1])
