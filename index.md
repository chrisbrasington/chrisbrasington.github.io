---
title: Christopher Brasington
layout: default
csharp_start: 2010
python_start: 2010
linux_start: 2004
obsidian_start: 2023
blazor_start: 2019
umbraco_start: 2021
kotlin_start: 2024
arduino_start: 2015
---

# Hi, I'm [{{ site.name }}](https://www.linkedin.com/in/brasington/)

I am a software engineer at a science museum. This is a site for projects and writings.

## 💻 Skills

<!-- | Tech                     | Experience |
|--------------------------|------------|
| Linux                    | {{ site.time | date: "%Y" | minus: page.linux_start }} years |
| C#                       | {{ site.time | date: "%Y" | minus: page.csharp_start }} years |
| Python                   | {{ site.time | date: "%Y" | minus: page.python_start }} years |
| Arduino                  | {{ site.time | date: "%Y" | minus: page.arduino_start }} years |
| Blazor/MAUI              | {{ site.time | date: "%Y" | minus: page.blazor_start }} years |
| Umbraco                  | {{ site.time | date: "%Y" | minus: page.umbraco_start }} years |
| [Obsidian.md](https://obsidian.md/) | {{ site.time | date: "%Y" | minus: page.obsidian_start }} years |
| Kotlin                   | {{ site.time | date: "%Y" | minus: page.kotlin_start }} years | -->

# Tech Experience Chart

<canvas id="experienceChart" style="width: 50%; height: 50%;"></canvas>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
const ctx = document.getElementById('experienceChart').getContext('2d');

// Dynamically calculate years from front matter
const currentYear = {{ site.time | date: "%Y" }};
const experienceData = [
    currentYear - {{ page.linux_start }},
    currentYear - {{ page.csharp_start }},
    currentYear - {{ page.python_start }},
    currentYear - {{ page.arduino_start }},
    currentYear - {{ page.blazor_start }},
    currentYear - {{ page.umbraco_start }},
    currentYear - {{ page.obsidian_start }},
    currentYear - {{ page.kotlin_start }}
];

const data = {
    labels: ["Linux", "C#", "Python", "Arduino", "Blazor/MAUI", "Umbraco", "Obsidian", "Kotlin"],
    datasets: [{
        label: 'Years of Experience',
        data: experienceData,
        backgroundColor: 'rgba(54, 162, 235, 0.6)',
        borderColor: 'rgba(54, 162, 235, 1)',
        borderWidth: 1
    }]
};

new Chart(ctx, {
    type: 'bar',
    data: data,
    options: {
        indexAxis: 'y',  // Horizontal bars
        scales: {
            x: {
                beginAtZero: true,
                stepSize: 1
            }
        }
    }
});
</script>

## 🖊️ Writings
[Tips to reducing pychological “hooks” of the modern internet age](./attention/)

## </> Professional Projects

| Site | | |
|----------|------------|------------|
| [dmns.org](https://www.dmns.org/) | Denver Museum of Nature & Science | ![](./resources/dmns1.png) ![](./resources/dmns2.png) |
| dmns kiosk | Payment kiosks | ![](./resources/dmnskiosk1.jpg)
| dmns curiosity cruiser | roving science | ![](./resources/dmnscruiser1.jpg)
| dmns member app | | ![](./resources/dmnsapp1.jpg)
| mitek blackpoint | CAD automation and materials manager | ![](./resources/blackpoint.webp)

## </> Projects

| Personal | | |
|----------|------------|------------|
| [github.io](https://github.com/chrisbrasington/chrisbrasington.github.io) | [site](https://chrisbrasington.github.io/), [homepage](https://chrisbrasington.github.io/home/), and [articles](https://chrisbrasington.github.io/attention/) | ![](./resources/site.png) |
| Launcher (WIP) | Minimalist launcher / media player | ![](./resources/launcher1.png) ![](./resources/launcher2.png) ![](./resources/launcher3.png) |

| Manga | | |
|----------|------------|------------|
| [onepiece_dl](https://github.com/chrisbrasington/onepiece_dl) | Download latest one-piece chapter | ![](./resources/onepiece.png)|
| [manga-downloader-sync](https://github.com/chrisbrasington/manga-downloader-sync) | Download from mangadex / docker support |  <img src="./resources/manga1.png" width="40%">|
| [lightnovel-epub-creator](https://github.com/chrisbrasington/lightnovel-epub-creator) | Download from url - create epub|

| Utility | | |
|----------|------------|------------|
| [epub_search](https://github.com/chrisbrasington/epub_search) | Find words within books | Search for multiple words in EPUB files in a directory, and display contextual paragraph and location. 
| [Obsidian Image Cache Script](https://github.com/chrisbrasington/obsidian-image-cache) | Scan markdown files for image metadata | Download images to .cache for performance and/or long-term survivability 
| [MangaDex Covers Downloader](https://github.com/chrisbrasington/mangadex-covers) | Generate cover images from MangaDex URL | ![](./resources/dandadan.png) | 
| [kobo-to-obsidian-import](https://github.com/chrisbrasington/kobo-to-obsidian-import) | export as markdown | ![](./resources/kobo_markdown.png)
| [book-scanner](https://github.com/chrisbrasington/book-scanner) | Use a barcode scanner, scans into database/csv | ![](./resources/bookscan.png)
| [image-organizer] | CLI tool for sorting images into folders | ![](./resources/imagesort.png)
| [obsidian-tagger](https://github.com/chrisbrasington/obsidian-tagger) | Bulk apply tags to a folder of markdown files
| [discord-canary-updater](https://github.com/chrisbrasington/discord-canary-updater) | Automates update of .deb discord canary
| [obsidian-sort](https://github.com/chrisbrasington/obsidian-sort) | manages sort metadata value for folder of mardown files
| [obsidian cover url updater](https://github.com/chrisbrasington/markdown-coverimage-fixer) | If images are not found online, allow user to update | ![](./resources/coverurlfixer.png)
| [garmin data parse to obsidian chart](https://github.com/chrisbrasington/garmin) | Converts garmin sleep or activity data into dataview
| [obsidian search](https://github.com/chrisbrasington/obsidiansearch) | commandline utility for search markdown files | ![](./resources/obsearch.png)


| Security | | |
|----------|------------|------------|
| [ssh-attempt log analyzer](https://github.com/chrisbrasington/ssh-attempts) | script analyzes SSH login logs (auth.log*)

| Gaming | | |
|----------|------------|------------|
| [morrowind-mod-tracker](https://github.com/chrisbrasington/morrowind-mod-tracker) | Reads mod directory, produces markdown | ![](./resources/morrowind.png)
| [bestset](https://github.com/chrisbrasington/bestset) | Create "best set" of ROMS | Search multiple folders and copy cleaned file-names to a directory per game system folder (PS1, GBA, etc) 
| [launch modifier](https://github.com/chrisbrasington/morrowind_launcher) | Launch openMW or openRTC (rollercoaster tycoon) | Compatible to steam game time recording
| [3DS save sync](https://github.com/chrisbrasington/3ds-save-sync) | Sync checkpoint saves between two 3DSes | ![](./resources/3dssavesync.png)
| [psp-psx save sync and converter](https://github.com/chrisbrasington/psp_psx_save_sync) | Supports 2 different save types and movement - useful for PSP hardware and emulators | ![](./resources/pspsync1.png)
| [steam deck image pull](https://github.com/chrisbrasington/steamdeck-screenshot-pull) | Pull steamdeck screenshot folder to PC
| [leap motion swipe detectoin](https://github.com/chrisbrasington/leap_motion) | Detects swipe motion on leap motion device
| [switch capture script](https://github.com/chrisbrasington/nintendoswitch-card-capture) | Nintendo Switch using mpv, while routing the audio using PulseAudio loopback | ![](./resources/switch1.png)
| [steam icon fix](https://github.com/chrisbrasington/steam-icon-fix-linux) | parses icon-cache | ![](./resources/steamiconfix1.png)
| [disgaea-macro-generator (windows only)](https://github.com/chrisbrasington/disgaea-macro-generator) | uses autohotkey | ![](./resources/disgaea.gif)
| [final fantasy PR auto-battler (windows only)](https://github.com/chrisbrasington/final-fantasy-auto-auto-battle) | uses autohotkey, has battle detection | ![](./resources/ffauto1.jpg)

| Fun | | |
|----------|------------|------------|
| [denver-skyimage](https://github.com/chrisbrasington/denver-skyimage) | timelapse | ![](./resources/skyimage.jpg)
| [washer-dryer-pushover-status-monitor-ESP8266](github.com/chrisbrasington/washer-dryer-pushover-status-monitor-ESP8266) | Get a text when washer/dryer done shaking

| Discord BOT  | | |
|----------|------------|------------|
| [onepiece_dl](https://github.com/chrisbrasington/onepiece_dl) | Download latest one-piece chapter | Bot commands for latest or by chapter number / url|
| [screenshot-bot](https://github.com/chrisbrasington/screenshot-bot) | Steam support | ![](./resources/screenshotbot1.png) ![](./resources/screenshotbot2.png)
| [discord game turn bot](https://github.com/chrisbrasington/discord-game-turn-bot) | Used to manage a game of telephone | ![](./resources/gamebot1.png) ![](./resources/gamebot2.png)
| [discord event bot](https://github.com/chrisbrasington/discord-deep-rock-event-bot) | Obsolete, but does respond to "rock and stone"
| [sonic bot](https://github.com/chrisbrasington/sonic-bot) | Uses [VADER](https://vadersentiment.readthedocs.io/en/latest/) sentiment to response positive/negative/neutral

| DotFiles (sway) | | |
|----------|------------|------------|
| [dotfiles](https://github.com/chrisbrasington/dotfiles) | sway | ![](./resources/dotfiles.png)

| OLD music theory | | |
|----------|------------|------------|
| [ruby music theory](https://github.com/chrisbrasington/ruby-music-theory)
| [ardunino midi LED](https://github.com/chrisbrasington/arduino-piano)
| [euterpea-studies](https://github.com/chrisbrasington/Euterpea-Study)

| Obsolete / Unmaintained  OLD | | |
|----------|------------|------------|
| [obsidian - light-novel-markdown-creator](https://github.com/chrisbrasington/light-novel-markdown-creator) | Use [obsidian-book-search-plugin](https://github.com/anpigon/obsidian-book-search-plugin) which added manga support
| [quicktask](https://github.com/chrisbrasington/quicktask) | Creates quick task markdown for obsidian | Abandoned for google keep and/or manual obsidian entry
| [jameswebb-downloader](https://github.com/chrisbrasington/jameswebb-downloader)
| [audiobook parser/synchronization app](https://github.com/chrisbrasington/audiobook-sync-app) | uses author/title | ![](./resources/audobooksync.png)
| [discord-anything-status](https://github.com/chrisbrasington/discord-anything-status)
| [hackathon-led](https://github.com/chrisbrasington/hackathon-led)
| [comic books weekly RSS](https://github.com/chrisbrasington/comic-books-weekly)
| [gnucash savings report](https://github.com/chrisbrasington/gnucash-savings)
| [gnucash budge report](https://github.com/chrisbrasington/gnucash-budget)
| [gnucash from text message](https://github.com/chrisbrasington/text-messaging-to-gnucash)
| [speedtest randomizer runs](https://github.com/chrisbrasington/speedtest-randomizer)
| [RTD Transit Feed parser](https://github.com/chrisbrasington/rtd)
| [tunefind playlist generator](https://github.com/chrisbrasington/tunefind-playlist-generator)
| [lastfm googlemusic playlist generator](https://github.com/chrisbrasington/lastfm-googlemusic-playlist-generator)
| [crawl stone soup stats](https://github.com/chrisbrasington/crawl-stats) | go play [dungeon crawl stone soup](https://crawl.develz.org/)
| [guildwars javascript api wrapper](https://github.com/chrisbrasington/guildwars2-javascript-api-wrapper)
| [LBN511-hack](https://github.com/chrisbrasington/LBN511-hack)
| [lastfm website](https://github.com/chrisbrasington/lastfm-website)