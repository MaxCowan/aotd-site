<script>
import AlbumCard from "../components/albumCard.svelte";
import albumsRawJson from '../../static/aotd_sheet_data_raw.json';

const albumsJson = albumsRawJson;

let searchTerm = "";
let filteredAlbums = albumsJson;

$: {
    if (searchTerm) {
        filteredAlbums = albumsJson.filter(album => album.name.toLowerCase().includes(searchTerm.toLowerCase()));
    } else {
        filteredAlbums = albumsJson;
    }
}
</script>

<svelte:head>
    <title>Albums</title>
</svelte:head>

<div class="container">
    <input class="search-bar" bind:value={searchTerm} placeholder="Search Albums" />
    <div class="album-grid">
        {#each filteredAlbums as album}
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
    overflow-y: auto;
    padding: 1rem;
    box-sizing: border-box;
    width: 100%;
    height: calc(100vh - 2rem - 2px - 1rem - 2px - 1rem);
    flex-grow: 1;
    font-family: inherit;
}
</style>
