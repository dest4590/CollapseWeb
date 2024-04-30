function animateCards() {
    var index = 0

    for (const element of document.querySelectorAll('div.card')) {
        const timeout = 30 * (index++)

        setTimeout(() => {
            element.style.marginTop = '1rem'
            element.style.filter = 'blur(0px)'
        }, timeout)
    }
}

function animateHeader() {
    var element = document.getElementById('hl-text')

    element.style.opacity = 1
}

function returnJSON(url, callback) {
    var xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function () {
        if (this.readyState === 4) {
            if (this.status === 200) {
                var jsonData = JSON.parse(this.responseText);
                callback(jsonData);
            } else {
                callback(false)
            }
        }
    };

    xhttp.open("GET", url);
    xhttp.send();

}

function fadeOut() {
    document.body.style.filter = 'blur(0px)'
}

function showButtons() {
    var hl_text = document.getElementById('hl-text')
    hl_text.style.marginLeft = '10rem'
    hl_text.style.marginTop = '5rem'

    if (hl_text.getAttribute('can_hide') == 'false') {
        document.getElementById('hl-text').setAttribute('onclick', '')
        
        setTimeout(() => {
            document.getElementById('header-buttons').style.opacity = 1
            
            setTimeout(() => {
                hl_text.setAttribute('can_hide', true)
                document.getElementById('hl-text').setAttribute('onclick', 'showButtons()')
            }, 2000);
        }, 700);
    }

    if (hl_text.getAttribute('can_hide') == 'true') {
        document.getElementById('hl-text').setAttribute('onclick', '')
        
        document.getElementById('header-buttons').style.opacity = 0
        
        setTimeout(() => {
            hl_text.style.marginLeft = '0'
            hl_text.style.marginTop = '3rem'
            setTimeout(() => {
                hl_text.setAttribute('can_hide', false)
                document.getElementById('hl-text').setAttribute('onclick', 'showButtons()')
            }, 2000);
        }, 700);
    }
}

window.onload = () => {
    const lenis = new Lenis({
        duration: 1,
        easing: (x) => x === 1 ? 1 : 1 - Math.pow(2, -10 * x)
    })

    function raf(time) {
        lenis.raf(time)
        requestAnimationFrame(raf)
    }

    requestAnimationFrame(raf)

    setTimeout(() => {
        document.getElementById('hl-text').style.animation = '3s ease-in-out infinite alternate pulse, headerWiggle 2s var(--eio2)'

        animateHeader()
        fadeOut()

        setTimeout(() => {
            // set onclick attribute
            document.getElementById('hl-text').setAttribute('onclick', 'showButtons()')
        }, 2100);

        animateCards()
    }, 500);
}