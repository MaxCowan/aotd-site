<script>
export let album;
</script>

<div class="album-card">
    <img src="https://upload.wikimedia.org/wikipedia/en/9/9b/Tame_Impala_-_Currents.png?1642732008806" alt={album.name} class="album-image"/>
    <div class="overlay"></div>
    <div class="album-title">{album.name}</div>
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

.album-title {
    position: absolute;
    bottom: 1rem;
    left: 1rem;
    right: 1rem;
    color: white;
    font-size: 1.25rem;
    font-weight: bold;
    text-align: center;
    opacity: 0;
    transform: translateY(1rem);
    transition: opacity 0.5s, transform 0.5s;
    font-family: inherit;
}

.album-card:hover .album-title {
    opacity: 1;
    transform: translateY(0);
}
</style>
