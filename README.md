<p align="center">
  <img src="https://raw.githubusercontent.com/remarkablegames/psych-101/master/web-presplash.jpg" width="600px" alt="Psych 101">
</p>

# Psych 101

![release](https://img.shields.io/github/v/release/remarkablegames/psych-101)
[![build](https://github.com/remarkablegames/psych-101/actions/workflows/build.yml/badge.svg)](https://github.com/remarkablegames/psych-101/actions/workflows/build.yml)
[![lint](https://github.com/remarkablegames/psych-101/actions/workflows/lint.yml/badge.svg)](https://github.com/remarkablegames/psych-101/actions/workflows/lint.yml)

📖 Play as a student attending Psych 101!

Play the game on:

- [remarkablegames](https://remarkablegames.org/psych-101)
- [itch.io](https://remarkablegames.itch.io/psych-101)

Read the [blog post](https://remarkablegames.org/posts/psych-101/).

## Credits

### Art

- [Homo Studio](https://unsplash.com/photos/a-blackboard-with-a-chalkboard-and-two-pens-on-it-iCyEPaLdPAs)
- [Lia](https://liah0227.itch.io/hoshiko)
- [Uncle Mugen](https://lemmasoft.renai.us/forums/viewtopic.php?t=17302)
- [Noraneko Games](https://noranekogames.itch.io/yumebackground)
- [Withoutpenorpaper](https://witpop.itch.io/sprite-pack-female-pink-hair)
- [renpytom](https://github.com/renpy/renpy/tree/master/the_question/game/images)

### Font

- [Rudiment](https://www.1001fonts.com/rudiment-font.html?text=PSYCH%20101&size=9&fg=ffffff&bg=000000)

### Sound

- [Bell](https://pixabay.com/sound-effects/bel-sekolah-153453/)
- [Kenney Interface Sounds](https://kenney.nl/assets/interface-sounds)
- [Piano Oneshot](https://pixabay.com/sound-effects/low-end-cinematic-piano-oneshots-215805/)

## Ideation

- [Excalidraw](https://excalidraw.com/#json=fZsGhoV7_qbCx1CrTdl5w,RfNwdGpO82BLKXXnkH3MiQ)
- [Game Design Document](https://docs.google.com/document/d/1XKnFt6Ct47ciPOkS1r2irNke3j0LwOY6ioVPo57E0s4/edit)

## Prerequisites

Download [Ren'Py SDK](https://www.renpy.org/latest.html):

```sh
git clone https://github.com/remarkablegames/renpy-sdk.git
```

Symlink `renpy`:

```sh
sudo ln -sf "$(realpath renpy-sdk/renpy.sh)" /usr/local/bin/renpy
```

## Install

Clone the repository to the `Projects Directory`:

```sh
git clone https://github.com/remarkablegames/psych-101.git
cd psych-101
```

## Run

Launch the project:

```sh
renpy .
```

Or open the `Ren'Py Launcher`:

```sh
renpy
```

Press `Shift`+`R` to reload the game.

Clean the cache:

```sh
find game -name "*.rpyc" -delete
```

## Lint

Lint the game:

```sh
renpy game lint
```

## License

[MIT](LICENSE)
