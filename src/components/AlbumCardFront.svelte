<script>
import AlbumImage from './AlbumImage.svelte';
import AlbumInfo from './AlbumInfo.svelte';

export let album;
</script>

<div class="album-card-front">
    <AlbumImage {album} />
    <div class="overlay"></div>
    <AlbumInfo {album} />
</div>

<style>
.album-card-front {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    backface-visibility: hidden;
    border-radius: 0.5rem;
    overflow: hidden;
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

:global(.album-card:hover .overlay) {
    opacity: 1;
}
</style>
