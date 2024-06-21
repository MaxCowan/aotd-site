<script>
import AlbumCard from "../components/albumCard.svelte";
import albumsRawJson from '../../static/aotd_sheet_data_raw.json';
import { onMount } from 'svelte';

const albumsJson = albumsRawJson;

let searchTerm = "";
let filteredAlbums = albumsJson;
let visibleAlbums = [];
const albumsPerPage = 50;
let currentPage = 1;
let containerElement;

$: {
    if (searchTerm) {
        filteredAlbums = albumsJson.filter(album => album.name.toLowerCase().includes(searchTerm.toLowerCase()));
    } else {
        filteredAlbums = albumsJson;
    }
    visibleAlbums = filteredAlbums.slice(0, albumsPerPage * currentPage);
    console.log('Updated visibleAlbums:', visibleAlbums.length);
}

function loadMore() {
    if (visibleAlbums.length < filteredAlbums.length) {
        currentPage += 1;
        visibleAlbums = filteredAlbums.slice(0, albumsPerPage * currentPage);
        console.log('Loading more albums, current page:', currentPage, 'visibleAlbums:', visibleAlbums.length);
    }
}

function handleScroll() {
    const { scrollTop, scrollHeight, clientHeight } = containerElement;
    console.log('Scroll values:', { scrollTop, scrollHeight, clientHeight });
    if (scrollTop + clientHeight >= scrollHeight - 100) {
        loadMore();
    }
}

onMount(() => {
    containerElement.addEventListener('scroll', handleScroll);
    return () => containerElement.removeEventListener('scroll', handleScroll);
});
</script>

<svelte:head>
    <title>Albums</title>
</svelte:head>

<div class="container" bind:this={containerElement}>
    <input class="search-bar" bind:value={searchTerm} placeholder="Search Albums" />
    <div class="album-grid">
        {#each visibleAlbums as album}
            <AlbumCard {album} />
        {/each}
    </div>
</div>

<style>
.container {
    display: flex;
    flex-direction: column;
    height: 100vh;
    width: 100%;
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
    flex-grow: 1;
    font-family: inherit;
}
</style>
