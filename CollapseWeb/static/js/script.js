document.addEventListener("DOMContentLoaded", function(){
    setTimeout(() => {
        animateCards()
    }, 400);
});

function animateCards() {
    var index = 0

    for (const element of document.querySelectorAll('div.card')) {
        const timeout = 20 * (index++)

        setTimeout(() => {
            element.style.filter = 'blur(0px)'
        }, timeout)
    }
}

function getClientsId() {
    var clients = []
    for (const element of document.querySelectorAll('div.card')) {
        if (element.id.startsWith('client-')) clients.push([element.id, element])
    }
    return clients
}

function getConfigs() {
    var configs = []
    for (const element of document.querySelectorAll('div.card')) {
        if (element.id.startsWith('config-')) configs.push([element.id, element])
    }
    return configs
}

function highlightClient(event, clientId) {
    event.preventDefault();
    const target = document.querySelector(`#client-${clientId}`);
    if (target) {
        target.classList.add('glow');
        target.scrollIntoView({ behavior: 'smooth', block: 'center' });
        setTimeout(() => {
            target.classList.remove('glow');
        }, 1500);
    }
}