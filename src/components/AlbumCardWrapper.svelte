<script>
import { onMount } from 'svelte';
import { currentExpanded } from '../stores';
import { get } from 'svelte/store';
import AlbumCardFront from './AlbumCardFront.svelte';
import AlbumCardBack from './AlbumCardBack.svelte';

export let album;
let cardElement;
let placeholderElement;
let originalRect;
let isExpanded = false;
let isFlipped = false;

function toggleExpand(event) {
    const current = get(currentExpanded);

    if (current && current !== cardElement) {
        return; // Do nothing if another card is currently expanded
    }

    if (current === cardElement) {
        cardElement.style.transition = 'all 0.4s ease';
        cardElement.style.transform = 'none';

        setTimeout(() => {
            placeholderElement.style.display = 'none';
            cardElement.style.position = '';
            cardElement.style.top = '';
            cardElement.style.left = '';
            cardElement.style.width = '';
            cardElement.style.height = '';
            cardElement.style.transform = '';
            cardElement.style.zIndex = '';
            cardElement.style.transition = '';
            currentExpanded.set(null);
            isExpanded = false;
            isFlipped = false;
        }, 400);

        document.body.style.overflow = '';
    } else {
        originalRect = cardElement.getBoundingClientRect();
        placeholderElement.style.display = 'block';
        placeholderElement.style.width = `${originalRect.width}px`;
        placeholderElement.style.height = `${originalRect.height}px`;

        cardElement.style.position = 'fixed';
        cardElement.style.top = `${originalRect.top}px`;
        cardElement.style.left = `${originalRect.left}px`;
        cardElement.style.width = `${originalRect.width}px`;
        cardElement.style.height = `${originalRect.height}px`;
        cardElement.style.zIndex = '10';
        cardElement.style.transition = 'all 0.4s ease';

        // Flip the card immediately
        isFlipped = true;

        setTimeout(() => {
            requestAnimationFrame(() => {
                const viewportWidth = window.innerWidth;
                const viewportHeight = window.innerHeight;

                const translateX = (viewportWidth / 2 - originalRect.left - originalRect.width / 2);
                const translateY = (viewportHeight / 2 - originalRect.top - originalRect.height / 2);

                cardElement.style.transform = `translate(${translateX}px, ${translateY}px) scale(2.5)`;
            });
        }, 500); // Wait for the flip animation to complete

        currentExpanded.set(cardElement);
        document.body.style.overflow = 'hidden';
        isExpanded = true;
    }

    event.stopPropagation();
}

function handleClose(event) {
    if (get(currentExpanded) === cardElement) {
        toggleExpand(event);
    }
}

function handleKeyPress(event) {
    if (event.key === 'Enter' || event.key === ' ') {
        toggleExpand(event);
    }
}
</script>

<div bind:this={placeholderElement} class="album-card-placeholder"></div>
<div bind:this={cardElement} class="album-card-wrapper" on:click={handleClose} role="button" tabindex="0" on:keypress={handleKeyPress}>
    <div class="album-card {isExpanded ? 'expanded' : ''} {isFlipped ? 'flipped' : ''}" on:click={toggleExpand} role="button" tabindex="0" aria-expanded={get(currentExpanded) === cardElement} aria-label={`Toggle expand for ${album.name}`} on:keypress={handleKeyPress}>
        <div class="album-card-inner">
            <AlbumCardFront {album} />
            <AlbumCardBack {album} {isExpanded} />
        </div>
    </div>
</div>

<style>
.album-card-wrapper {
    position: relative;
    display: inline-block;
}

.album-card-placeholder {
    display: none;
    visibility: hidden;
}

.album-card {
    position: relative;
    width: 100%;
    padding-top: 100%;
    border-radius: 0.5rem;
    overflow: hidden;
    transition: transform 0.4s, box-shadow 0.4s;
    font-family: inherit;
    box-sizing: border-box;
    cursor: pointer;
    transform-style: preserve-3d;
    perspective: 1000px;
}

.album-card:hover {
    transform: scale(1.05);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
}

.album-card.expanded {
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5);
}

.album-card-inner {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    transform-style: preserve-3d;
    transition: transform 0.6s;
}

.album-card.flipped .album-card-inner {
    transform: rotateY(180deg);
}
</style>
