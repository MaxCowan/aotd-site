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
        <h3 class="title">{album.name}</h3>
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
:root {
    --title-font-size: 1.5rem;
    --details-font-size: 1rem;
}

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
    align-items: flex-start; /* Align to top for better scaling */
    backface-visibility: hidden;
    border-radius: 0.5rem;
    overflow: hidden; /* Maintain card boundaries */
    padding: 1rem;
    box-sizing: border-box;
    z-index: 2;
    transition: all 0.4s ease;
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
    transition: background-color 0.4s ease;
    background-color: transparent;
}

.expanded .back-content {
    pointer-events: auto;
    background-color: rgba(0, 0, 0, 0.8); /* Optional: Darken background when expanded */
}

.title {
    margin: 0;
    padding: 1rem 0;
    font-size: var(--title-font-size);
    transition: font-size 0.4s ease;
}

.album-details {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    margin-top: 1rem;
    font-size: var(--details-font-size);
    text-align: left;
    width: 100%;
    padding: 0 0.5rem;
    box-sizing: border-box;
    overflow-y: auto;
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

/* Adjust font sizes when expanded */
.album-card-back.expanded {
    --title-font-size: 2.5rem; /* Scale up title */
    --details-font-size: 1.5rem; /* Scale up details */
}
</style>
