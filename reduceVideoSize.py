import sys
import os
from moviepy import VideoFileClip


def compress_video(input_path):
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
        print("\n no video provided.")
        print(" usage: \n")
        print(" > py reduceVideoSize.py <your_video.mp4>\n")
    else:
        compress_video(sys.argv[1])
