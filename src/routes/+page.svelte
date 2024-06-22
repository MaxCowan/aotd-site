<script>
import { onMount, afterUpdate } from 'svelte';
import AlbumCard from "../components/albumCard.svelte";

let albumsJson = [];
let searchTerm = "";
let filteredAlbums = [];
let containerElement;

async function fetchData() {
    try {
        console.log('Fetching data from /aotd_sheet_data_raw.json');
        const response = await fetch('/aotd_sheet_data_raw.json');
        albumsJson = await response.json();
        filteredAlbums = albumsJson;
        console.log('Fetched and set albums data:', albumsJson.length);
    } catch (error) {
        console.error('Error fetching albums data:', error);
    }
}

$: if (albumsJson.length > 0) {
    console.log('Filtering albums');
    filteredAlbums = searchTerm
        ? albumsJson.filter(album => album.name.toLowerCase().includes(searchTerm.toLowerCase()))
        : albumsJson;
    console.log('Updated filteredAlbums:', filteredAlbums.length, searchTerm);
}

onMount(() => {
    console.log('Component mounted, fetching data');
    fetchData();
});
</script>

<svelte:head>
    <title>Albums</title>
</svelte:head>

<div class="container" bind:this={containerElement}>
    <input class="search-bar" bind:value={searchTerm} placeholder="Search Albums" />
    <div class="album-grid">
        {#each filteredAlbums as album, index (album.name + index)}
            <AlbumCard {album} />
        {/each}
    </div>
</div>

<style>
.container {
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 100vh;
    overflow-y: auto;
    box-sizing: border-box;
    font-family: inherit;
}

.search-bar {
    width: 100%;
    padding: 1rem;
    font-size: 1.25rem;
    border: 2px solid gray;
    border-radius: 0;
    box-sizing: border-box;
    margin-bottom: 1rem;
    font-family: inherit;
}

.album-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(254px, 1fr));
    gap: 25px;
    padding: 1rem;
    box-sizing: border-box;
    width: 100%;
}
</style>
