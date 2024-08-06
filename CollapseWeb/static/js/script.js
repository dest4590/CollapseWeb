document.addEventListener("DOMContentLoaded", () => {
    animateCards();
});

async function animateCards() {
    const cards = document.querySelectorAll('div.card');

    await Promise.all(
        Array.from(cards).map((card, index) => {
            return new Promise((resolve) => {
                setTimeout(() => {
                    card.style.filter = 'blur(0px)';
                    resolve();
                }, 20 * index);
            });
        })
    );
}

function getItemsById(prefix) {
    return Array.from(document.querySelectorAll(div.card[id ^= "${prefix}"])).map(
        (element) => [element.id, element]
    );
}

async function highlightClient(event, clientId) {
    event.preventDefault();
    const target = document.getElementById(`client-${clientId}`);
    if (target) {
        target.classList.add('glow');
        target.scrollIntoView({ behavior: 'smooth', block: 'center' });
        await new Promise((resolve) => setTimeout(resolve, 1500));
        target.classList.remove('glow');
    }
}
