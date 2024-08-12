var colorschemeList = {
    "dracula": {
        '--color-foreground-1': '#F8F8F2',
        '--color-foreground-2': '#B9BBCB',
        '--color-background-1': '#44475A',
        '--color-background-2': '#282A36',
        '--color-background-3': '#1F1F28',
        '--color-accent-1': '#BD93F9',
        '--color-accent-2': '#BD93F933',
        '--color-shadow-1': '#1D1D26',
        '--color-shadow-2': '#46495C',
    },
    "edge": {
        '--color-foreground-1': '#F8F8F8',
        '--color-foreground-2': '#B9B9B9',
        '--color-background-1': '#6B6B6B',
        '--color-background-2': '#3B3B3B',
        '--color-background-3': '#2B2B2B',
        '--color-accent-1': '#C9C9C9',
        '--color-accent-2': '#9B9B9B33',
        '--color-shadow-1': '#2B2B2B',
        '--color-shadow-2': '#B9B9B9',
    }
};

function changeColorScheme() {
    var root = document.documentElement;
    var colorscheme = document.getElementById("colorscheme-selector");
    var selectedScheme = colorschemeList[colorscheme.value];

    for (var property in selectedScheme) {
        root.style.setProperty(property, selectedScheme[property]);
    }

    localStorage.setItem("selectedColorscheme", colorscheme.value);
}

function loadSavedColorscheme() {
    var savedColorscheme = localStorage.getItem("selectedColorscheme");
    var colorscheme = document.getElementById("colorscheme-selector");

    if (savedColorscheme) {
        colorscheme.value = savedColorscheme;
    } else {
        colorscheme.value = "dracula";
    }

    changeColorScheme();
}

loadSavedColorscheme();
