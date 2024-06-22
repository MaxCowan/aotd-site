<script>
import { onMount } from 'svelte';
import AlbumCard from './AlbumCard.svelte';

export let searchTerm = "";
let albumsJson = [];
let filteredAlbums = [];

async function fetchData() {
    try {
        console.log('Fetching data from /aotd_sheet_data_raw.json');
        const response = await fetch('/aotd_sheet_data_raw.json');
        albumsJson = await response.json();
        console.log('Fetched and set albums data:', albumsJson.length);
        filterAlbums();
    } catch (error) {
        console.error('Error fetching albums data:', error);
    }
}

function filterAlbums() {
    console.log('Filtering albums with searchTerm:', searchTerm);
    if (searchTerm) {
        const lowerSearchTerm = searchTerm.toLowerCase();
        const exactMatches = albumsJson.filter(album => album.name.toLowerCase() === lowerSearchTerm);
        const partialMatches = albumsJson.filter(album => album.name.toLowerCase().includes(lowerSearchTerm) && album.name.toLowerCase() !== lowerSearchTerm);
        filteredAlbums = [...exactMatches, ...partialMatches];
    } else {
        filteredAlbums = albumsJson;
    }
    console.log('Filtered albums:', filteredAlbums.length);
}

$: if (albumsJson.length > 0 || searchTerm) {
    filterAlbums();
    console.log('Search term or albumsJson changed, filtering albums.');
}

onMount(() => {
    fetchData();
});
</script>

<div class="album-grid">
    {#each filteredAlbums as album (album.name + album.artist)}
        <AlbumCard {album} />
    {/each}
</div>

<style>
.album-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(254px, 1fr));
    gap: 25px;
    box-sizing: border-box;
    width: 100%;
}
</style>
