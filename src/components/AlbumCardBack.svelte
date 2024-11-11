<script>
    export let album;
    export let isExpanded = false;

    let backContentElement;

    $: if (isExpanded) {
        backContentElement.scrollTo(0, 0);
    }
</script>

<div class="album-card-back {isExpanded ? 'expanded' : ''}">
    <div class="back-content" bind:this={backContentElement}>
        <h3>{album.name}</h3>
        <div class="album-details">
            {#each Object.entries(album) as [key, value]}
                <div class="detail">
                    <span class="key">{key}:</span>
                    <span class="value">{value}</span>
                </div>
            {/each}
        </div>
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
    padding: 1rem;
    box-sizing: border-box;
    z-index: 2;
    transition: transform 0.4s ease, font-size 0.4s ease;
}

.album-card-front {
    z-index: 1;
}

.back-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    text-align: center;
    width: 100%;
    height: 100%;
    overflow-y: auto;
    pointer-events: none;
    will-change: opacity, transform;
    transform: translateZ(0);
}

.expanded .back-content {
    pointer-events: auto;
}

h3 {
    margin: 0;
    padding: 1rem 0;
    font-size: 1.5rem;
    transition: font-size 0.4s ease;
}

.album-details {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    margin-top: 1rem;
    font-size: 1.0rem;
    text-align: left;
    width: 100%;
    padding: 0 0.5rem;
    box-sizing: border-box;
    transition: font-size 0.4s ease;
}

.detail {
    display: flex;
    flex-direction: column;
    gap: 0.25rem;
}

.key {
    font-weight: bold;
    white-space: nowrap;
}

.value {
    word-wrap: break-word;
    white-space: normal;
    overflow: visible;
    text-align: left;
}

.expanded h3 {
    font-size: 4.0rem;
}

.expanded .album-details {
    font-size: 2.5rem;
}
</style>
