<p align="center">
  <img src="https://raw.githubusercontent.com/remarkablegames/psych-101/master/game/gui/window_icon.png" alt="Psych 101">
</p>

# Psych 101

![release](https://img.shields.io/github/v/release/remarkablegames/psych-101)
[![build](https://github.com/remarkablegames/psych-101/actions/workflows/build.yml/badge.svg)](https://github.com/remarkablegames/psych-101/actions/workflows/build.yml)
[![lint](https://github.com/remarkablegames/psych-101/actions/workflows/lint.yml/badge.svg)](https://github.com/remarkablegames/psych-101/actions/workflows/lint.yml)

📖 Play as a student attending Psych 101 class.

Play the game on:

- [remarkablegames](https://remarkablegames.org/psych-101)

## Credits

- [Withoutpenorpaper](https://witpop.itch.io/sprite-pack-female-pink-hair)
- [Lia](https://liah0227.itch.io/hoshiko)
- [renpytom](https://github.com/renpy/renpy/tree/master/the_question/game/images)

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
