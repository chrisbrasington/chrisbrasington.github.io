<h1 align="center">Startpage</h1>

<p align="center">A minimalist startpage designed for quick access to your favorite websites</p>

![Startpage Screenshot](../resources/startpage-2024-10-08.gif)

This is my personalized startpage, designed to be my browser homepage. It includes quick links to my favorite websites, a search bar, and a minimalist layout.

## Repository Structure

- **_build**: Build script and page template. Not published by Jekyll.
- **scripts**: The scripts used in the startpage.
- **static**: CSS, font, icons and hero images.
- **index.html** / **sw.js**: Generated. Do not edit by hand.

## Building

`index.html` is compiled from the sources so the page is a single request with
nothing left to fetch or lay out after first paint. The stylesheet, scripts and
settings icons are inlined, and the link list in `scripts/links.js` is rendered
to static markup instead of being built by JavaScript on load.

Edit `scripts/links.js`, `static/styles/style.css` or `_build/index.template.html`,
then from this directory run:

```sh
python3 _build/build.py
```

That rewrites `index.html` and `sw.js`, and commits go up as usual.

Adding or removing a file in `static/images/` is enough to change the hero image
rotation - the build picks the directory up automatically.

`sw.js` is a service worker that precaches the font and every hero image, so
repeat visits paint immediately. The document itself is fetched network-first,
so a rebuild is never served stale.

## Keyboard Shortcuts

The following keyboard shortcuts are available on the search page:

- **Escape**: Hide the settings panel.
- **Alt + Space**: Focus on the search input field.
- **Enter**: Execute the search.
- **Ctrl + C**: Clear the search input field.

## Contribute

If you want to make any change, follow these steps:

1. Open an issue to discuss the changes.
2. Fork this repository.
3. Create a new branch for your contribution: `git checkout -b your-branch-name`.
4. Make your changes.
5. Commit your changes, for example: `git commit -m 'fix: incorrect svg path'`.
6. Push your changes to your forked repository: `git push origin your-branch-name`.
7. Open a Pull Request in this repository and reference the original issue.

## License

This project is licensed under the GPL-3.0 License. See the [LICENSE](LICENSE) file for more details.

## Credits

- Inspired from [Fxzii Startpage](https://github.com/Fxzzi/startpage).
