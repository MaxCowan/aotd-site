<script>
import { onMount } from 'svelte';
import InfiniteLoading from 'svelte-infinite-loading';
import AlbumCardWrapper from './AlbumCardWrapper.svelte';

let albumsJson = [];
let filteredAlbums = [];
let displayedAlbums = [];
let currentPage = 0;
let pageSize = 20;
let infiniteId = Symbol();
export let searchTerm = "";

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
    resetDisplayedAlbums();
}

function resetDisplayedAlbums() {
    displayedAlbums = [];
    currentPage = 0;
    infiniteId = Symbol();
}

function loadMoreAlbums({ detail: { loaded, complete } }) {
    const start = currentPage * pageSize;
    const end = start + pageSize;
    const newAlbums = filteredAlbums.slice(start, end);
    console.log(`Loading more albums: start=${start}, end=${end}, newAlbums.length=${newAlbums.length}`);
    
    if (newAlbums.length) {
        displayedAlbums = [...displayedAlbums, ...newAlbums];
        currentPage += 1;
        loaded();
        console.log(`New page: ${currentPage}, displayedAlbums.length=${displayedAlbums.length}`);
    } else {
        complete();
        console.log('No more albums to load');
    }
}

$: if (searchTerm) {
    filterAlbums();
}

onMount(() => {
    fetchData();
});
</script>

<div class="album-grid">
    {#each displayedAlbums as album (album.name + album.artist)}
        <AlbumCardWrapper {album} />
    {/each}
    <InfiniteLoading on:infinite={loadMoreAlbums} identifier={infiniteId} />
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
