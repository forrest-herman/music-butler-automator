# music-butler-automator
 A Python web automator script to auto-add my Music Butler feed to my Apple Music library.

## Ideas for features and improvements
- [ ] Check if music already exists
  - Maybe parse the music.apple.com website to check?
  - Don't import duplicates
- [ ] Only import music released since the last import
  - A method to achieve this might be to save the current date to a file when the script is run, and then cross-check the release date of the album to find albums that are newer.