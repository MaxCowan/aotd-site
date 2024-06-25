<script>
export let album;
let imageElement;

function getImageUrl() {
    const url = album.artworkUrl
        ? album.artworkUrl.replace('{width}', '400').replace('{height}', '400')
        : "https://upload.wikimedia.org/wikipedia/en/9/9b/Tame_Impala_-_Currents.png?1642732008806";
    return url;
}
</script>

<img bind:this={imageElement} alt={album.name} class="album-image" src={getImageUrl()} />

<style>
.album-image {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.5s, filter 0.5s;
}

:global(.album-card:hover .album-image) {
    transform: scale(1.05);
    filter: blur(2px);
}
</style>
