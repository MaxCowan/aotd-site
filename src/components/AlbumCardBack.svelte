<script>
export let album;
</script>

<div class="album-card-back">
    <div class="back-content">
        <h3>{album.name}</h3>
        <p>Sample text on the backside</p>
    </div>
</div>

<style>
.album-card-back {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    transform: rotateY(180deg);
    background-color: black;
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    backface-visibility: hidden;
    border-radius: 0.5rem;
    overflow: hidden;
}

.back-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
}
</style>
