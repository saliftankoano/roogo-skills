#!/usr/bin/env python3
"""Lay the narration and a music bed under the silent video.

Usage: mixer.py --video silent.mp4 --narration narration.wav --music music.mp3 --out final.mp4
                [--delay 2.0] [--music-db -17] [--lift 3.2]

The music runs from the first to the last frame: lifted over the title card,
ducked by a sidechain under the voice, lifted again once the narration ends,
faded over the last 2.8 s. The mix is normalized to -16 LUFS.
"""
import argparse, subprocess


def seconds(path):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                                 path], check=True, capture_output=True, text=True).stdout)


def music_gain(delay, voice_end, lift):
    """ffmpeg volume expression: lift before the voice and after it, 1 under it."""
    down = delay - 0.4
    return (f"if(lt(t,{down:.2f}),{lift},if(lt(t,{delay:.2f}),{lift}-(t-{down:.2f})*{(lift - 1) / 0.4:.2f},"
            f"if(lt(t,{voice_end:.2f}),1,min({lift},1+(t-{voice_end:.2f})*{(lift - 1) / 0.5:.2f}))))")


def build_command(video, narration, music, out, delay=2.0, music_db=-17, lift=3.2):
    total = seconds(video)
    voice_end = delay + seconds(narration) + 0.2
    ms = int(delay * 1000)
    graph = (f"[0:a]aresample=48000,aformat=channel_layouts=stereo,adelay={ms}|{ms},apad=whole_dur={total:.3f},asplit=2[n][sc];"
             f"[1:a]aresample=48000,aformat=channel_layouts=stereo,atrim=0:{total:.3f},volume={music_db}dB,"
             f"volume='{music_gain(delay, voice_end, lift)}':eval=frame,afade=t=in:d=1.2,afade=t=out:st={total - 2.8:.3f}:d=2.8[m];"
             "[m][sc]sidechaincompress=threshold=0.02:ratio=6:attack=20:release=600[md];"
             "[n][md]amix=inputs=2:duration=longest:normalize=0,loudnorm=I=-16:TP=-1.5:LRA=11[a]")
    return ["ffmpeg", "-y", "-loglevel", "error", "-i", narration, "-i", music, "-i", video,
            "-filter_complex", graph, "-map", "2:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
            "-ar", "48000", "-t", f"{total:.3f}", "-movflags", "+faststart", out]


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    for k in ("video", "narration", "music", "out"):
        ap.add_argument(f"--{k}", required=True)
    ap.add_argument("--delay", type=float, default=2.0)
    ap.add_argument("--music-db", type=float, default=-17)
    ap.add_argument("--lift", type=float, default=3.2)
    a = ap.parse_args()
    subprocess.run(build_command(a.video, a.narration, a.music, a.out, a.delay, a.music_db, a.lift), check=True)
    print("saved", a.out)
