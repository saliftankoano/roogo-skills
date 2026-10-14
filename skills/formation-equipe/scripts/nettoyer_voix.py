#!/usr/bin/env python3
"""Reduce the hiss and rumble a cloned voice carries, and measure the result.

Usage: nettoyer_voix.py in.wav out.wav [strength=0.9]

The noise profile is the quietest 12% of 20 ms frames (the pauses between
words). Prints speech level, background level and their gap before and after;
aim for a gap above 18 dB and listen for a metallic tone above 0.95.
Needs numpy, soundfile and noisereduce.
"""
import sys

import numpy as np


def frame_db(x, win):
    n = len(x) // win
    f = x[: n * win].reshape(n, win)
    return 20 * np.log10(np.sqrt((f ** 2).mean(1)) + 1e-12)


def speech_and_background(x, sr, quiet_cut=None):
    """Mean level of loud frames (speech) and quiet frames (background), in dB."""
    d = frame_db(x, int(0.02 * sr))
    cut = np.percentile(d, 12) if quiet_cut is None else quiet_cut
    speech = d[d > np.percentile(d, 90) - 8]
    pauses = d[d < cut + 0.5]
    mean = lambda v: 10 * np.log10(np.mean(10 ** (v / 10)))
    return mean(speech), mean(pauses)


def main():
    import noisereduce as nr
    import soundfile as sf

    src, dst = sys.argv[1], sys.argv[2]
    strength = float(sys.argv[3]) if len(sys.argv) > 3 else 0.9
    x, sr = sf.read(src)
    if x.ndim > 1:
        x = x.mean(1)
    win = int(0.02 * sr)
    d = frame_db(x, win)
    cut = np.percentile(d, 12)
    frames = x[: len(d) * win].reshape(len(d), win)
    noise = frames[d < cut].ravel()
    y = nr.reduce_noise(y=x, sr=sr, y_noise=noise, stationary=True, prop_decrease=strength, n_fft=2048)
    sf.write(dst, y, sr, subtype="PCM_16")
    for name, sig in (("original", x), ("cleaned", y)):
        s, b = speech_and_background(sig, sr, cut)
        print(f"{name:9} speech {s:6.1f} dB  background {b:6.1f} dB  gap {s - b:5.1f} dB")


if __name__ == "__main__":
    main()
