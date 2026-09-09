# System

How the published skills work. See [DECISIONS.md](DECISIONS.md) for reasons,
[DOMAIN.md](DOMAIN.md) for vocabulary, [CHANGELOG.md](CHANGELOG.md) for shipped
changes, and [ROADMAP.md](ROADMAP.md) for unfinished commitments.

## What does this repository provide?

It provides reusable agent instructions, not the Roogo app or a hosted rendering
service. Four packages are published: Voxplainer, and the three Roogo ad formats
Appel a proprietaires, Video avantage, and Milestone. Its [human guide](../skills/voxplainer/README.md)
covers installation and examples; [SKILL.md](../skills/voxplainer/SKILL.md) is the
agent contract. References supply conditional detail, metadata supports invocation,
and the audio helper checks technical output. Copying a package does not provision
provider credentials, licensed assets, or a Remotion project.

## How does Voxplainer route a request?

The request chooses a delivery format, a visual grammar, and optional storytelling
treatments independently. The agent reads the matching references before production.
The [human mode comparison](../skills/voxplainer/README.md#understand-the-modes)
is the canonical reader overview; [visual modes](../skills/voxplainer/references/visual-modes.md)
contains the operating criteria. This separation follows the [mode decision](DECISIONS.md).

The contract establishes audience, evidence, scope, budget, voice, and deliverables.
Research and script feed visual beats. Accepted, processed narration supplies
timing; implementation produces previews; encoded review checks the delivered
artifact. Missing evidence or unauthorized paid work stops that part of production,
not permission to invent a result. A concept request ends before rendering.

## How do the three ad formats divide the work?

Each package answers one question the requester already knows the answer to, so the
routing happens before any paid generation. A specific renter or buyer demand that
should make owners call is [Appel a proprietaires](../skills/appel-proprietaires/README.md).
A feature, differentiator, or business-model benefit with no listing photography to
build from is [Video avantage](../skills/video-avantage/README.md). An existing
celebration graphic that needs to move is [Milestone](../skills/milestone/README.md).
Every package states its own exclusions, and each one stops for approval of the
script, the numbers, or the cost path before spending.

The two narrated formats select a narration provider the way Voxplainer does: a
provider-independent workflow covering approval by ear, voice roles, spoken
numbers, and timing, plus one reference per provider that is read only when that
provider is selected. ElevenLabs with the narrator voice Alimata is their
default and Cartesia is the approved alternative, with Sandrine in the narrator
role. Milestone selects no provider, because a milestone post is scored rather
than narrated.

They share standing Roogo video conventions rather than a shared module: the corner
watermark excluded over full-logo spans, captions kept clear of on-screen graphics,
real French titles as filenames, no em dashes or emoji in ad copy, measured rather
than guessed audio, and verification by re-listening and by frame checks rather than
by a successful exit code. Each package carries its own copy of those rules and of
any helper it needs, because a package must remain portable when it is copied alone
into a user skills directory. See the [self-containment decision](DECISIONS.md).

Two hard-won pieces of timing maths are helpers rather than prose, because they are
the ones that were repeatedly got wrong by hand: the real post-transition timeline of
a crossfade chain, and the frame-exact length of a flattened caption track.

## What does validation establish?

Audience/message review is separate from the checks below: technical or visual
success alone does not establish that the film serves its intended viewer.

| Check | Establishes | Does not establish |
| --- | --- | --- |
| Package validator | Metadata, package-local links, reachable references, Python syntax | Quality of a generated film or correctness of factual claims |
| Executable regression suite | Tested helper behavior, validator regressions, whitespace workflow cases | Every possible runtime environment or media input |
| Ad-format timing helpers | Crossfade chain length, card windows, caption frame counts | That a render actually used them, or that the creative works |
| Audio quality helper | Measured technical audio checks against configured targets | Natural speech, intelligibility in context, or artistic acceptance |
| Behavioral fixtures and encoded review | Human/agent evaluation of production behavior and actual output | Automatic proof merely because CI is green |

Run the commands in the [repository README](../README.md#validation). CI validates
pull requests and pushes to main, including changed-line whitespace. The
[review record](voxplainer-review.md) and [behavioral fixtures](../tests/fixtures/voxplainer-review.md)
retain the distinction between automated tests and manual judgment.

## Where do production work and project memory live?

Media projects remain outside this repository. Source assets retain provenance;
modified working copies and fresh UI captures are identified separately. Secrets
stay in private configuration, never in public prompts, manifests, or commits.
See the [public-safety decision](DECISIONS.md).

The five logbook documents record reasons, mechanisms, shipped changes, language,
and unfinished commitments separately. AGENTS.md makes maintenance part of meaningful
work. A documentation PR is unfinished until merged; it does not enter the shipped
changelog merely because its files exist on a branch.

## Audience and message planning

How does a feature inventory become a useful campaign? Voxplainer's
[planning reference](../skills/voxplainer/references/audience-and-messaging.md)
organizes films by primary viewer, situation, communication purpose, evidence,
takeaway, and ending before scripting. The audience/message brief lives in the
production contract; campaigns add a proposed film map rather than a competing
contract. Format and visual grammar are selected independently.

Material audience ambiguity is resolved before script lock or paid narration.
Existing explicit approval can satisfy that checkpoint. Proposed splits, merges,
or deferrals do not change a commissioned lineup until accepted. Narrow repairs
preserve approved messages and surface unrelated strategy findings separately.

Message review checks opening relevance, language, scene necessity, role handoffs,
and the ending. It records what was actually inspected; an agent review does not
claim measured viewer comprehension or retention. The [decision](DECISIONS.md)
explains why this layer precedes production. Installation and campaign adoption
remain separately tracked in [ROADMAP.md](ROADMAP.md).
