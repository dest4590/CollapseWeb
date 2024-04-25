function animateCards() {
    var index = 0

    for (const element of document.querySelectorAll('div.card')) {
        const timeout = 80 * (index++)

        setTimeout(() => {
            element.style.marginTop = '3rem'
            element.style.filter = 'blur(0px)'
        }, timeout)
    }
}

function animateHeader(normal) {
    var index = 0

    for (const element of document.querySelectorAll('div.header > h1')) {
        const timeout = 80 * (index++)

        setTimeout(() => {
            if (!normal) {
                element.style.marginLeft = `${timeout / 80}rem`                
            }
            else {
                element.style.marginLeft = `0rem` 
            }
            element.style.opacity = 1
        }, timeout)
    }
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

window.onload = () => {
    const lenis = new Lenis()

    function raf(time) {
        lenis.raf(time)
        requestAnimationFrame(raf)
    }

    requestAnimationFrame(raf)

    setTimeout(() => {
        animateHeader(false)
        
        setTimeout(() => {
            animateHeader(true)
        }, 2000);

        animateCards()
    }, 500);
}