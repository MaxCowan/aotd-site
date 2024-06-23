<script>
import { onMount } from 'svelte';
import AlbumCardWrapper from './AlbumCardWrapper.svelte';

export let searchTerm = "";
let albumsJson = [];
let filteredAlbums = [];

async function fetchData() {
    try {
        const response = await fetch('/aotd_sheet_data_raw.json');
        albumsJson = await response.json();
        filterAlbums();
    } catch (error) {
        console.error('Error fetching albums data:', error);
    }
}

function filterAlbums() {
    if (searchTerm) {
        const lowerSearchTerm = searchTerm.toLowerCase();
        const exactMatches = albumsJson.filter(album => album.name.toLowerCase() === lowerSearchTerm);
        const partialMatches = albumsJson.filter(album => album.name.toLowerCase().includes(lowerSearchTerm) && album.name.toLowerCase() !== lowerSearchTerm);
        filteredAlbums = [...exactMatches, ...partialMatches];
    } else {
        filteredAlbums = albumsJson;
    }
}

$: {
    if (albumsJson.length > 0 || searchTerm) {
        filterAlbums();
    }
}

onMount(() => {
    fetchData();
});
</script>

<div class="album-grid">
    {#each filteredAlbums as album (album.name + album.artist)}
        <AlbumCardWrapper {album} />
    {/each}
</div>

<style>
.album-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(254px, 1fr));
    gap: 25px;
    box-sizing: border-box;
    width: 100%;
    overflow: visible;
    padding: 25px;
}
</style>
