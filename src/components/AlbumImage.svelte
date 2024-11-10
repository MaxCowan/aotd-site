<script>
import { onMount, onDestroy } from 'svelte';
export let album;
let imageElement;

function getImageUrl() {
    const url = album.artworkUrl
        ? album.artworkUrl.replace('{width}', '400').replace('{height}', '400')
        : "https://upload.wikimedia.org/wikipedia/en/9/9b/Tame_Impala_-_Currents.png?1642732008806";
    return url;
}

let loaded = false;
let observer;

function onLoad() {
    loaded = true;
    if (observer) {
        observer.disconnect();
    }
}

onMount(() => {
    if ('IntersectionObserver' in window) {
        observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    imageElement.src = getImageUrl();
                    observer.unobserve(imageElement);
                }
            });
        });
        observer.observe(imageElement);
    } else {
        // Fallback for browsers without IntersectionObserver support
        imageElement.src = getImageUrl();
    }
});

onDestroy(() => {
    if (observer) {
        observer.disconnect();
    }
});
</script>

<img 
    bind:this={imageElement} 
    alt={album.name} 
    class="album-image {loaded ? 'loaded' : ''}"
    data-src={getImageUrl()} 
    loading="lazy"
    decoding="async"
    width="400"
    height="400"
    on:load={onLoad}
/>

<style>
.album-image {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.5s, filter 0.5s, opacity 0.5s;
    opacity: 0;
}

/* Fade in image once loaded */
.album-image.loaded {
    opacity: 1;
}

/* Apply hover effects only when the card is not expanded */
:global(.album-card:not(.expanded):hover .album-image) {
    transform: scale(1.05);
    filter: blur(2px);
}

/* Ensure no blur or transform when the card is expanded */
:global(.album-card.expanded .album-image) {
    transform: none;
    filter: none;
}
</style>
