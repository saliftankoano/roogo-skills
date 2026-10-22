#!/usr/bin/env python3
"""Reduce the hiss and rumble a cloned voice carries, and measure the result.

Usage: nettoyer_voix.py in.wav out.wav [strength=0.9]

The noise profile is the quietest 12% of 20 ms frames (the pauses between
words). Frames of pure digital silence (below -120 dB, such as the breaks
narration.py puts between paragraphs) are left out of the profile and of the
measurement. When nothing audible sits between the words, the file is reported
as already clean and copied unchanged. Prints speech level, background level
and their gap before and after; aim for a gap above 18 dB and listen for a
metallic tone above 0.95. Needs numpy, soundfile and noisereduce.
"""
import sys

import numpy as np

SILENCE_DB = -120.0   # below this a 20 ms frame is digital silence, not background
QUIET_SHARE = 12      # percentile of audible frames used as the noise profile
MIN_BACKGROUND = 0.01  # under 1% of frames audible and well below speech: nothing to clean


def frame_db(x, win):
    n = len(x) // win
    f = x[: n * win].reshape(n, win)
    return 20 * np.log10(np.sqrt((f ** 2).mean(1)) + 1e-12)


def _mean_db(v):
    return float(10 * np.log10(np.mean(10 ** (v / 10)))) if len(v) else float("-inf")


def speech_and_background(x, sr, quiet_cut=None):
    """Mean level of loud frames (speech) and quiet frames (background), in dB.

    Digital silence is ignored; background is -inf when there is none.
    """
    d = frame_db(x, int(0.02 * sr))
    d = d[d > SILENCE_DB]
    if not len(d):
        return float("-inf"), float("-inf")
    cut = np.percentile(d, QUIET_SHARE) if quiet_cut is None else quiet_cut
    speech = d[d > np.percentile(d, 90) - 8]
    pauses = d[d < cut + 0.5]
    return _mean_db(speech), _mean_db(pauses)


def noise_profile(x, sr):
    """Samples of the quietest audible frames, the cut used, and whether any background exists."""
    win = int(0.02 * sr)
    d = frame_db(x, win)
    live = d > SILENCE_DB
    if not live.any():
        return np.zeros(0), None, False
    cut = float(np.percentile(d[live], QUIET_SHARE))
    speech = np.percentile(d[live], 90) - 8
    background = live & (d < speech - 12)        # audible, and clearly below the voice
    frames = x[: len(d) * win].reshape(len(d), win)
    noise = frames[live & (d < cut)].ravel()
    return noise, cut, background.sum() >= MIN_BACKGROUND * len(d) and len(noise) > 0


def gap_line(name, x, sr, cut, has_background=True):
    s, b = speech_and_background(x, sr, cut)
    if b == float("-inf") or not has_background:
        return f"{name:9} speech {s:6.1f} dB  background silent"
    return f"{name:9} speech {s:6.1f} dB  background {b:6.1f} dB  gap {s - b:5.1f} dB"


def main():
    import soundfile as sf

    src, dst = sys.argv[1], sys.argv[2]
    strength = float(sys.argv[3]) if len(sys.argv) > 3 else 0.9
    x, sr = sf.read(src)
    if x.ndim > 1:
        x = x.mean(1)
    noise, cut, has_background = noise_profile(x, sr)
    if not has_background:
        sf.write(dst, x, sr, subtype="PCM_16")
        print(gap_line("original", x, sr, cut, has_background=False))
        print("already clean: nothing audible between the words; copied unchanged to", dst)
        return
    import noisereduce as nr

    y = nr.reduce_noise(y=x, sr=sr, y_noise=noise, stationary=True, prop_decrease=strength, n_fft=2048)
    sf.write(dst, y, sr, subtype="PCM_16")
    for name, sig in (("original", x), ("cleaned", y)):
        print(gap_line(name, sig, sr, cut))


if __name__ == "__main__":
    main()
