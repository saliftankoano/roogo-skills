# Script and voice

## Structure (30 to 45 seconds)

1. Hook with the place: "Tanghin, en plein cœur de Waga !"
2. What it is and how big: "Une parcelle de trois cent trente-six mètres carrés est à vendre."
3. Two or three selling facts from the listing (neighborhood, what can be built, nearby landmark, documents).
4. Price: "Prix de vente : quarante millions de francs CFA."
5. Service line: "Avec Rohgo, on s'occupe de tout, de la visite jusqu'au notaire."
6. Contact: "Appelez-nous ou écrivez-nous sur WhatsApp, au soixante-sept, zéro zéro, soixante et un, seize !"

The outro starts on the service line (`endcard_from` in the plan).

A targeted variant reuses the same photos with a different hook, for example
the diaspora: "Vous vivez loin du Bourkina, mais vous voulez bâtir à Waga ?"
It pairs well with fact chips on screen.

## Keep the French simple

Write the way people speak. Avoid formal wording: "on s'occupe de tout", not
"vous avez un seul interlocuteur".

## Emotion comes from punctuation

Cartesia has no emotion tags. These patterns gave Sandrine clear, lively
delivery on the first take:

- an exclamation on the opening line;
- a setup, then a reveal: "Et pas n'importe où : dans le lotissement de mille neuf cent quatre-vingt-cinq.";
- a question answered at once: "Et le grand marché Arb-Yaar ? À seulement cinq cents mètres !"
  (she dropped to a near-whisper on the reveal, which the founder liked).

## Voice

- Narrator: **Sandrine**, Cartesia voice `2435841c-fce7-4fd5-aed1-dc7008eb7d20`,
  model `sonic-3.5`, language `fr`. Credentials as in the sibling packages'
  Cartesia reference: `CARTESIA_API_KEY`, or the macOS Keychain item
  `ai.cartesia.api-key`; never print or commit the key.
- The ElevenLabs narrator (Alimata) was tested on this format and rejected: flat
  delivery, a mispronounced neighborhood, and a year that changed between takes
  of the same text.

## Spoken-text respellings

Captions and on-screen text keep normal spelling; only the text sent to the
voice changes.

| On screen | Write for the voice |
| --- | --- |
| Roogo | Rohgo |
| Burkina (Faso) | Bourkina (Faso) |
| Ouaga, Ouagadougou | Waga |
| Years | in full words: "mille neuf cent quatre-vingt-cinq" |
| Phone numbers | French pairs: "soixante-sept, zéro zéro, soixante et un, seize" |

Sandrine read "Tanghin" correctly as written. Test any new place name.

## Transcribe back before building

Transcribe the voiceover with a large Whisper model (for example
`mlx_whisper --model mlx-community/whisper-large-v3-turbo --word-timestamps True`)
and check every number, year, place name and the phone number. The tiny default
model garbles French and raises false alarms; confirm a suspicious word on a
short slice with a second model. Use the word timestamps to place the cuts,
about 0.4 seconds after the word that starts each new phrase.

If one line is wrong, regenerate or splice the correct line from another take
with the same settings at a natural pause, then transcribe the result again.
