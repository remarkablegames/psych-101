<p align="center">
  <img src="https://raw.githubusercontent.com/remarkablegames/psych-101/master/game/gui/window_icon.png" alt="Ren'Py Template">
</p>

# psych-101

📖 Write visual novels with Ren'Py Template.

Play the game on:

- [remarkablegames](https://remarkablegames.org/psych-101)

## Prerequisites

- [Ren'Py SDK](https://www.renpy.org/latest.html)

## Install

Clone the repository to the `Projects Directory`:

```sh
git clone https://github.com/remarkablegames/psych-101.git
cd psych-101
```

Rename the project:

```sh
git grep -l 'Psych 101' | xargs sed -i '' -e 's/Psych 101/Psych 101/g'
```

```sh
git grep -l 'Psych 101' | xargs sed -i '' -e 's/psych-101/psych-101/g'
```

## Run

Change directory to Ren'Py SDK:

```sh
cd path/to/renpy-sdk
```

### CLI

Launch the project:

```sh
./renpy.sh path/to/psych-101
```

### GUI

Open `Ren'Py Launcher`:

```sh
./renpy.sh launcher
```

Click `refresh` and select `psych-101`

Click `Launch Project`

## License

[MIT](LICENSE)
