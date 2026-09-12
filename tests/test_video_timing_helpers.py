"""Cover the timing maths that two ad formats depend on; no media needed."""

import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


def load(relative_path, name):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


xfade = load("skills/appel-proprietaires/scripts/xfade_timeline.py", "xfade_timeline")
captions = load("skills/video-avantage/scripts/caption_timing.py", "caption_timing")


class XfadeTimelineTests(unittest.TestCase):
    durations = [5.6, 3.8, 2.6, 4.9]
    xfade_seconds = 0.4

    def test_chain_is_shorter_than_the_naive_sum(self):
        self.assertAlmostEqual(
            xfade.chain_length(self.durations, self.xfade_seconds), 15.7, places=6)
        self.assertAlmostEqual(sum(self.durations), 16.9, places=6)

    def test_single_clip_chain_loses_nothing(self):
        self.assertAlmostEqual(xfade.chain_length([7.5], 0.4), 7.5, places=6)

    def test_empty_chain_is_zero(self):
        self.assertEqual(xfade.chain_length([], 0.4), 0.0)

    def test_card_windows_use_the_post_transition_timeline(self):
        windows = xfade.clip_windows(self.durations, self.xfade_seconds)
        # The naive cumulative start of the last clip is 12.0; every prior
        # transition shifts it earlier by one crossfade.
        self.assertAlmostEqual(windows[-1][0], 10.8, places=6)
        self.assertAlmostEqual(
            windows[-1][1], xfade.chain_length(self.durations, self.xfade_seconds),
            places=6)

    def test_windows_start_at_zero_and_overlap_by_one_crossfade(self):
        windows = xfade.clip_windows(self.durations, self.xfade_seconds)
        self.assertEqual(windows[0][0], 0.0)
        for (_, previous_end), (next_start, _) in zip(windows, windows[1:]):
            self.assertAlmostEqual(previous_end - next_start, self.xfade_seconds,
                                   places=6)

    def test_extension_makes_the_chain_match_the_audio(self):
        target = 17.0
        extension = xfade.last_clip_extension(self.durations, self.xfade_seconds,
                                              target)
        self.assertAlmostEqual(extension, 1.3, places=6)
        extended = self.durations[:-1] + [self.durations[-1] + extension]
        self.assertAlmostEqual(
            xfade.chain_length(extended, self.xfade_seconds), target, places=6)

    def test_enable_expression_hides_the_badge_over_a_final_card(self):
        expression = xfade.enable_expression(self.durations, self.xfade_seconds, [3])
        self.assertEqual(expression, "lt(t,10.800)")

    def test_enable_expression_brackets_a_middle_card(self):
        expression = xfade.enable_expression(self.durations, self.xfade_seconds, [1])
        self.assertEqual(expression, "lt(t,5.200)+gte(t,9.000)")


class CaptionTimingTests(unittest.TestCase):
    def test_frames_sum_to_the_rounded_track_length(self):
        boundaries = [round(0.404 * index, 3) for index in range(1, 115)]
        frames = captions.clip_frames(boundaries, 30)
        self.assertEqual(sum(frames), captions.total_frames(boundaries, 30))

    def test_per_clip_rounding_would_have_drifted(self):
        boundaries = [round(0.404 * index, 3) for index in range(1, 115)]
        naive = [round(0.404 * 30)] * len(boundaries)
        self.assertNotEqual(sum(naive), captions.total_frames(boundaries, 30))

    def test_rejects_boundaries_that_do_not_increase(self):
        with self.assertRaises(ValueError):
            captions.clip_frames([1.0, 1.0], 30)

    def test_rejects_a_chunk_too_short_to_render_a_frame(self):
        with self.assertRaises(ValueError):
            captions.clip_frames([1.0, 1.001], 30)

    def test_total_frames_of_an_empty_track_is_zero(self):
        self.assertEqual(captions.total_frames([], 30), 0)

    def test_chunks_break_at_punctuation_and_at_the_word_cap(self):
        words = [(0.0, 0.2, "Un"), (0.2, 0.4, "client"), (0.4, 0.7, "cherche."),
                 (0.7, 0.9, "Une"), (0.9, 1.1, "boutique"), (1.1, 1.3, "a"),
                 (1.3, 1.5, "Ouaga"), (1.5, 1.7, "maintenant")]
        chunks = captions.chunk_words(words, max_words=4)
        self.assertEqual([len(chunk) for chunk in chunks], [3, 4, 1])

    def test_chunking_keeps_every_word(self):
        words = [(index / 10, (index + 1) / 10, f"mot{index}") for index in range(9)]
        chunks = captions.chunk_words(words, max_words=4)
        self.assertEqual([word for chunk in chunks for word in chunk], words)


if __name__ == "__main__":
    unittest.main()
