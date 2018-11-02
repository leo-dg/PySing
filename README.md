<h1>PySing</h1>
<em>A pointless procrastination.</em>

## Description
PySing allows Windows users to use Python to play music with a `.txt` of the notes used in the music. Accidentals and note duration can also specified, though these features are not yet robust. To do this, the `winsound` library has been used to play beeps.

## Preqrequisites
To use PySing, you simply need a Windows machine and have Python 3 installed. To make PySing <em>sing</em>, a basic understanding of sheet music is also required.

## Usage
Simply create a `.txt` file in the same directory as PySing, create a `PySinger()` class and use `<PySinger Object>.play(<your .txt>)` to make it sing!

## Input Format
The `.txt` must follow the specified format:
* All notes must be upper-case.
* They must each be separated with commas `,`.
* To use __accidentals__, use `#` or `b` (note: at the moment, please use `G#` over `Ab`, `Bb` over `A#` and `C#` instead of `Db`).
* The __octave__ is specified after the note (and accidental if applicable). Currently implemented is middle octave (4), 5 and 6.
* To specify the __duration__, append after note, accidental and octave:
    * `s` - Semibreve
    * `m` - Minim
    * `C` - Crotchet
    * `c` - Dotted quaver (Don't ask)
    * `Q` - Quaver
    * `q` - Semiquaver

Example: `C#4C` would play a middle C# crotchet.
Note: Currently, the values for all durations are hardcoded.
