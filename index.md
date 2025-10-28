---
title: Christopher Brasington
layout: default
csharp_start: 2010
python_start: 2010
javascript_start: 2008
linux_start: 2004
obsidian_start: 2023
blazor_start: 2019
umbraco_start: 2021
kotlin_start: 2024
arduino_start: 2015
azure_start: 2018
---

# Hi, I'm [{{ site.name }}](https://www.linkedin.com/in/brasington/)

I am a software engineer at a wonderful [science museum](https://www.dmns.org/). This is a site for projects and writings.

<div style="display:flex; flex-wrap:wrap; gap:20px; justify-content:space-between;">

  <!-- Column 1: Skills Chart -->
  <div style="flex:1 1 300px; min-width:300px; text-align:center;">
    <h3>Tech Experience</h3>
    <canvas id="experienceChart" style="width:100%; height:300px;"></canvas>
  </div>

  <!-- Column 2: Writings -->
  <div style="flex:1 1 300px; min-width:300px;">
    <h3>🖊️ Writings</h3>
    <ul>
      <li><a href="./mods/">Morrowind Modlist</a></li>
      <li><a href="./gaming/ten">10 Games to Get to Know Me</a></li>
      <li><a href="./morrowind/">Tales of Greater Morrowind</a></li>
      <li><a href="./attention/">Tips to reducing psychological “hooks” of the modern internet age</a></li>
    </ul>
    
    <h3>🎮 NextFest Reviews</h3>
    <div style="font-size:16px; line-height:1.5;">
      <strong>2025:</strong> <a href="https://github.com/chrisbrasington/nextfest/blob/main/2025_October.md" target="_blank">October</a> · <a href="https://github.com/chrisbrasington/nextfest/blob/main/2025_June.md" target="_blank">June</a> · <a href="https://github.com/chrisbrasington/nextfest/blob/main/2025_Feb.md" target="_blank">February</a><br>
      <strong>2024:</strong> <a href="https://github.com/chrisbrasington/nextfest/blob/main/2024_June.md" target="_blank">June</a> · <a href="https://github.com/chrisbrasington/nextfest/blob/main/2024_Feb.md" target="_blank">February</a><br>
      <strong>2023:</strong> <a href="https://github.com/chrisbrasington/nextfest/blob/main/2023.md" target="_blank">February</a>
    </div>
  </div>

<!-- Column 3: Hobbies -->
<div style="flex:1 1 300px; min-width:300px; text-align:center;">
  <h3>🛹 Hobbies</h3>

  <table class="scale3-hover" style="margin:0 auto; border-collapse:collapse; border-spacing:12px; border:none;">
    <tr>
      <td style="text-align:center; border:none;">
        <strong>Skateboarding</strong><br>
        <img src="./resources/skate2.jpg" width="150" class="img-row">
      </td>
      <td style="text-align:center; border:none;">
        <strong>Gaming</strong><br>
        <img src="./resources/handheld3.jpg" width="150" class="img-row">
      </td>
    </tr>
    <tr>
      <td style="text-align:center; border:none;">
        <strong>Reading</strong><br>
        <img src="./resources/books1.jpg" width="150" class="img-row">
      </td>
      <td style="text-align:center; border:none;">
        <strong>Camping</strong><br>
        <img src="./resources/camper.jpg" width="150" class="img-row">
      </td>
    </tr>
  </table>
</div>

</div>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
const ctx = document.getElementById('experienceChart').getContext('2d');

const currentYear = {{ site.time | date: "%Y" }};
const experienceData = [
    currentYear - {{ page.linux_start }},
    currentYear - {{ page.javascript_start }},
    currentYear - {{ page.csharp_start }},
    currentYear - {{ page.python_start }},
    currentYear - {{ page.arduino_start }},
    currentYear - {{ page.azure_start }},
    currentYear - {{ page.blazor_start }},
    currentYear - {{ page.umbraco_start }},
    currentYear - {{ page.obsidian_start }},
    currentYear - {{ page.kotlin_start }}
];

const data = {
    labels: ["Linux", "Javascript", "C#", "Python", "Arduino", "Azure CI/CD", "Blazor/MAUI", "Umbraco", "Obsidian", "Kotlin"],
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


## </> Professional Projects

| Site | | |
|----------|------------|------------|
| [dmns.org](https://www.dmns.org/) | Denver Museum of Nature & Science | ![](./resources/dmns1.png) ![](./resources/dmns2.png) |
| dmns curiosity cruiser | roving science | ![](./resources/dmnscruiser1.jpg)
| dmns kiosk | Payment kiosks | ![](./resources/dmnskiosk1.jpg)
| dmns member app | | ![](./resources/dmnsapp1.jpg)
| mitek blackpoint | CAD automation and materials manager | ![](./resources/blackpoint.webp)
| hohmann & barnard | submittal package generation and estimation | ![](./resources/hb.jpg)

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
| [image-organizer](https://github.com/chrisbrasington/image-organizer) | CLI tool for sorting images into folders | ![](./resources/imagesort.png)
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
| [hackathon-led](https://github.com/chrisbrasington/hackathon-led) | | ![](./resources/hackathon.jpg)
| [obsidian - light-novel-markdown-creator](https://github.com/chrisbrasington/light-novel-markdown-creator) | Use [obsidian-book-search-plugin](https://github.com/anpigon/obsidian-book-search-plugin) which added manga support
| [quicktask](https://github.com/chrisbrasington/quicktask) | Creates quick task markdown for obsidian | Abandoned for google keep and/or manual obsidian entry
| [jameswebb-downloader](https://github.com/chrisbrasington/jameswebb-downloader)
| [audiobook parser/synchronization app](https://github.com/chrisbrasington/audiobook-sync-app) | uses author/title | ![](./resources/audobooksync.png)
| [discord-anything-status](https://github.com/chrisbrasington/discord-anything-status)
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