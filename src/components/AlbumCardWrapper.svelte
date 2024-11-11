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
        // Collapse the card
        collapseCard();
    } else {
        // Expand the card
        expandCard();
    }

    event.stopPropagation();
}

function expandCard() {
    originalRect = cardElement.getBoundingClientRect();
    placeholderElement.style.display = 'block';
    placeholderElement.style.width = `${originalRect.width}px`;
    placeholderElement.style.height = `${originalRect.height}px`;

    // Set initial fixed position
    cardElement.style.position = 'fixed';
    cardElement.style.top = `${originalRect.top}px`;
    cardElement.style.left = `${originalRect.left}px`;
    cardElement.style.width = `${originalRect.width}px`;
    cardElement.style.height = `${originalRect.height}px`;
    cardElement.style.zIndex = '10';
    cardElement.style.transition = 'all 0.4s ease';
    cardElement.style.transformOrigin = 'center center';

    // Flip the card first
    isFlipped = true;

    // Wait for the flip to complete before expanding
    setTimeout(() => {
        // Calculate center position
        const viewportWidth = window.innerWidth;
        const viewportHeight = window.innerHeight;
        const targetWidth = 600; // Adjust as needed
        const targetHeight = 600; // Adjust as needed

        const targetTop = (viewportHeight - targetHeight) / 2;
        const targetLeft = (viewportWidth - targetWidth) / 2;

        // Apply expansion
        cardElement.style.top = `${targetTop}px`;
        cardElement.style.left = `${targetLeft}px`;
        cardElement.style.width = `${targetWidth}px`;
        cardElement.style.height = `${targetHeight}px`;

        isExpanded = true;
        currentExpanded.set(cardElement);
        document.body.style.overflow = 'hidden';
    }, 600); // Match this timeout with the flip transition duration (0.6s)
}

function collapseCard() {
    // Revert to original size and position
    cardElement.style.transition = 'all 0.4s ease';
    cardElement.style.width = `${originalRect.width}px`;
    cardElement.style.height = `${originalRect.height}px`;
    cardElement.style.top = `${originalRect.top}px`;
    cardElement.style.left = `${originalRect.left}px`;
    isExpanded = false;

    // After transition, flip the card back
    setTimeout(() => {
        isFlipped = false; // Flip back after shrinking
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
        document.body.style.overflow = '';
    }, 400); // Match this timeout with the shrink transition duration (0.4s)
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
            <AlbumCardBack {album} isExpanded={isExpanded} />
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
    transition: all 0.4s ease, box-shadow 0.4s ease;
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
    transform: none !important;
}

.album-card-inner {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    transform-style: preserve-3d;
    transition: transform 0.6s ease;
}

.album-card.flipped .album-card-inner {
    transform: rotateY(180deg);
}

/* Prevent hover effects on the entire card when expanded */
:global(.album-card.expanded) {
    transform: none !important;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5);
}

/* Apply hover effects only to the front face when not expanded */
:global(.album-card:not(.expanded):hover .album-card-front .album-image) {
    transform: scale(1.05);
    filter: blur(2px);
}

:global(.album-card:not(.expanded):hover .album-info) {
    opacity: 1;
    transform: translateY(0);
}

/* Ensure no scaling-related styles remain */
:global(.album-card.expanded .album-image) {
    transform: none;
    filter: none;
}
</style>
