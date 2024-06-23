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
}

.expanded .back-content {
    pointer-events: auto;
}

h3 {
    margin: 0;
    padding: 1rem 0;
}

.album-details {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    margin-top: 1rem;
    font-size: 0.9rem;
    text-align: left;
    width: 100%;
    padding: 0 0.5rem;
    box-sizing: border-box;
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
</style>
