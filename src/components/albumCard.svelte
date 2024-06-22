<script>
import { onMount } from 'svelte';

export let album;
let imageElement;

function getImageUrl() {
    const url = album.artworkUrl
        ? album.artworkUrl.replace('{width}', '600').replace('{height}', '600')
        : "https://upload.wikimedia.org/wikipedia/en/9/9b/Tame_Impala_-_Currents.png?1642732008806";
    console.log(`Generated image URL for album "${album.name}":`, url);
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
                    console.log('Image src set for:', album.name);
                    observer.unobserve(imageElement);
                }
            });
        });

        observer.observe(imageElement);
        console.log('Observer setup for:', album.name, 'with data-src:', imageElement.getAttribute('data-src'));
    }
}
</script>

<div class="album-card">
    <img bind:this={imageElement} alt={album.name} class="album-image" data-src={getImageUrl()} />
    <div class="overlay"></div>
    <div class="album-info">
        <div class="album-title">{album.name}</div>
        <div class="album-artist">{album.artist}</div>
    </div>
</div>

<style>
.album-card {
    position: relative;
    width: 100%;
    padding-top: 100%;
    border-radius: 0.5rem;
    overflow: hidden;
    transition: transform 0.4s, box-shadow 0.4s;
    font-family: inherit;
    box-sizing: border-box;
}

.album-card:hover {
    transform: scale(1.05);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
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

.album-card:hover .album-info {
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
