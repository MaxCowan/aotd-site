<script>
import { onMount } from 'svelte';

export let album;
let imageElement;
let isExpanded = false;
let cardElement;
let originalRect;

function getImageUrl() {
    const url = album.artworkUrl
        ? album.artworkUrl.replace('{width}', '400').replace('{height}', '400')
        : "https://upload.wikimedia.org/wikipedia/en/9/9b/Tame_Impala_-_Currents.png?1642732008806";
    return url;
}

onMount(() => {
    setUpLazyLoad();
});

function setUpLazyLoad() {
    if (imageElement) {
        const observer = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    imageElement.src = imageElement.getAttribute('data-src');
                    observer.unobserve(imageElement);
                }
            });
        });

        observer.observe(imageElement);
    }
}

function toggleExpand(event) {
    if (!isExpanded) {
        originalRect = cardElement.getBoundingClientRect();

        cardElement.style.position = 'fixed';
        cardElement.style.top = `${originalRect.top}px`;
        cardElement.style.left = `${originalRect.left}px`;
        cardElement.style.width = `${originalRect.width}px`;
        cardElement.style.height = `${originalRect.height}px`;
        cardElement.style.zIndex = '10';
        cardElement.style.transition = 'all 0.4s ease';

        requestAnimationFrame(() => {
            const viewportWidth = window.innerWidth;
            const viewportHeight = window.innerHeight;

            const translateX = (viewportWidth / 2 - originalRect.left - originalRect.width / 2);
            const translateY = (viewportHeight / 2 - originalRect.top - originalRect.height / 2);

            cardElement.style.transform = `translate(${translateX}px, ${translateY}px) scale(2.5)`; // Adjust scale factor as needed
        });
    } else {
        cardElement.style.transition = 'all 0.4s ease';
        cardElement.style.transform = 'none';

        setTimeout(() => {
            cardElement.style.position = '';
            cardElement.style.top = '';
            cardElement.style.left = '';
            cardElement.style.width = '';
            cardElement.style.height = '';
            cardElement.style.transform = '';
            cardElement.style.zIndex = '';
            cardElement.style.transition = '';
        }, 400);
    }

    isExpanded = !isExpanded;

    if (isExpanded) {
        document.body.style.overflow = 'hidden';
    } else {
        document.body.style.overflow = '';
    }

    event.stopPropagation();
}

function handleClose(event) {
    if (isExpanded) {
        toggleExpand(event);
    }
}

function handleKeyPress(event) {
    if (event.key === 'Enter' || event.key === ' ') {
        toggleExpand(event);
    }
}
</script>

<div bind:this={cardElement} class="album-card-wrapper" on:click={handleClose} role="button" tabindex="0" on:keypress={handleKeyPress}>
    <div class="album-card {isExpanded ? 'expanded' : ''}" on:click={toggleExpand} role="button" tabindex="0" aria-expanded={isExpanded} aria-label={`Toggle expand for ${album.name}`} on:keypress={handleKeyPress}>
        <img bind:this={imageElement} alt={album.name} class="album-image" data-src={getImageUrl()} />
        <div class="overlay"></div>
        <div class="album-info">
            <div class="album-title">{album.name}</div>
            <div class="album-artist">{album.artist}</div>
        </div>
    </div>
</div>

<style>
.album-card-wrapper {
    position: relative;
    display: inline-block;
}

.album-card {
    position: relative;
    width: 100%;
    padding-top: 100%;
    border-radius: 0.5rem;
    overflow: hidden;
    transition: transform 0.4s, box-shadow 0.4s;
    font-family: inherit;
    box-sizing: border-box;
    cursor: pointer;
}

.album-card:hover {
    transform: scale(1.05);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
}

.album-card.expanded {
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5);
    transition: transform 0.4s, box-shadow 0.4s;
}

.album-image {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.5s, filter 0.5s;
}

.album-card:hover .album-image {
    transform: scale(1.05);
    filter: blur(2px);
}

.overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(to top, rgba(0, 0, 0, 0.7), transparent);
    opacity: 0;
    transition: opacity 0.5s;
}

.album-card:hover .overlay {
    opacity: 1;
}

.album-info {
    position: absolute;
    bottom: 1rem;
    left: 1rem;
    right: 1rem;
    text-align: center;
    color: white;
    opacity: 0;
    transform: translateY(1rem);
    transition: opacity 0.5s, transform 0.5s;
    font-family: inherit;
}

.album-card:hover .album-info,
.album-card.expanded .album-info {
    opacity: 1;
    transform: translateY(0);
}

.album-title {
    font-size: 1.35rem;
    font-weight: bold;
}

.album-artist {
    font-size: 1rem;
    margin-top: 0.5rem;
}
</style>
