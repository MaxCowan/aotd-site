<script>
export let album;
</script>

<div class="album-info">
    <div class="album-title">{album.name}</div>
    <div class="album-artist">{album.artist}</div>
</div>

<style>
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
