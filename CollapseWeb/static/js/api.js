window.addEventListener("load", (event) => {
    document.querySelectorAll('#endpoints a').forEach((e) => {
        tippy(e, {
            content: e.getAttribute('aria-details'),
        });
    });
});